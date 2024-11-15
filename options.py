from dataclasses import dataclass
from Options import Toggle, Choice, DefaultOnToggle, DeathLink, PerGameCommonOptions, AssembleOptions
from .data.pool_lookups import lookups
from .data.spawns import spawns


# stolen from hk
spawn_lookup = {i: s for i, s in enumerate(spawns)}
locations = {"option_" + start: i for i, start in spawn_lookup.items()}
# This way the dynamic start names are picked up by the MetaClass Choice belongs to
StartLocation = type("StartLocation", (Choice,), {
    **locations,
    "default": 0,
})


class StartSpawns(StartLocation):
    """The Location you spawn at."""
    @property
    def current_region(self):
        return spawn_lookup[self.value]


class SafeSmallKeys(DefaultOnToggle):
    """
    No locked doors are in logic until all small keys are obtainable.
    Prevents potential softlocks when spending small keys out of logic.

    Currently unused.
    """
    display_name = "Safe Small Keys"


class ProgressiveBreaker(DefaultOnToggle):
    """
    Replaces Dream Breaker, Strikebreak, and Soul Cutter with three Progressive Dream Breaker items.
    """
    display_name = "Progressive Dream Breaker"


class ProgressiveSlide(DefaultOnToggle):
    """
    Replaces Slide and Solar Wind with two Progressive Slide items.
    """
    display_name = "Progressive Slide"


class SplitSunGreaves(Toggle):
    """
    Replaces Sun Greaves and Heliacal Power with four individual Air Kicks.
    """
    display_name = "Split Sun Greaves"


class ShuffleGoatlings(Toggle):
    """
    Adds Goatlings to the location pool.
    """
    display_name = "Shuffle Goatlings"
    locations = lookups["Goatling"]


class ShuffleNotes(Toggle):
    """
    Adds Notes to the location pool.
    """
    display_name = "Shuffle Notes"
    locations = lookups["Note"]


class ShuffleChairs(Toggle):
    """
    Adds Chairs to the location pool.
    """
    display_name = "Shuffle Chairs"
    locations = lookups["Chair"]


class UpstreamTrick(Choice):
    option_disabled = 0
    option_normal = 1
    option_advanced = 2
    option_expert = 3
    option_insane = 4
    default = 1


class TrickClingAbuse(UpstreamTrick):
    """Abuse of cling to climb corners"""
    display_name = "Cling Abuse"


class TrickKnowledge(UpstreamTrick):
    """Things like enabling levers/breaking walls with sunsetter"""
    display_name = "Knowledge"


class TrickMovement(UpstreamTrick):
    """General movement such as backflips"""
    display_name = "Movement"


class TrickMomentum(UpstreamTrick):
    """Momentum conservation"""
    display_name = "Momentum"


class TrickOneWall(UpstreamTrick):
    """Single Wall wall-kicks"""
    display_name = "One Wall"


class TrickReverseKick(UpstreamTrick):
    """Reverse wall kicks"""
    display_name = "Reverse Kick"


class TrickSunsetterAbuse(UpstreamTrick):
    """Abuse the backflip"""
    display_name = "SunsetterAbuse"


@dataclass
class pseudoregalia_options(PerGameCommonOptions):
    # logic_level: LogicLevel
    # obscure_logic: ObscureLogic
    progressive_breaker: ProgressiveBreaker
    progressive_slide: ProgressiveSlide
    split_sun_greaves: SplitSunGreaves
    death_link: DeathLink

    cling_abuse: TrickClingAbuse
    knowledge: TrickKnowledge
    movement: TrickMovement
    momentum: TrickMomentum
    one_wall: TrickOneWall
    reverse_kick: TrickReverseKick
    sunsetter_abuse: TrickSunsetterAbuse

    shuffle_goatlings: ShuffleGoatlings
    shuffle_notes: ShuffleNotes
    shuffle_chairs: ShuffleChairs

    spawn: StartSpawns
