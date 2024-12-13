import json
from typing import Optional, Any, NamedTuple, List, Tuple, Dict
from collections import Counter

"""
Example data transformation:

# source format (indent cleaned)
Check {
    description: "missable high walled room",
    location: L::StrongEyes,
    index: 284,
    drop: Drop::Health,
    trial: None,
    locks: All(&[
        Any(&[
            Powerup(A::DreamBreaker),
            All(&[Powerup(A::Sunsetter), Trick(T::Knowledge, D::Normal)]),
        ]),
        Any(&[
            All(&[Powerup(A::SunGreaves)]), 
            Powerup(A::ClingGem(4))
        ]),
    ]),
},

# object logic format after parsing
{"All": [{"Any": ["DreamBreaker", {"All": ["Sunsetter", "Normal_Knowledge"]}]}, {"Any": [{"All": ["SunGreaves"]}, "ClingGem4"]}]}

# flattened array logic format in expected Any(All()) format 
[['DreamBreaker', 'SunGreaves'], ['DreamBreaker', 'ClingGem4'], ['Sunsetter', 'Normal_Knowledge', 'SunGreaves'], ['Sunsetter', 'Normal_Knowledge', 'ClingGem4']]

# Extended logic format for StringWorldDefinition output 
{
    "Name": "missable high walled room",
    "Logic": [
        {
            "StateProvider": "StrongEyes",
            "Conditions": [
                "Powerup_ProgressiveDreamBreaker_1",
                "Powerup_AirKick_3"
            ],
            "StateModifiers": []
        },
        {
            "StateProvider": "StrongEyes",
            "Conditions": [
                "Powerup_ProgressiveDreamBreaker_1",
                "Powerup_ClingPart_4"
            ],
            "StateModifiers": []
        },
        {
            "StateProvider": "StrongEyes",
            "Conditions": [
                "Powerup_Sunsetter",
                "Trick_Knowledge_Normal",
                "Powerup_AirKick_3"
            ],
            "StateModifiers": []
        },
        {
            "StateProvider": "StrongEyes",
            "Conditions": [
                "Powerup_Sunsetter",
                "Trick_Knowledge_Normal",
                "Powerup_ClingPart_4"
            ],
            "StateModifiers": []
        }
    ],
    "Handling": "Location"
},

"""


def get_raw_from_url(url: str) -> str:
    import requests
    req = requests.get(url)
    assert req.status_code == 200
    return req.text



def parse_spawns_file(raw_file: Optional[str]) -> Dict[str, str]:
    if raw_file == None:
        raw_file = get_raw_from_url("https://raw.githubusercontent.com/pseudoregalia-modding/rando/refs/heads/main/src/logic/spawns.rs")
    lines = raw_file.split("\n")
    # remove comments
    tab = "    "
    lines = [line[len(tab):].split("//")[0] for line in lines if line.startswith(tab)]
    # strip commas, remove empty lines, remove parenthesis
    lines = [line.strip(", ")[1:-1] for line in lines if line]
    ret = {}
    # expecting format ("gameStart", L::EarlyPrison),
    for line in lines:
        # remove trailing commas and split the tuple
        key, value = line.split(", ")
        # remove the string literal quotes
        key = key.strip('"')
        # remove L:: prefix on region name
        value = value[3:]
        # add key/value pair to output blob
        ret[key] = value
    return ret


class Check(NamedTuple):
    """Object format for directly parsed upstream "Check" format"""
    description: str
    location: str
    index: int
    drop: str
    trial: Optional[str]
    locks: Optional[Any]


