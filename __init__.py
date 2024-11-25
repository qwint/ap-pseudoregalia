from collections import Counter
from typing import List, Dict, Any, Tuple, NamedTuple, Optional, cast, Set

from BaseClasses import Location, Item, ItemClassification, Tutorial, CollectionState, MultiWorld, Region, Entrance, LocationProgressType
from worlds.AutoWorld import World, WebWorld

from .template_world import RandomizerCoreWorld
from .data.region_data import regions, locations, transition_to_region_map
from .data.spawns import spawns

from .items import PseudoregaliaItem, item_table, item_frequencies, item_groups, item_term_lookup
from .options import pseudoregalia_options


gamename = "Pseudoregalia"
base_id = 2365810001


class RCRule(NamedTuple):
    items: Dict[str, int]
    regions: List[str]


class PseudoLocation(Location):
    game: str = gamename
    rules: List[Dict[str, int]]

    def static_access_rule(self, state: CollectionState) -> bool:
        for clause in self.rules:
            if state.has_all_counts(clause.items, self.player):
                if all(state.can_reach_region(r, self.player) for r in clause.regions):
                    return True
        # no clause was True,
        return False

    def set_rule(self, rules: List[RCRule]):
        self.rules = rules
        self.access_rule = self.static_access_rule


class PseudoEntrance(Entrance):
    rules: List[Dict[str, int]]

    def static_access_rule(self, state: CollectionState) -> bool:
        for clause in self.rules:
            if state.has_all_counts(clause.items, self.player):
                if all(state.can_reach_region(r, self.player) for r in clause.regions):
                    return True
        # no clause was True,
        return False

    def set_rule(self, rules: List[RCRule]):
        self.rules = rules
        self.access_rule = self.static_access_rule


class PseudoRegion(Region):
    entrance_type = PseudoEntrance


event_locations = [location["name"] for location in locations if location["is_event"]]

rc_regions = [region for region in cast(List[Dict[str, Any]], regions)]
rc_locations = [location for location in cast(List[Dict[str, Any]], locations)]


datapackage_locs = {loc["name"] for loc in locations if not loc["is_event"]}
location_name_to_id = {
    location_name: location_id for location_id, location_name in
    enumerate(sorted(datapackage_locs), start=base_id)
}


class PseudoWorld(RandomizerCoreWorld, World):
    """
    When reality feels like it's falling apart, one might retreat to a world in their dreams to escape it.

    Unfortunately, dreams aren't made to last.
    """  # https://rittzler.itch.io/pseudoregalia

    game = gamename
    # web = PseudoWeb()
    location_name_to_id = location_name_to_id
    item_name_to_id = {item: data.code for item, data in item_table.items()}
    options_dataclass = pseudoregalia_options
    options: pseudoregalia_options
    item_name_groups = item_groups

    rc_regions: List[Dict[str, Any]] = rc_regions
    rc_locations: List[Dict[str, Any]] = rc_locations
    item_class = PseudoregaliaItem
    location_class = PseudoLocation
    region_class = PseudoRegion

    collect_translate = {
        "Cling Gem": {"Cling Part": 6},
        "Sun Greaves": {"Air Kick": 3},
        "Heliacal Power": {"Air Kick": 1},
        "Dream Breaker": {"Progressive Dream Breaker": 1},
        "Strikebreak": {"Progressive Dream Breaker": 1},
        "Soul Cutter": {"Progressive Dream Breaker": 1},
        "Slide": {"Progressive Slide": 1},
        "Solar Wind": {"Progressive Slide": 1},
    }

    trick_translate = {
        "ClingAbuse": "cling_abuse",
        "Knowledge": "knowledge",
        "Movement": "movement",
        "OneWall": "one_wall",
        "ReverseKick": "reverse_kick",
        "SunsetterAbuse": "sunsetter_abuse",
        "Momentum": "momentum",
    }
    difficulty_translate = {
        "Disabled": 0,  # shouldn't ever be in logic, but here for completeness
        "Normal": 1,
        "Advanced": 2,
        "Expert": 3,
        "Insane": 4,
    }

