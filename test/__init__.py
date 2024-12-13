import unittest
import typing
import random
from argparse import Namespace

from test.bases import WorldTestBase
from test.general import gen_steps
from BaseClasses import CollectionState, MultiWorld
from Generate import get_seed_name
from worlds.AutoWorld import call_all, AutoWorldRegister
from .. import PseudoWorld


def setup_pseudo_options(options: typing.Dict[str, typing.Any], seed: typing.Optional[int] = None) -> None:
    player = 1
    game = "Pseudoregalia"

    multiworld = MultiWorld(1)
    multiworld.game[player] = game
    multiworld.player_name = {player: "Tester"}
    multiworld.set_seed(seed)
    multiworld.state = CollectionState(multiworld)
    random.seed(multiworld.seed)
    multiworld.seed_name = get_seed_name(random)  # only called to get same RNG progression as Generate.py
    args = Namespace()
    for name, option in AutoWorldRegister.world_types[game].options_dataclass.type_hints.items():
        setattr(args, name, {
            1: option.from_any(options.get(name, option.default))
        })
    multiworld.set_options(args)
    for step in gen_steps:
        call_all(multiworld, step)
    return multiworld


class SpawnsTests(unittest.TestCase):

    # pulled and modified from core test_reachability
    def test_all_spawn_empty_state_can_reach_something(self):
        """Ensure empty state can reach at least one location with the defined options"""
        from ..data.spawns import spawns

        for i, spawn_name in enumerate(spawns):
            with self.subTest("Spawn", spawn=spawn_name):
                multiworld = setup_pseudo_options({"spawn": i})
                state = CollectionState(multiworld)
                all_locations = multiworld.get_locations()
                if all_locations:
                    locations = set()
                    for location in all_locations:
                        if location.can_reach(state):
                            locations.add(location)
                    self.assertGreater(len(locations), 0,
                                       msg="Need to be able to reach at least one location to get started.")


class PseudoTestBase(WorldTestBase):
    game = "Pseudoregalia"
    # player: typing.ClassVar[int] = 1
    seed: typing.Optional[int] = None
    world: PseudoWorld

    def world_setup(self, *args, **kwargs):
        super().world_setup(self.seed)
        # None is default and uses random seed