def parse_checks_file(raw_file: Optional[str]) -> List[Check]:
    if raw_file == None:
        raw_file = get_raw_from_url("https://raw.githubusercontent.com/pseudoregalia-modding/rando/refs/heads/main/src/logic/checks.rs")
    lines = raw_file.split("\n")
    # remove comments
    tab = "    "
    lines = [line[len(tab):].split("//")[0] for line in lines if line.startswith(tab)]

    raw_checks = []
    index = -1
    prev_key = None
    for line in lines:
        # ignore the open/close of the Check object
        if line.startswith("Check"):
            index += 1
            raw_checks.append({})
        elif line.startswith("}"):
            pass

        # if there is no `key: value` then it needs to be appended to previous key
        elif len(line.strip().split(": ", 1)) == 1:
            raw_checks[index][prev_key] += line.strip()
        # pull out key value pairs and save to raw_checks dict removing trailing commas and whitepace
        else:
            key, value = line.strip().split(": ", 1)
            prev_key = key
            raw_checks[index][prev_key] = value.rstrip(",")

    # from https://github.com/UltiNaruto/rando/blob/archipelago/src/config.rs
    name_index_overrides = [
        "",
        "Dilapidated Dungeon - Time Trial",
        "Dilapidated Dungeon - Dream Breaker",
        "Dilapidated Dungeon - Alcove Near Mirror",
        "Dilapidated Dungeon - Slide",
        "Dilapidated Dungeon - Dark Orbs",
        "Dilapidated Dungeon - Rafters",
        "Dilapidated Dungeon - Past Poles",
        "Dilapidated Dungeon - Strong Eyes",
        "",
        "Castle Sansa - Memento",
        "",
        "",
        "",
        "",
        "Castle Sansa - Indignation",
        "Castle Sansa - Platform In Main Halls",
        "",
        "Castle Sansa - Time Trial",
        "Castle Sansa - Corner Corridor",
        "Castle Sansa - Wheel Crawlers",
        "Castle Sansa - Alcove Near Scythe Corridor",
        "",
        "Castle Sansa - Near Theatre Front",
        "Castle Sansa - Tall Room Near Wheel Crawlers",
        "Castle Sansa - Alcove Near Dungeon",
        "",
        "Castle Sansa - Balcony",
        "",
        "",
        "Castle Sansa - Floater In Courtyard",
        "Castle Sansa - High Climb From Courtyard",
        "",
        "Listless Library - Time Trial",
        "Listless Library - Sun Greaves",
        "",
        "",
        "",
        "Listless Library - Upper Back",
        "Listless Library - Locked Door Across",
        "Listless Library - Locked Door Left",
        "",
        "",
        "",
        "Sansa Keep - Strikebreak",
        "Sansa Keep - Sunsetter",
        "Sansa Keep - Alcove Near Locked Door",
        "Sansa Keep - Levers Room",
        "Sansa Keep - Near Theatre",
        "Sansa Keep - Lonely Throne",
        "Sansa Keep - Time Trial",
        "",
        "",
        "Empty Bailey - Inside Building",
        "Empty Bailey - Guarded Hand",
        "Empty Bailey - Solar Wind",
        "Empty Bailey - Center Steeple",
        "Empty Bailey - Cheese Bell",
        "Empty Bailey - Time Trial",
        "The Underbelly - Rafters Near Keep",
        "The Underbelly - Surrounded By Holes",
        "The Underbelly - Ascendant Light",
        "The Underbelly - Alcove Near Light",
        "The Underbelly - Main Room",
        "",
        "The Underbelly - Strikebreak Wall",
        "The Underbelly - Time Trial",
        "The Underbelly - Locked Door",
        "",
        "",
        "The Underbelly - Building Near Little Guy",
        "Tower Remains - Cling Gem",
        "Tower Remains - Atop The Tower",
        "Tower Remains - Time Trial",
        "Twilight Theatre - Corner Beam",
        "Twilight Theatre - Time Trial",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "Twilight Theatre - Murderous Goat",
        "",
        "",
        "",
        "Twilight Theatre - Center Stage",
        "Twilight Theatre - Soul Cutter",
        "Twilight Theatre - Back Of Auditorium",
        "Twilight Theatre - Locked Door",
    ]

    # define overrides for names that are not unique
    name_overrides = {
        "a chair next to the goatling who wants to lick the checkpoint": [
            "the first chair next to the goatling who wants to lick the checkpoint",
            "the second chair next to the goatling who wants to lick the checkpoint",
            "the third chair next to the goatling who wants to lick the checkpoint",
        ],
        "the locked up time trial": [
            "the first locked up time trial",
            "the second locked up time trial",
            "the third locked up time trial",
        ],
        "a chair around the table": [
            "the first chair around the table",
            "the second chair around the table",
            "the third chair around the table",
        ],
        "the goatling who really wanted to see the show": [
            "the first goatling who really wanted to see the show",
            "the second goatling who really wanted to see the show",
        ],
        "behind the locked door": [
            "behind the first locked door",
            "behind the second locked door",
        ]
    }

    checks = []
    for c in raw_checks:
        # strip string literal quotes
        description = c["description"].strip('"')
        # if name in override, pop a name to force them unique
        if description in name_overrides:
            description = name_overrides[description].pop()
        name = name_index_overrides.pop(0)
        checks.append(Check(
            # description=description,
            description=name if name else description,
            location=c["location"][3:],  # strip L:: prefix
            index=int(c["index"]),
            drop=c["drop"][6:],  # strip Drop:: prefix
            trial=c["trial"] if c["trial"] != 'None' else None,
            locks=c["locks"] if c["locks"] != 'Lock::None' else None,  # reformat in translate_parse
            ))

    return checks