# black box methods
    def get_region_list(self) -> List[str]:
        ret = super().get_region_list()
        ret.append("Menu")
        return ret

    def get_connections(self) -> "List[Tuple(str, str, Optional[Any])]":
        ret = super().get_connections()
        print(f"Connecting menu to {spawns[self.options.spawn.current_region]}")
        ret.append(("Menu", spawns[self.options.spawn.current_region], None))
        return ret

    def get_location_map(self) -> "List[Tuple(str, str, Optional[Any])]":
        ret = super().get_location_map()
        for o in (self.options.shuffle_goatlings, self.options.shuffle_notes, self.options.shuffle_chairs):
            if not o:
                # if any option is off, remove locations tied to that option
                ret = [r for r in ret if r[1] not in o.locations]
        return ret

    def create_rule(self, rule: Any) -> List[Dict[str, int]]:
        def parse_item_logic(reqs: list) -> Tuple[bool, Counter[str]]:  # Mapping[str, int]:
            # handle both keys of item name and keys of itemname>count
            ret: Counter[str] = Counter()
            for full_req in reqs:
                if full_req.startswith("Powerup_"):
                    req = full_req[8:]
                    if "_" in req:
                        req, count = req.split("_")
                    else:
                        req = req
                        count = 1
                    # if req.startswith("ClingGem_"):
                    #     ret["Cling Gem"] += int(req[-1:])
                    if req in item_term_lookup:
                        # handle when upstream has both progressiveslide_1 and progressiveslide_2
                        if ret[item_term_lookup[req]] < int(count):
                            ret[item_term_lookup[req]] = int(count)
                    else:
                        raise Exception(f"Unknown powerup {req}")
                    # print(req)
                elif full_req == "Lock::SmallKey":
                    ret["Small Key"] = 4  # TODO make this variable / fix
                    # print("SmallKey_4")
                elif full_req == "Lock::Ending":
                    for key in item_groups["major keys"]:
                        ret[key] = 1
                elif full_req.startswith("Trick_"):
                    # return skip_clause=True because the rest of the clause doesn't matter
                    _, category, level = full_req.split("_")
                    if getattr(self.options, self.trick_translate[category]) < self.difficulty_translate[level]:
                        # if our option value is less than the required for the clause, return skip=true
                        return True, {}
                elif full_req in ("CsMain", "EbEntryUnderBelly",):
                    # TODO temporary solution until i can get the extractor putting regions in regions
                    raise Exception(f"this should no longer be necessary {full_req}")
                else:
                    raise Exception(f"Unknown req {full_req}")

            return False, ret
        if rule is None:
            return None

        assert rule != []
        ret = []
        for clause in rule:
            assert not clause["location_requirements"] and not clause["state_modifiers"]

            skip_clause, items = parse_item_logic(clause["item_requirements"])
            if skip_clause:
                continue
            # TODO make this a named tuple again,,
            ret.append(RCRule(items=dict(items), regions=clause["region_requirements"]))

        return ret

    def set_rule(self, spot, rule):
        # set hk_rule instead of access_rule because our Location class defines a custom access_rule
        if rule is not None:
            spot.set_rule(rule)
        # else leave it as-is

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        change = super().collect(state, item)
        if change and item.name in self.collect_translate:
            for i, c in self.collect_translate[item.name].items():
                state.prog_items[item.player][i] += c
        return change

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        change = super().remove(state, item)
        if change and item.name in self.collect_translate:
            for i, c in self.collect_translate[item.name].items():
                state.prog_items[item.player][i] -= c
        return change

    def get_item_list(self) -> List[str]:
        ret = []
        for item, data in item_table.items():
            if data.code and data.can_create(self):
                if item in item_frequencies:
                    ret += [item] * item_frequencies[item]
                else:
                    ret.append(item)

        return ret

    def set_victory(self) -> None:
        multiworld = self.multiworld
        player = self.player

        multiworld.completion_condition[player] = lambda state: state.can_reach_region("FinalBoss", player)

    def get_item_classification(self, name: str) -> ItemClassification:
        if name not in item_table:
            return ItemClassification.filler

        return item_table[name].classification

    def get_filler_item_name(self) -> str:
        # return self.random.choice(self.get_filler_items())
        return "Empathy"

    def fill_slot_data(self) -> Dict[str, Any]:
        return self.options.as_dict(
            "progressive_breaker",
            "progressive_slide",
            "split_sun_greaves",
            "death_link",

            "cling_abuse",
            "knowledge",
            "movement",
            "one_wall",
            "reverse_kick",
            "sunsetter_abuse",
        )
