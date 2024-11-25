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
    """
    Disabled means doesnt expect anything, its just there as a placeholder so you can select something othere than an actual difficutly
    Normal means you can do it somewhat easily after just being told about it essentialy first 3-5 tries with no prior experience with it
    Advanced means its not new to you, the application has easy retries or isnt neccassairly hard, would need 10 or more tries if you had no previous experience in the trick category
    Expert means you know what youre doing with the trick and the application of it might be harder to do or harder to retry/easier to die attempting it
    Insane is a  catch all for everything above that and essentially means that the trick is second nature to you and you can do expert and below more or less first try with little to no difficulty
    """
    option_disabled = 0
    option_normal = 1
    option_advanced = 2
    option_expert = 3
    option_insane = 4
    default = 1


class TrickClingAbuse(UpstreamTrick):
    __doc__ = UpstreamTrick.__doc__ + """
    ClingAbuse is climbing corners with cling"""
    display_name = "Cling Abuse"


class TrickKnowledge(UpstreamTrick):
    __doc__ = UpstreamTrick.__doc__ + """
    Knowledge is things like activating levers /breaking walls with sunsetter, essentially anything that isnt obvious that you can do but that you can do."""
    display_name = "Knowledge"


class TrickMovement(UpstreamTrick):
    __doc__ = UpstreamTrick.__doc__ + """
    Movement is general movement such as standing backflips or jumping around a tight corner"""
    display_name = "Movement"


class TrickMomentum(UpstreamTrick):
    __doc__ = UpstreamTrick.__doc__ + """
    Momentum conservation is things like using cling and jumping of a pillar to get a backflip (see empty bailey bridge to ruins)"""
    display_name = "Momentum"


class TrickOneWall(UpstreamTrick):
    __doc__ = UpstreamTrick.__doc__ + """
    OneWall is just wall kicking up a single wall without a corner or another wall"""
    display_name = "One Wall"


class TrickReverseKick(UpstreamTrick):
    __doc__ = UpstreamTrick.__doc__ + """
    ReverseKick is a reverse wall kick"""
    display_name = "Reverse Kick"


class TrickSunsetterAbuse(UpstreamTrick):
    __doc__ = UpstreamTrick.__doc__ + """
    Sunsetter abuse is abusing the sunsetter backflip since it can be kinda floaty (see the bridge again, you can cross it with only sunsetter)"""
    display_name = "SunsetterAbuse"

class TrickPogoAbuse(UpstreamTrick):
    # currently unused?
    __doc__ = UpstreamTrick.__doc__ + """
    PogoAbuse is using ascendent light in ways vanilla doesnt "expect"
    """
    display_name = "PogoAbuse"

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