class Location(NamedTuple):
    """Object format for directly parsed upstream "Location" format"""
    parent: str
    logic: str


def parse_locations_file(raw_file: Optional[str]) -> List[Location]:
    if raw_file == None:
        raw_file = get_raw_from_url("https://raw.githubusercontent.com/pseudoregalia-modding/rando/refs/heads/main/src/logic/locations.rs")
    lines = raw_file.split("\n")

    # define a (fragile) end of section and trim lines so we can trust indenting
    end_line = [i for i, line in enumerate(lines) if line.startswith("    pub const fn file")][0]
    lines = lines[:end_line]
    
    # remove comments and indenting
    tab = "            "
    lines = [line[len(tab):].split("//")[0] for line in lines if line.startswith(tab)]

    raw_locations = []
    index = -1
    for line in lines:
        if not line:
            # skip empty (comments trimmed) lines
            continue
        # expect Location format as L::MainTheatre => Any(&[
        # if there is => delimiter in the line we need to start a new object and increment our index
        if "=>" in line:
            index += 1
            parent, logic = line.split("=>")
            raw_locations.append(
                {
                    "parent": parent.strip(),
                    "logic": logic.strip(),
                }
            )
        # if we aren't starting a new object, append to previous one
        else:
            raw_locations[index]["logic"] += line.strip()

    locations = []
    for c in raw_locations:
        locations.append(Location(
            parent=c["parent"].strip()[3:],  # strip L:: prefix
            logic=c["logic"],  # reformat in translate_parse
            ))

    return locations


