from . import PseudoTestBase, SpawnsTests


class TestGoal_any(PseudoTestBase):
    options = {
        "spawn": 0,
    }

# runs just importing it
# class TestSpawns(SpawnsTests):
#     pass