def parse_logic(logic: str, title=None) -> List[Any]:
    def unknown_parse(part: str):
        """Translate whitespace stripped rust into json-ish blob of Any/All objects containing Tuples of requirements"""
        control_characters = ("(", ")", "[", "]", "&", ",")
        current_string = ""
        assert part

        # if there are no control characters, just return as-is
        if not any(c in part for c in control_characters):
            return part

        # loop through characters in current part, breaking on control character
        for i, c in enumerate(part):
            if c not in control_characters:
                current_string += c
            else:
                break

        # remove any leading whitespace from control text
        current_string = current_string.strip()

        if current_string in ("All", "Any"):
            # remove Any/All prefix and stripping (&[ prefix and ]) suffix regardless of commas
            substring = part[i+3:].rstrip(",")[:-2].rstrip(",")

            # handle_cs translates comma seperated string of values into a list
            subparts = handle_cs(substring)

            # pass each substring into unknown_parse and roll up into output blob
            return {current_string: [unknown_parse(p) for p in subparts if p is not None]}

        elif current_string in ("Powerup", "Trick", "Loc"):
            # expecting Powerup(item) so find next end paren to know full token
            value = part.find(")", i)
            text = part[i+1:value]
            # may get Powerup(item(subvalue)) this handles that case and converts it to item_subvalue
            if "(" in text:
                s_value = part.find("(", i+1)
                e_value = part.find(")", i+1)
                text = part[i+1:s_value] + "_" + part[s_value+1:e_value]

            return (current_string, text)
        else:
            raise Exception(f"Unknown control text \'{current_string}\' handling part \'{part}\'")

    def handle_cs(substring: str) -> List:
        """Handles comma seperated value string of arbitrary rust code into a list of substrings following brackets"""
        counter = Counter()  # counter of brackets to know when we aren't in a subfunction
        indicies = [0]  # indicies to split into substrings by
        groupers = {
            ")": "(",
            "]": "[",
            }  # bracket lookup so the ending brackets decrement the correct key

        for i, c in enumerate(substring):
            # loop through values in substring, saving commas if we don't have any orphaned brackets
            if c == "," and all(not count for count in counter.values()):
                indicies.append(i)

            # keep track of if we started a new list of things
            if c in groupers.values():
                counter[c] += 1
            # keep track of if we ended a new list of things
            elif c in groupers.keys():
                counter[groupers[c]] -= 1

        # https://stackoverflow.com/a/10851479
        # breaks the substring at defined indicies, the stripping any trailing commas and spaces from the output
        subparts = [substring[i:j].strip(", ") for i, j in zip(indicies, indicies[1:]+[None])]
        return subparts

    progressive_lookup = {
        "SunGreaves": "AirKick_3",
        "HeliacalPower": "AirKick_1",
        "DreamBreaker": "ProgressiveDreamBreaker_1",
        "Strikebreak": "ProgressiveDreamBreaker_2",
        "SoulCutter": "ProgressiveDreamBreaker_3",
        "Slide": "ProgressiveSlide_1",
        "SolarWind": "ProgressiveSlide_2",
    }

    def translate_parse(node) -> List[List[Any]]:
        """Translated parsed json-like blob into Any(All()) formatted List of Lists"""
        if isinstance(node, str):
            # Single strings are one requirement, just update to output format
            return [[node]]
        elif isinstance(node, Tuple):
            if node[0] == "Powerup":
                name = node[1][3:]
                # Tuples are (Powerup, A::SunGreaves) so translate into one downstream-parsable string
                if name in progressive_lookup:
                    # translate to a progressive value if relevent and let collect override handle
                    return translate_parse(f"{node[0]}_{progressive_lookup[name]}")
                elif name.startswith("ClingGem"):
                    # Translate to ClingParts and let collect override handle the value of each cling item
                    return translate_parse(f"{node[0]}_ClingPart_{node[1].split('_')[1]}")
                else:
                    return translate_parse(f"{node[0]}_{name}")
            elif node[0] == "Trick":
                # Tricks have a Trick and Difficulty parameter
                t, d = node[1].split(",")
                t = t.strip()[3:]
                d = d.strip()[3:]
                return translate_parse(f"{node[0]}_{t}_{d}")
            elif node[0] == "Loc":
                # convert from Location::Name to just Name so extractor registers them as the same regions
                return translate_parse(f"{node[0]}_{node[1].split('::')[1].strip()}")
            else:
                raise Exception(f"Unknown part {node}")
        elif "All" in node:
            # parents is all(any(all)), multiply all the arrays together
            # i.e. [[[A, B], [C]], [[D, E], [F]]] becomes
            # becomes [[A, B], [C]] * [[D, E], [F]]
            # [
            #     [A, B] + [D, E],
            #     [C] + [D, E],
            #     [A, B] + [F],
            #     [C] + [F],
            # ]

            parents = [translate_parse(n) for n in node["All"]]
            ret = [[]]
            for item in parents:
                ret = [r + i for r in ret for i in item]
            return ret
        elif "Any" in node:
            # parents is a list of valid outputs, so flatten one level
            # because any(any(a, b), any(c)) == any(a, b, c)
            parents = [translate_parse(n) for n in node["Any"]]
            return [i for parent in parents for i in parent]

    if logic is None:
        return None
    ret = translate_parse(unknown_parse(logic))
    return ret


def parse_checks_logic(logic: str, state_provider: str, title=None):
    logic_list = parse_logic(logic, title=title)
    if logic_list is None:
        return [
                {
                    "StateProvider": state_provider,
                    "Conditions": [],
                    "StateModifiers": []
                }
            ]
    # convert Loc_name format to expected Name/ format for StringWorldDefinition for can_reach_region references
    logic_list = [[i[4:] + "/" if i.startswith("Loc_") else i for i in logic_array] for logic_array in logic_list]
    return [
        {
            "StateProvider": state_provider,
            "Conditions": logic_array,
            "StateModifiers": []
        }
        for logic_array in logic_list
    ]


def parse_location_logic(logic: str, title=None):
    flat_logic = parse_logic(logic, title=title)
    ret = []
    for clause in flat_logic:
        # StringWorldDefinition needs one parent region per clause, so pull out the region requirements
        state_providers = [item for item in clause if item.startswith("Loc_")]
        if state_providers:
            # grab the first region and assume it's the parent region
            state_provider = state_providers[0]
            # remove the region from the output clause
            clause.remove(state_provider)
            # strip Loc_ prefix
            state_provider = state_provider[4:]

            # if there are more than just the one we picked add the rest as can_reach_region requirements
            if len(state_providers) > 1:
                raise Exception("I have code for this its just not tested yet")
                for region in state_providers[1:]:
                    clause.remove(region)
                    clause.append(region[4:] + "/")  # without Loc_ prefix and with the trailing slash format
        else:
            # if we don't have a region requirement for the clause, set to None so it'll export as json null which will become Menu
            state_provider = None
        ret.append(
           {
                "StateProvider": state_provider,
                "Conditions": clause,
                "StateModifiers": []
            }
        )
    return ret

# Create Location handling objects for all upstream Checks that will be transfered to AP Locations
checks = parse_checks_file(None)#checks_file)
location_objects = [
            {
                "Name": o.description,
                "Logic": parse_checks_logic(o.locks, o.location, title=o.description),
                "Handling": "Location"
            }
            for o in checks
        ]

# Default handling objects are waypoints that will be transfered to become AP regions
defaults = parse_locations_file(None)#locations_file)
default_objects = [
            {
                "Name": o.parent,
                "Logic": parse_location_logic(o.logic, title=o.parent),
                "Handling": "Default"
            }
            for o in defaults
        ]

# currently unused, mostly important for tracking shuffable transitions for entrance rando
transition_objects = [
            {
                "Name": o.description,
                "Logic": [],
                "Handling": "Transition"
            }
            for o in []
        ]

# Combine all logic objects into StringWorldDefinition format for output
output = {
    "LogicObjects": [*location_objects, *default_objects, *transition_objects],
}
with open("StringWorldDefinition.json", "w") as file:
    print("Writing to StringWorldDefinition.json")
    file.write(json.dumps(output, indent=4))


# write pool_lookups so locations can be skipped based on their vanilla items
drop_lookup = {c.description: c.drop[:c.drop.find("(")] if "(" in c.drop else c.drop for c in checks}
reverse_drop_lookup = {a: [b for b, c in drop_lookup.items() if c == a] for a in drop_lookup.values()}
# lookups for location name to/from vanilla item and print to file for use in apworld
with open("data/pool_lookups.py", "w") as file:
    print("Writing to pool_lookups.py")
    file.write("lookups = " + json.dumps(reverse_drop_lookup, indent=4))

# write spawns file for mapping non-vanilla start locations
spawns = parse_spawns_file(None)#spawns_file)
with open("data/spawns.py", "w") as file:
    print("Writing to spawns.py")
    file.write("spawns = " + json.dumps(spawns, indent=4) + "\n" +
               # add emptyRegionsToKeep, which is a subset of the config needed for extractor so logically useless regions don't get removed
               "emptyRegionsToKeep = " + json.dumps(sorted({region for region in spawns.values()}), indent=4))