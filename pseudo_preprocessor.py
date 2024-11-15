import json
from typing import Optional, Any, NamedTuple, List, Tuple, Dict
from collections import Counter

checks_file = """
use super::*;

use Ability as A;
use Location as L;
use Lock::{All, Any, Movement as Powerup, Location as Loc, Trick};
// for some reason doesn't import properly as just Trick
use super::Trick as T;
use Difficulty as D;

pub const CHECKS: [Check; 92] = [
    Check {
        description: "the goatling who fell out his cage",
        location: L::EarlyPrison,
        index: 433,
        drop: Drop::Goatling(&[
            "Oh[3rr](...)sorry, I didn't mean to[3rr](...)fall out of my cage[3rr](...)",
            "I hope[3rr](...)the [#cf2525](princess) won't be upset with me[3rr](...)"
        ]),
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "the time trial in the starting room",
        location: L::EarlyPrison,
        index: 503,
        drop: Drop::Ability(A::SolSister),
        trial: Some(486),
        // not final logic
        locks: All(&[Powerup(A::DreamBreaker), Powerup(A::SolarWind), Powerup(A::SunGreaves), Powerup(A::ClingGem(6)), Powerup(A::Sunsetter)]),
    },
    Check {
        description: "where dream breaker normally is",
        location: L::EarlyPrison,
        index: 501,
        drop: Drop::Ability(A::DreamBreaker),
        trial: None,
        locks: Any(&[
            Powerup(A::DreamBreaker), 
            All(&[
                Powerup(A::SunGreaves),
                Trick(T::Movement, D::Expert),
                Trick(T::OneWall, D::Advanced),
            ]),
            All(&[
                Powerup(A::SunGreaves),
                Powerup(A::SolarWind),
                Trick(T::Movement, D::Advanced),
                Trick(T::OneWall, D::Advanced),
            ]),
            All(&[
                Powerup(A::Sunsetter),
                Trick(T::Knowledge, D::Expert), // This wall sucks
            ]),
        ]),
    },
    Check {
        description: "where the first health piece is",
        location: L::EarlyPrison,
        index: 283,
        drop: Drop::Health,
        trial: None,
        locks: Any(&[
            Any(&[
                Powerup(A::Sunsetter),
                Powerup(A::AscendantLight),
                // just enough space to do this
                All(&[Powerup(A::SolarWind), Trick(T::Movement, D::Normal)]),
                All(&[Powerup(A::ClingGem(4)), Trick(T::ClingAbuse, D::Normal)]),
                Powerup(A::HeliacalPower),
            ]),
            // you can drop down from the entrance
            Loc(Location::CsMain),
        ]),
    },
    Check {
        description: "where slide normally is",
        location: L::LatePrison,
        index: 502,
        drop: Drop::Ability(A::Slide),
        trial: None,
        locks: Any(&[
            Powerup(A::Slide),
            Powerup(A::SunGreaves),
            All(&[Powerup(A::Sunsetter), Powerup(A::HeliacalPower)]),
            Powerup(A::ClingGem(2)),
            All(&[Powerup(A::HeliacalPower), Trick(T::Movement, D::Advanced)]),
            All(&[Powerup(A::Sunsetter), Trick(T::Movement, D::Advanced)]),
        ]),
    },
    Check {
        description: "black hole parkour off the beaten path",
        location: L::LatePrison,
        index: 504,
        drop: Drop::Ability(A::GoodGraces),
        trial: None,
        locks: Any(&[
            Powerup(A::ClingGem(6)),
            All(&[Powerup(A::AscendantLight), Powerup(A::SunGreaves)]),
            All(&[Powerup(A::SunGreaves), Powerup(A::SolarWind), Trick(T::Movement, D::Advanced), Trick(T::OneWall, D::Advanced)]),
        ]),
    },
    Check {
        description: "up in the rafters",
        location: L::StrongEyes,
        index: 255,
        drop: Drop::SmallKey,
        trial: None,
        locks: Any(&[
            All(&[
                Powerup(A::SunGreaves),
                Any(&[
                    Powerup(A::Sunsetter),
                    Powerup(A::SolarWind)
                ]),
            ]),
            All(&[Powerup(A::ClingGem(4)), Trick(T::ClingAbuse, D::Advanced)]),
        ]),
    },
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
    Check {
        description: "strong eyes' lair",
        location: L::StrongEyes,
        index: 254,
        drop: Drop::SmallKey,
        trial: None,
        locks: Powerup(A::DreamBreaker), // not changing, fighting without DB sucks
    },
    Check {
        description: "the goatling lamenting the skill issue of players who need a map",
        location: L::CsMain,
        index: 820,
        drop: Drop::Goatling(&["So many of have been trapped in the dungeon, and for what?"]),
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "where memento normally is",
        location: L::CsMain,
        index: 998,
        drop: Drop::Ability(A::Memento),
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "the goatling who wants to lick the checkpoint",
        location: L::CsMain,
        index: 817,
        drop: Drop::Goatling(&[
            "These [#7c79e8](crystals) are pretty nice, right?",
            "They make me feel safe...",
            "I think i'm gonna lick it. I bet it's full of [#8ada1c, buoy, italics](minerals).",
        ]),
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "a chair next to the goatling who wants to lick the checkpoint",
        location: L::CsMain,
        index: 822,
        drop: Drop::Chair,
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "a chair next to the goatling who wants to lick the checkpoint",
        location: L::CsMain,
        index: 823,
        drop: Drop::Chair,
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "a chair next to the goatling who wants to lick the checkpoint",
        location: L::CsMain,
        index: 824,
        drop: Drop::Chair,
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "where indignation normally is",
        location: L::CsMain,
        index: 994,
        drop: Drop::Ability(A::Indignation),
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "chillin' on a ledge by the window",
        location: L::CsMain,
        index: 540,
        drop: Drop::SmallKey,
        trial: None,
        locks: Any(&[
            Powerup(A::Sunsetter),
            All(&[Powerup(A::HeliacalPower), Trick(T::Movement, D::Advanced)]),
            All(&[Powerup(A::ClingGem(2)), Trick(T::ClingAbuse, D::Normal)]),
            Powerup(A::SolarWind),
        ]),
    },
    Check {
        description: "the goatling who wanted to see the armour display",
        location: L::CsMain,
        index: 821,
        drop: Drop::Goatling(&[
            "There was supposed to be a [#ffdb6b](new armor display) in the [#cf2525](library) I wanted to see.",
            "But with the state of the castle,  I can't find the entrance anywhere!",
            "I miss that [#ba7f27](comfy hay)..."
        ]),
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "the time trial behind a locked door",
        location: L::CsMain,
        index: 999,
        drop: Drop::Ability(A::Professional),
        trial: Some(969),
        locks: Lock::SmallKey, // You can easily do this with nothing but ability to hit the crystal.
    },
    Check {
        description: "tucked deep in a corner in the bouncer room",
        location: L::CsMain,
        index: 592,
        drop: Drop::Health,
        trial: None,
        locks: Any(&[
            Powerup(A::ClingGem(6)),
            All(&[Powerup(A::SunGreaves), Powerup(A::HeliacalPower), Trick(T::Movement, D::Advanced)]),
        ]),
    },
    Check {
        description: "the extremely slappable wheel guy room",
        location: L::CsMain,
        index: 591,
        drop: Drop::Health,
        trial: None,
        locks: Any(&[
            Powerup(A::AscendantLight),
            All(&[Powerup(A::SunGreaves), Trick(T::OneWall, D::Normal)]),
            Powerup(A::ClingGem(2)),
        ]),
    },
    Check {
        description: "the old softlock room",
        location: L::CsOldSoftlockRoom,
        index: 595,
        drop: Drop::Health,
        trial: None,
        locks: Any(&[
            All(&[Powerup(A::ClingGem(6)), Trick(T::ClingAbuse, D::Expert), Trick(T::Movement, D::Advanced)]),
            All(&[Powerup(A::SolarWind), Powerup(A::SunGreaves), Powerup(A::HeliacalPower), Powerup(A::AscendantLight)]), // Intended way
            All(&[Powerup(A::SolarWind), Powerup(A::HeliacalPower), Trick(T::Movement, D::Advanced)]),
            All(&[Powerup(A::SunGreaves), Powerup(A::Sunsetter), Trick(T::OneWall, D::Advanced), Trick(T::SunsetterAbuse, D::Advanced)])
        ]),
    },
    Check {
        description: "the goatling about to jump into the haze",
        location: L::CsOldSoftlockRoom,
        index: 819,
        drop: Drop::Goatling(&[
            "Oh, thanks for breaking that wall down.",
            "Thought I was gonna have to jump into the haze..."
        ]),
        trial: None,
        locks: Any(&[ // Just need to break the wall.. nothing new
            Powerup(A::DreamBreaker),
            All(&[
                Powerup(A::Sunsetter),
                Trick(T::Knowledge, D::Normal),
            ])
        ]),
    },
    Check {
        description: "cool moon room",
        location: L::CsTheatreEntrance,
        index: 997,
        drop: Drop::Ability(A::ClearMind),
        trial: None,
        locks: Any(&[ // Cross gap then climb the room
            All(&[Powerup(A::ClingGem(6)), Trick(T::ClingAbuse, D::Normal)]),
            All(&[Powerup(A::SolarWind), Powerup(A::SunGreaves), Powerup(A::HeliacalPower), Trick(T::Movement, D::Advanced)]),
            All(&[Powerup(A::Sunsetter), Powerup(A::ClingGem(4)), Trick(T::ClingAbuse, D::Normal)]),
            All(&[Powerup(A::Sunsetter), Powerup(A::SunGreaves), Powerup(A::ClingGem(2))]),
            All(&[Powerup(A::SolarWind), Powerup(A::ClingGem(2)), Powerup(A::SunGreaves)]),
        ]),
    },
    Check {
        description: "through the wallkick tunnel",
        location: L::CsMain,
        index: 539,
        drop: Drop::SmallKey,
        trial: None,
        locks: All(&[
            Any(&[// Activate the switch OR skip it
                Powerup(A::DreamBreaker),
                All(&[Powerup(A::Sunsetter), Trick(T::Knowledge, D::Normal)]),
                All(&[
                    Powerup(A::SunGreaves),
                    Powerup(A::HeliacalPower),
                    Trick(T::OneWall, D::Normal),
                ]),
                All(&[
                    Powerup(A::SolarWind),
                    Powerup(A::HeliacalPower),
                    Trick(T::Movement, D::Normal)
                ]),
                All(&[
                    Powerup(A::SolarWind),
                    Trick(T::Movement, D::Advanced)
                ]),
            ]),
            Any(&[ // Getting here is not an issue really.
                Powerup(A::SunGreaves), Powerup(A::ClingGem(6)),
                All(&[
                    Powerup(A::SunGreaves),
                    Powerup(A::SolarWind),
                    Trick(T::Movement, D::Normal),
                    Trick(T::OneWall, D::Normal),
                ]),
                All(&[
                    Powerup(A::ClingGem(2)),
                    Powerup(A::SolarWind)
                ]),
                All(&[
                    Powerup(A::ClingGem(2)),
                    Powerup(A::SunGreaves)
                ]),
                All(&[
                    Powerup(A::ClingGem(2)),
                    Powerup(A::HeliacalPower),
                    Trick(T::Movement, D::Advanced),
                    Trick(T::OneWall, D::Normal),

                ])
            ]),
        ]),
    },
    Check {
        description: "in the pit next to the dungeon entrance",
        location: L::CsTheatreEntryNearPrison, // Change Node so that we can infer the logic for getting to said node
        index: 594,
        drop: Drop::Health,
        trial: None,
        locks: Any(&[
            Powerup(A::ClingGem(4)),
            Powerup(A::HeliacalPower),
        ]),
    },
    Check {
        description: "the goatling that calls you bubble girl",
        location: L::CsTheatreEntryNearPrison, // Same as above, lower logic requirements that way
        index: 816,
        drop: Drop::Goatling(&[
            "I was supposed to go help in the [#cf2525](theatre), but I can't really get through here.",
            "I just don't really wanna touch the [#cf2525](bubbles)...",
            "What? I dont have a problem. You go touch 'em then, bubble girl."
        ]),
        trial: None,
        locks: Any(&[
            Powerup(A::HeliacalPower),
            Powerup(A::ClingGem(4)),
        ]),
    },
    Check {
        description: "on the ledge above the bailey entrance",
        location: L::CsMain,
        index: 593,
        drop: Drop::Health,
        trial: None,
        locks: Any(&[ // Not much to add here really
            All(&[Powerup(A::SunGreaves), Powerup(A::HeliacalPower), Trick(T::Movement, D::Normal)]),
            Powerup(A::ClingGem(4)),
            All(&[Powerup(A::SolarWind), Powerup(A::HeliacalPower)]),
        ]),
    },
    Check {
        description: "the goatling in the gazebo",
        location: L::CsMain,
        index: 818,
        drop: Drop::Goatling(&[
            "The princess used to love having afternoon tea here.",
            "But the handmaiden has run out of her special ingredient.",
            "I guess the princess doesn't really want anybody else's tea...",
        ]),
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "the chair in the gazebo",
        location: L::CsMain,
        index: 825,
        drop: Drop::Chair,
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "next to a bouncer in the massive room",
        location: L::CsMain,
        index: 995,
        drop: Drop::Ability(A::Pilgrimage),
        trial: None,
        locks: Any(&[
            All(&[
                Powerup(A::AscendantLight),
                Trick(T::Movement, D::Normal),
                Any(&[
                    Powerup(A::SunGreaves),
                    Powerup(A::SolarWind),
                ]),
            ]),
            All(&[Powerup(A::SunGreaves), Powerup(A::HeliacalPower), Trick(T::OneWall, D::Advanced)]),
            All(&[
                Powerup(A::ClingGem(6)), 
                Any(&[
                    Powerup(A::HeliacalPower),
                    Powerup(A::Sunsetter),
                    Powerup(A::SolarWind),
                    Powerup(A::AscendantLight),
                ]),
            ]),
        ]),
    },
    Check {
        description: "in the room with two other ones to each side",
        location: L::CsMain,
        index: 996,
        drop: Drop::Ability(A::GoodGraces),
        trial: None,
        locks: Any(&[
            All(&[
                Powerup(A::ClingGem(6)),
                Any(&[
                    Powerup(A::Sunsetter),
                    Powerup(A::HeliacalPower),
                    Trick(T::ClingAbuse, D::Normal),
                ]),
            ]),
            Powerup(A::SunGreaves),
            All(&[Powerup(A::HeliacalPower), Trick(T::Movement, D::Advanced)]),
            All(&[Powerup(A::SolarWind), Trick(T::Movement, D::Normal)]),
        ]),
    },
    // Listless Library
    Check {
        description: "the chair at the entrance",
        location: L::MainLibrary,
        index: 289,
        drop: Drop::Chair,
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "the time trial amidst the books",
        location: L::MainLibrary,
        index: 325,
        drop: Drop::Ability(A::Sleepytime),
        // not final logic
        trial: Some(314),
        locks: All(&[
            Any(&[
                Powerup(A::DreamBreaker),
                All(&[
                    Powerup(A::Sunsetter),
                    Trick(T::Knowledge, D::Normal)
                ])
            ]),
            Any(&[
                All(&[Powerup(A::Sunsetter), Trick(T::Movement, D::Advanced)]),
                All(&[Powerup(A::SunGreaves), Trick(T::Movement, D::Normal)]),
                All(&[Powerup(A::SolarWind), Trick(T::Movement,D::Normal)]),
                All(&[Powerup(A::ClingGem(6)), Trick(T::Movement, D::Advanced), Trick(T::ClingAbuse, D::Normal)]),
                All(&[Powerup(A::Sunsetter), Powerup(A::HeliacalPower), Powerup(A::SolarWind)]),
            ]),
        ]),
    },
    Check {
        description: "where sun greaves normally is",
        location: L::LibSaveNearGreaves,
        index: 324,
        drop: Drop::Ability(A::SunGreaves),
        trial: None,
        locks: Any(&[
            Powerup(A::DreamBreaker),
            All(&[Trick(T::Knowledge, D::Advanced), Powerup(A::Sunsetter)]),
        ]),
    },
    Check {
        description: "the chair after the normal sun greaves location",
        location: L::LibSaveNearGreaves,
        index: 291,
        drop: Drop::Chair,
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "the note next to the egg nest",
        location: L::MainLibrary,
        index: 288,
        drop: Drop::Note,
        trial: None,
        locks: Any(&[
            Powerup(A::SunGreaves),
            Powerup(A::ClingGem(4)),
            Powerup(A::SolarWind),
        ]),
    },
    Check {
        description: "the chair next to the egg nest",
        location: L::MainLibrary,
        index: 290,
        drop: Drop::Chair,
        trial: None,
        locks: Any(&[
            Powerup(A::SunGreaves),
            Powerup(A::ClingGem(4)),
            Powerup(A::SolarWind),
        ]),
    },
    Check {
        description: "in the buttress room",
        location: L::MainLibrary,
        index: 237,
        drop: Drop::Health,
        trial: None,
        locks: Any(&[Powerup(A::SunGreaves), Powerup(A::ClingGem(4))]),
    },
    Check {
        description: "in the hay behind the locked door",
        location: L::Restricted,
        index: 326,
        drop: Drop::Ability(A::ClearMind),
        trial: None,
        locks: Any(&[
            Powerup(A::SolarWind),
            All(&[Powerup(A::HeliacalPower), Trick(T::Movement, D::Expert)]),
            Powerup(A::ClingGem(4)),
        ]),
    },
    Check {
        description: "tucked deep behind the locked door",
        location: L::Restricted,
        index: 238,
        drop: Drop::Health,
        trial: None,
        locks: Any(&[
            Powerup(A::SolarWind),
            All(&[Powerup(A::HeliacalPower), Trick(T::Movement, D::Expert)]),
            Powerup(A::ClingGem(4)),
        ]),
    },
    // Sansa Keep
    Check {
        description: "the goatling sad about the lack of furniture",
        location: L::SansaKeep,
        index: 475,
        drop: Drop::Goatling(&[
            "They took away all my furniture."
        ]),
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "the goatling collapsing out of reality",
        location: L::SkCastleRampEntry,
        index: 476,
        drop: Drop::Goatling(&[
            "[6rr](.....c.....y..u...i....y.......ce....)"
        ]),
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "the chair collapsing out of reality",
        location: L::SkCastleRampEntry,
        index: 477,
        drop: Drop::Chair,
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "where strikebreak normally is",
        location: L::SansaKeep,
        index: 565,
        drop: Drop::Ability(A::Strikebreak),
        trial: None,
        locks: All(&[
            Powerup(A::Strikebreak),
            Any(&[
                All(&[Powerup(A::HeliacalPower), Trick(T::Movement, D::Advanced)]), // Only at advanced bc of the forward backflip that is harder on controller.
                Powerup(A::ClingGem(4)),
                Powerup(A::SolarWind),
            ]),
        ]),
    },
    Check {
        description: "where sunsetter normally is",
        location: L::Sunsetter,
        index: 564,
        drop: Drop::Ability(A::Sunsetter),
        trial: None,
        locks: All(&[
            Powerup(A::DreamBreaker),
            Any(&[
                Powerup(A::Sunsetter),
                All(&[Powerup(A::HeliacalPower), Trick(T::Movement, D::Advanced)]), // Only at advanced bc of the forward backflip that is harder on controller.
                All(&[Powerup(A::ClingGem(2)), Trick(T::ClingAbuse, D::Normal)]),
            ]),
        ]),
    },
    Check {
        description: "in an alcove next to the locked door",
        location: L::Sunsetter,
        index: 330,
        drop: Drop::Health,
        trial: None,
        locks: Any(&[
            Powerup(A::Sunsetter),
            Powerup(A::SunGreaves),
            Powerup(A::SolarWind),
            Trick(T::Movement, D::Normal), // Can legit get this sphere 0 with nothing.
        ]),
    },
    Check {
        description: "in the room with a lever on each side",
        location: L::SansaKeep,
        index: 304,
        drop: Drop::SmallKey,
        trial: None,
        locks: Any(&[
            All(&[Powerup(A::Sunsetter), Trick(T::Knowledge, D::Normal)]),
            Powerup(A::DreamBreaker),
        ]),
    },
    Check {
        description: "tucked near the theatre entrance",
        location: L::SansaKeep,
        index: 566,
        drop: Drop::Ability(A::ClearMind),
        trial: None,
        locks: Any(&[
            Powerup(A::Sunsetter),
            Powerup(A::HeliacalPower),
            Powerup(A::ClingGem(4)),
        ]),
    },
    Check {
        description: "at the end of the parkour",
        location: L::SansaKeep,
        index: 305,
        drop: Drop::BigKey(4),
        trial: None,
        locks: Any(&[
            All(&[
                Powerup(A::AscendantLight),
                Any(&[
                    All(&[
                        Powerup(A::ClingGem(4)),
                        Any(&[Powerup(A::Sunsetter), Powerup(A::SunGreaves)]),
                    ]),
                    All(&[Powerup(A::Sunsetter), Powerup(A::SunGreaves)]),
                ]),
            ]),
            All(&[
                Powerup(A::DreamBreaker),
                Powerup(A::Slide),
                Powerup(A::SolarWind),
                Powerup(A::Sunsetter),
                Powerup(A::ClingGem(2)),
                Powerup(A::SunGreaves),
            ]),
        ]),
    },
    Check {
        description: "the time trial at the end of the parkour",
        location: L::SansaKeep,
        index: 567,
        drop: Drop::Ability(A::Guardian),
        // only logic to get here not final
        trial: Some(541),
        locks: All(&[Powerup(A::DreamBreaker), Powerup(A::SolarWind), Powerup(A::SunGreaves), Powerup(A::ClingGem(6)), Powerup(A::Sunsetter), Powerup(A::AscendantLight)]),
    },
    Check {
        description: "the chair in the middle of the parkour",
        location: L::SansaKeep,
        index: 478,
        drop: Drop::Chair,
        trial: None,
        locks: Any(&[
            All(&[
                Powerup(A::AscendantLight),
                Any(&[
                    All(&[
                        Powerup(A::ClingGem(4)),
                        Any(&[Powerup(A::Sunsetter), Powerup(A::SunGreaves)]),
                    ]),
                    All(&[Powerup(A::Sunsetter), Powerup(A::SunGreaves)]),
                ]),
            ]),
            All(&[
                Powerup(A::DreamBreaker),
                Powerup(A::Slide),
                Powerup(A::SolarWind),
                Powerup(A::Sunsetter),
                Powerup(A::ClingGem(2)),
                Powerup(A::SunGreaves),
            ]),
        ]),
    },
    // Empty Bailey
    Check {
        description: "the goatling who's hiding",
        location: L::EmptyBailey,
        index: 115,
        drop: Drop::Goatling(&["...i'm not here."]),
        trial: None,
        locks: Powerup(A::Slide), // Theres another way to get TO the item, not putting it in since its a one way unless it is slide though...
    },
    Check {
        description: "in the building you slide into",
        location: L::EmptyBailey,
        index: 70,
        drop: Drop::SmallKey,
        trial: None,
        locks: Powerup(A::Slide),
    },
    Check {
        description: "guarded by the hand and soldier",
        location: L::EmptyBailey,
        index: 69,
        drop: Drop::BigKey(1),
        trial: None,
        locks: Any(&[
            Powerup(A::Sunsetter),
            Powerup(A::SunGreaves),
            Powerup(A::ClingGem(4)),
            Powerup(A::SolarWind),
            All(&[
                Loc(L::EbEntryUnderBelly),
                Trick(T::Movement, D::Advanced), // Can just jump to it from above.
            ]),
        ]),
    },
    Check {
        description: "where solar wind normally is",
        location: L::EmptyBailey,
        index: 148,
        drop: Drop::Ability(A::SolarWind),
        trial: None,
        locks: All(&[
            Powerup(A::Slide),
            Any(&[
                Powerup(A::DreamBreaker),
                All(&[
                    Powerup(A::Sunsetter),
                    Trick(T::Knowledge, D::Normal),
                ])
            ]),
            Any(&[
                Powerup(A::SolarWind),
                All(&[Powerup(A::HeliacalPower), Trick(T::Movement, D::Advanced)]),
            ]),
        ]),
    },
    Check {
        description: "in the tower in the middle",
        location: L::EmptyBailey,
        index: 80,
        drop: Drop::Health,
        trial: None,
        locks: Any(&[
            Powerup(A::Sunsetter),
            All(&[Powerup(A::HeliacalPower), Trick(T::ReverseKick, D::Advanced)]),
            All(&[Powerup(A::SunGreaves), Trick(T::OneWall, D::Normal)]),
            // you can jump down from cheese bell
            All(&[
                Powerup(A::SolarWind), 
                Any(&[
                    Powerup(A::ClingGem(6)),
                    All(&[Powerup(A::Sunsetter), Powerup(A::HeliacalPower), Trick(T::Movement, D::Advanced)]),
                    All(&[Trick(T::Movement, D::Advanced),Powerup(A::Sunsetter), Powerup(A::SunGreaves)]),
                    All(&[Powerup(A::ClingGem(4)), Powerup(A::Sunsetter), Powerup(A::SunGreaves)]),
                ]),
            ]),
        ]),
    },
    Check {
        description: "under the cheese bell",
        location: L::EmptyBailey,
        index: 149,
        drop: Drop::Ability(A::Empathy),
        trial: None,
        locks: Any(&[
            All(&[
                Powerup(A::SolarWind),
                Any(&[
                    Powerup(A::ClingGem(6)),
                    All(&[Powerup(A::Sunsetter), Powerup(A::HeliacalPower), Trick(T::Movement, D::Advanced)]),
                ]),
            ]),
            All(&[Trick(T::Movement, D::Advanced),Powerup(A::Sunsetter), Powerup(A::SunGreaves)]),
            All(&[Powerup(A::ClingGem(4)), Powerup(A::Sunsetter), Powerup(A::SunGreaves)]),
        ]),
    },
    Check {
        description: "the locked up time trial",
        location: L::EmptyBailey,
        index: 150,
        drop: Drop::Ability(A::Soldier),
        trial: Some(128),
        locks: All(&[Powerup(A::DreamBreaker), Powerup(A::SolarWind), Powerup(A::SunGreaves), Powerup(A::ClingGem(6)), Powerup(A::Sunsetter)]),
    },
    // Underbelly
    Check {
        description: "near the entrance from sansa keep",
        location: L::SansaHole,
        index: 614,
        drop: Drop::Health,
        trial: None,
        locks: Any(&[
            Powerup(A::SunGreaves),
            All(&[Powerup(A::Sunsetter), Powerup(A::HeliacalPower)]),
        ]),
    },
    Check {
        description: "the soul cutter lever room",
        location: L::SansaHole,
        index: 545,
        drop: Drop::BigKey(2),
        trial: None,
        locks: All(&[
            Powerup(A::DreamBreaker),
            Powerup(A::Sunsetter),
            Any(&[
                All(&[
                    Powerup(A::SoulCutter),
                    Any(&[Powerup(A::AscendantLight), Powerup(A::ClingGem(6))]),
                ]),
                All(&[Powerup(A::SunGreaves), Powerup(A::SolarWind)]),
            ]),
        ]),
    },
    Check {
        description: "where ascendant light normally is",
        location: L::VAscendantLight,
        index: 1044,
        drop: Drop::Ability(A::AscendantLight),
        // you can go through the dark area and there's a passage which you can do with nothing
        trial: None,
        locks: Any(&[
            Powerup(A::DreamBreaker),
            All(&[
                Powerup(A::Sunsetter),
                Trick(T::Knowledge, D::Expert), // this is at expert bc of fighting the statue...
            ])
        ]),
    },
    Check {
        description: "in an alcove behind some pillars",
        location: L::VAscendantLight,
        index: 616,
        drop: Drop::Health,
        trial: None,
        locks: Any(&[
            All(&[Powerup(A::Sunsetter), Trick(T::Knowledge, D::Normal)]), // normal route into AL 
            Powerup(A::DreamBreaker)
        ]),
    },
    Check {
        description: "on a missable ledge in the centre",
        location: L::MainUnderbelly,
        index: 546,
        drop: Drop::SmallKey,
        trial: None,
        locks: Any(&[ // Leaving as is for now.
            Powerup(A::Sunsetter),
            Powerup(A::SolarWind),
        ]),
    },
    Check {
        description: "the note on a high ledge in the big room",
        location: L::MainUnderbelly,
        index: 894,
        drop: Drop::Note,
        trial: None,
        locks: All(&[ // Leaving as is for now.
            Powerup(A::HeliacalPower),
            Powerup(A::Sunsetter),
            Any(&[
                Powerup(A::ClingGem(6)),
                Powerup(A::SunGreaves),
                Powerup(A::SolarWind),
            ]),
        ]),
    },
    Check {
        description: "black hole parkour behind strikebreak wall",
        location: L::MainUnderbelly,
        index: 1046,
        drop: Drop::Ability(A::MartialProwess),
        trial: None,
        locks: All(&[// Leaving this one out of tricks for now since theres a ton of ways to do it
            Powerup(A::Strikebreak), // Dont know why this one was SoulCutter before...
            Powerup(A::AscendantLight),
            Any(&[
                Powerup(A::HeliacalPower),
                Powerup(A::Sunsetter),
                Powerup(A::SolarWind),
                Powerup(A::ClingGem(2)),
            ]),
        ]),
    },
    Check {
        description: "the locked up time trial",
        location: L::MainUnderbelly,
        index: 1045,
        drop: Drop::Ability(A::Xix),
        // need to hit lever at top first
        trial: Some(1028),
        locks: All(&[Powerup(A::DreamBreaker), Powerup(A::SolarWind), Powerup(A::SunGreaves), Powerup(A::ClingGem(6)), Powerup(A::Sunsetter)]),
    },
    Check {
        description: "behind the locked door",
        location: L::HpSave,
        index: 1047,
        drop: Drop::Ability(A::HeliacalPower),
        trial: None,
        locks: Lock::SmallKey,
    },
    Check {
        description: "the note behind the locked door",
        location: L::HpSave,
        index: 895,
        drop: Drop::Note,
        trial: None,
        locks: Lock::SmallKey,
    },
    Check {
        description: "the note near the empty bailey entrance",
        location: L::BaileyHole,
        index: 896,
        drop: Drop::Note,
        trial: None,
        locks: Any(&[
            Powerup(A::SunGreaves),
            All(&[Powerup(A::HeliacalPower), Powerup(A::Sunsetter)]),
            Powerup(A::ClingGem(6)),
            Powerup(A::AscendantLight),
            Powerup(A::SolarWind),
            All(&[Powerup(A::HeliacalPower), Trick(T::ReverseKick, D::Normal)]),
            All(&[Powerup(A::Sunsetter), Trick(T::Movement, D::Normal)]),
        ]),
    },
    Check {
        description: "on top of the big building",
        location: L::BaileyHole,
        index: 615,
        drop: Drop::Health,
        trial: None,
        locks: Any(&[
            Powerup(A::SunGreaves),
            Powerup(A::Sunsetter),
            Powerup(A::SolarWind),
        ]),
    },
    // Tower Ruins
    Check {
        description: "where cling gem normally is",
        location: L::TowerRuinsKeep,
        index: 155,
        drop: Drop::Ability(A::ClingGem(6)),
        trial: None,
        locks: Any(&[
            Powerup(A::ClingGem(6)),
            Powerup(A::SunGreaves),
            All(&[Powerup(A::HeliacalPower), Powerup(A::Sunsetter), Trick(T::Movement, D::Normal)]),
        ]),
    },
    Check {
        description: "atop the tower",
        location: L::TowerRuinsKeep,
        index: 77,
        drop: Drop::BigKey(3),
        trial: None,
        locks: Any(&[
            All(&[
                Powerup(A::ClingGem(2)),
                Any(&[
                    Powerup(A::SunGreaves),
                    All(&[
                        Powerup(A::HeliacalPower),
                        Powerup(A::Sunsetter),
                    ]),
                ]),
            ]),
            All(&[
                Powerup(A::SunGreaves),
                Powerup(A::SolarWind),
                Trick(T::Movement, D::Expert),
                Trick(T::OneWall, D::Advanced),
            ])
        ]),
    },
    Check {
        description: "the time trial at the tower entrance",
        location: L::TowerRuinsKeep,
        index: 156,
        drop: Drop::Ability(A::BleedingHeart),
        // again again just to get to top of tower
        // need to hit lever tho
        trial: Some(129),
        locks: All(&[Powerup(A::DreamBreaker), Powerup(A::SolarWind), Powerup(A::SunGreaves), Powerup(A::ClingGem(6)), Powerup(A::Sunsetter)]),
    },
    // Twilight Theatre
    Check {
        description: "on a beam in the corner",
        location: L::PillarRoom,
        index: 1231,
        drop: Drop::Ability(A::AerialFinesse),
        trial: None,
        locks: Any(&[
            All(&[
              Powerup(A::SunGreaves),
              Any(&[Powerup(A::ClingGem(2)), Powerup(A::SolarWind), Powerup(A::Sunsetter)])
            ]),
            All(&[Powerup(A::SolarWind), Powerup(A::ClingGem(2))]),
            All(&[Powerup(A::Sunsetter), Powerup(A::SunGreaves), Trick(T::SunsetterAbuse, D::Normal), Trick(T::Movement, D::Advanced), Trick(T::OneWall, D::Normal)]),
        ]),
    },
    Check {
        description: "the locked up time trial",
        location: L::PillarRoom,
        index: 1232,
        drop: Drop::Ability(A::Classy),
        // need to hit the lever first
        trial: Some(1211),
        locks: All(&[Powerup(A::DreamBreaker), Powerup(A::SolarWind), Powerup(A::SunGreaves), Powerup(A::ClingGem(6)), Powerup(A::Sunsetter)]),
    },
    Check {
        description: "a chair around the table",
        location: L::OtherTheatrePath,
        index: 1081,
        drop: Drop::Chair,
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "a chair around the table",
        location: L::OtherTheatrePath,
        index: 1084,
        drop: Drop::Chair,
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "a chair around the table",
        location: L::OtherTheatrePath,
        index: 1085,
        drop: Drop::Chair,
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "the chair next to the books",
        location: L::OtherTheatrePath,
        index: 1086,
        drop: Drop::Chair,
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "the goatling who can eat 20 beans at least",
        location: L::TheatreEntrance,
        index: 1072,
        drop: Drop::Goatling(&[
            "where have [#cf2525](you been)?",
            "three bean casserole? not enough for 1 man. i can eat like, [#cf2525](20 beans), at least.",
            "so get to it. [up, 10rr](please?)"
        ]),
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "the goatling who thought the theatre was safe",
        location: L::TheatreEntrance,
        index: 1074,
        drop: Drop::Goatling(&[
            "I heard that the theatre was still in good condition...",
            "But it seems even this place has been affected."
        ]),
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "the goatling who really wanted to see the show",
        location: L::TheatreEntrance,
        index: 1079,
        drop: Drop::Goatling(&[
            "Ah nuts....I really wanted to see the show today."
        ]),
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "the goatling who really wanted to see the show",
        location: L::TheatreEntrance,
        index: 1080,
        drop: Drop::Goatling(&[
            "Sorry miss, can't let you in.",
            "Theatre's closed until all the haze is gone."
        ]),
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "hiding amid the boxes",
        location: L::MainTheatre,
        index: 912,
        drop: Drop::Health,
        trial: None,
        locks: Lock::None,
    },
    Check {
        description: "the goatling that will kill again",
        location: L::MainTheatre,
        index: 1071,
        drop: Drop::Goatling(&[
            "please leave me alone?",
            "i will [#cf2525](kill again)"
        ]),
        trial: None,
        locks: Any(&[
            All(&[Powerup(A::SolarWind), Powerup(A::HeliacalPower)]),
            Powerup(A::SunGreaves),
            Powerup(A::ClingGem(6))
        ]),
    },
    Check {
        description: "the chair near the courtyard",
        location: L::MainTheatre,
        index: 1082,
        drop: Drop::Chair,
        trial: None,
        locks: Any(&[
            Powerup(A::ClingGem(4)),
            All(&[Powerup(A::SolarWind), Powerup(A::HeliacalPower), Powerup(A::SunGreaves)]),
        ]),
    },
    Check {
        description: "the chair in the soul cutter zone",
        location: L::MainTheatre,
        index: 1083,
        drop: Drop::Chair,
        trial: None,
        locks: All(&[
            Powerup(A::Strikebreak), 
            Powerup(A::ClingGem(6)),
            Any(&[
                // Logic for soul cutter route w/o soulcutter
                All(&[
                    Powerup(A::Strikebreak),
                    Powerup(A::SolarWind),
                    Powerup(A::HeliacalPower),
                    Powerup(A::SunGreaves),
                    Powerup(A::Sunsetter),
                    Trick(T::ClingAbuse, D::Expert),
                    Trick(T::OneWall, D::Expert),
                    Trick(T::Movement, D::Insane),
                    Trick(T::Momentum, D::Expert),
                ]),
                //with soul cutter.
                All(&[
                    Powerup(A::SoulCutter),
                    Any(&[
                        Powerup(A::HeliacalPower),
                        Powerup(A::SolarWind)
                    ]),
                ]),
            ]),
        ]),
    },
    Check {
        description: "behind three maximum security cages",
        location: L::MainTheatre,
        index: 871,
        drop: Drop::BigKey(5),
        // there's one gap in the open green room with enemies which is too big
        trial: None,
        locks: All(&[
            Powerup(A::Strikebreak), 
            Powerup(A::ClingGem(6)),
            Any(&[
                // Logic for soul cutter route
                All(&[
                    Powerup(A::Strikebreak),
                    Powerup(A::SolarWind),
                    Powerup(A::HeliacalPower),
                    Powerup(A::SunGreaves),
                    Powerup(A::Sunsetter),
                    Trick(T::ClingAbuse, D::Expert),
                    Trick(T::OneWall, D::Expert),
                    Trick(T::Movement, D::Insane),
                    Trick(T::Momentum, D::Expert),
                ]),
                All(&[
                    Powerup(A::SoulCutter),
                    Any(&[
                        Powerup(A::HeliacalPower),
                        Powerup(A::SolarWind)
                    ]),
                ]),
            ]),
        ]),
    },
    Check {
        description: "where soul cutter normally is",
        location: L::MainTheatre,
        index: 1230,
        drop: Drop::Ability(A::SoulCutter),
        trial: None,
        locks: All(&[
            //Absolutely neccassary 
            Powerup(A::Strikebreak),
            
            Any(&[
                //Trick for leaving same way as came in.
                All(&[                    
                    Powerup(A::SolarWind),
                    Trick(T::Movement, D::Expert), // Go under the gate as it closes to drop back down. then use abilities to scale shafts.
                    Powerup(A::SunGreaves),
                    Powerup(A::HeliacalPower),
                    Powerup(A::ClingGem(6)),
                    Powerup(A::Sunsetter),
                    Trick(T::OneWall, D::Expert),
                    Trick(T::Knowledge, D::Advanced), // for going under gate from soulcutter and knowing not being locked and needing to climb.
                ]),
                // Go the soul cutter route out to lever without Soulcutter.
                All(&[
                    Powerup(A::Strikebreak),
                    Powerup(A::SolarWind),
                    Powerup(A::HeliacalPower),
                    Powerup(A::SunGreaves),
                    Powerup(A::Sunsetter),
                    Trick(T::ClingAbuse, D::Expert),
                    Trick(T::OneWall, D::Expert),
                    Trick(T::Movement, D::Insane),
                    Trick(T::Momentum, D::Expert),
                ]),
                // Go out the lever route WITH soul cutter.
                All(&[
                    Powerup(A::SoulCutter),
                    Any(&[
                        Powerup(A::HeliacalPower),
                        Powerup(A::SolarWind)
                    ]),
                ]),
            ]),
        ]),
    },
    Check {
        description: "in the back on a pillar",
        location: L::MainTheatre,
        index: 913,
        drop: Drop::Health,
        trial: None,
        locks: Any(&[Powerup(A::SunGreaves), Powerup(A::ClingGem(6))]),
    },
    Check {
        description: "behind the locked door",
        location: L::MainTheatre,
        index: 1233,
        drop: Drop::Ability(A::Empathy),
        trial: None,
        locks:  All(&[
            Lock::SmallKey,
            Any(&[
                Powerup(A::SunGreaves),
                Powerup(A::ClingGem(2)),
            ]),
        ]),
    },
];
"""

locations_file = """
use super::*;
/*
To-Do:
split areas further to ensure proper logic is available.
Add Nodes for each lever.
Re-name current nodes.
i.e. split Late prison into the save crystal's, In the rafters room, and after the underbelly wall.
*/
#[derive(Debug, Clone, Copy, PartialEq, strum::EnumIter, strum::EnumCount, strum::Display)]
pub enum Location {
    // Prison
    EarlyPrison,
    LatePrison,
    StrongEyes,
    PEntryCastle,
    PEntryUnderBelly,
    PEntryTheatre,
    // Castle
    CsOldSoftlockRoom,
    CsKeepClimbEntrance,
    CsMain,
    CsTheatreEntrance,
    CsPrisonEntry,
    CsLibraryEntry,
    CsTheatreEntryNearPrison,
    CsKeepEntryMain,
    CsKeepEntryRamp,
    CsBaileyEntry,
    // Library
    MainLibrary,
    Restricted,
    LibSaveNearGreaves,
    // Keep
    SkCastleRampEntry,
    SkCastleMainEntry,
    SkCastleClimbEntry,
    SkUnderbellyEntry,
    SkTheatreEntry,
    SansaKeep,
    Sunsetter,
    // Bailey
    EmptyBailey,
    EbEntryUnderBelly,
    EbEntryRuins,
    EbEntryTheatre,
    EbEntryCastle,
    // Ruins
    TowerRuinsEntrance,
    TowerRuinsKeep,
    // Underbelly
    SansaHole,
    BaileyHole,
    PrisonHole,
    MainUnderbelly,
    VAscendantLight,
    HpSave,
    // Theatre
    ThCastleEntryPillar,
    ThCastleEntryMain,
    ThBaileyEntry,
    ThKeepEntry,
    ThDungeonEntry,
    PillarRoom,
    TheatreEntrance,
    OtherTheatrePath,
    MainTheatre,
    // Final
    FinalBoss,
}

use tricks::Trick as T;
use Ability as A;
use Difficulty as D;
use Location as L;
use Lock::{All, Any, Location as Loc, Movement as Powerup, Trick};
impl Location {
    // need to include some reverse directions
    pub const fn locks(&self) -> Lock {
        match self {
            // Prison / Dilapidated Dungeon
            L::LatePrison => All(&[
                Any(&[
                    Powerup(A::DreamBreaker),
                    All(&[Trick(T::Knowledge, D::Normal), Powerup(A::Sunsetter)]),
                ]),
                Any(&[
                    Loc(L::CsMain),
                    Loc(L::PEntryUnderBelly),
                    Loc(L::EarlyPrison),
                ]),
            ]),
            L::EarlyPrison => All(&[
                Any(&[
                    Powerup(A::DreamBreaker),
                    All(&[Powerup(A::Sunsetter), Trick(T::Knowledge, D::Normal)]),
                ]),
                Any(&[
                    All(&[
                        Loc(L::StrongEyes),
                        Any(&[
                            Lock::SmallKey, // Open the door
                            All(&[
                                // Go through the little shortcut thing
                                Powerup(A::Sunsetter),
                                Powerup(A::DreamBreaker),
                                Trick(T::Knowledge, D::Normal),
                            ]),
                        ]),
                    ]), // From Strong Eyes
                    Loc(L::CsMain),     // Drop in from castle
                    Loc(L::LatePrison), // Breaking wall from late.
                ]),
            ]),
            L::PEntryUnderBelly => Any(&[
                All(&[
                    Loc(L::LatePrison),
                    Any(&[
                        Powerup(A::DreamBreaker),
                        All(&[
                            Powerup(A::Sunsetter),
                            Trick(T::Knowledge, D::Expert), // This wall also sucks lol
                        ]),
                    ]),
                ]),
                All(&[Loc(L::PrisonHole), Powerup(A::AscendantLight)]),
            ]),
            L::StrongEyes => Any(&[
                All(&[Loc(L::LatePrison), Powerup(A::Slide)]),
                All(&[
                    Loc(L::CsMain),
                    Any(&[
                        Lock::SmallKey, // Open the door
                        All(&[
                            // Go through the little shortcut thing
                            Powerup(A::Sunsetter),
                            Powerup(A::DreamBreaker),
                            Trick(T::Knowledge, D::Normal),
                        ]),
                    ]),
                ]),
            ]),
            L::PEntryCastle => Any(&[
                Loc(L::CsPrisonEntry),
                All(&[Loc(L::StrongEyes), Lock::SmallKey]),
                All(&[
                    Loc(L::EarlyPrison),
                    Powerup(A::SolarWind),
                    Powerup(A::SunGreaves),
                    Powerup(A::HeliacalPower),
                    Powerup(A::Sunsetter),
                    Powerup(A::ClingGem(6)),
                    Trick(T::ClingAbuse, D::Expert),
                    Trick(T::Movement, D::Expert),
                    Trick(T::Momentum, D::Advanced),
                ]),
            ]),
            L::PEntryTheatre => Any(&[
                Loc(L::ThDungeonEntry),
                All(&[
                    Loc(L::LatePrison),
                    Any(&[
                        Powerup(A::ClingGem(6)),
                        Powerup(A::SunGreaves),
                        Powerup(A::AscendantLight),
                    ]),
                ]),
            ]),
            // Castle Sansa
            L::CsPrisonEntry => Any(&[Loc(L::CsMain), Loc(L::PEntryCastle)]),
            L::CsLibraryEntry => Any(&[
                Loc(L::MainLibrary),
                All(&[Loc(L::CsMain), Powerup(A::DreamBreaker)]),
            ]),
            L::CsTheatreEntryNearPrison => Any(&[
                Loc(L::PillarRoom),
                All(&[
                    Loc(L::CsMain),
                    Any(&[
                        All(&[
                            Powerup(A::Slide),
                            Trick(T::Movement, D::Advanced),
                            Trick(T::Momentum, D::Advanced),
                        ]),
                        All(&[Powerup(A::Sunsetter), Powerup(A::SunGreaves)]),
                        All(&[Powerup(A::HeliacalPower), Powerup(A::SolarWind)]), // This is using the little block stair case thing to get up
                        All(&[Powerup(A::SunGreaves), Trick(T::Movement, D::Normal)]),
                        All(&[Powerup(A::Sunsetter), Trick(T::Movement, D::Advanced)]),
                        All(&[Powerup(A::ClingGem(4)), Trick(T::ClingAbuse, D::Normal)]),
                        All(&[
                            Powerup(A::Slide),
                            Powerup(A::SolarWind),
                            Trick(T::Movement, D::Normal),
                        ]),
                    ]),
                ]),
            ]),
            L::CsOldSoftlockRoom => Any(&[
                All(&[Loc(L::CsMain), Powerup(A::ClingGem(2))]),
                All(&[
                    Loc(L::CsTheatreEntrance),
                    Any(&[
                        All(&[
                            Powerup(A::SolarWind),
                            Powerup(A::HeliacalPower),
                            Trick(T::Movement, D::Normal),
                        ]),
                        All(&[
                            Powerup(A::Slide),
                            Powerup(A::ClingGem(2)),
                            Trick(T::Movement, D::Advanced),
                        ]),
                    ]),
                ]),
            ]),
            L::CsKeepClimbEntrance => All(&[Loc(L::CsMain), Lock::SmallKey]),
            L::CsKeepEntryMain => Any(&[Loc(L::CsMain), Loc(L::SansaKeep)]),
            L::CsKeepEntryRamp => Any(&[
                All(&[
                    Loc(L::CsMain),
                    Any(&[
                        Powerup(A::DreamBreaker),
                        Trick(T::Movement, D::Normal),
                        Powerup(A::SunGreaves),
                        Powerup(A::Sunsetter),
                    ]),
                ]),
                Loc(L::SansaKeep),
            ]),
            L::CsBaileyEntry => Any(&[Loc(L::CsMain), Loc(L::EbEntryCastle)]),
            L::CsMain => Any(&[
                Loc(L::CsPrisonEntry),
                Loc(L::CsBaileyEntry),
                Loc(L::CsTheatreEntryNearPrison),
                All(&[
                    Loc(L::CsOldSoftlockRoom),
                    Any(&[
                        Powerup(A::ClingGem(4)),
                        All(&[
                            Powerup(A::SunGreaves),
                            Trick(T::Movement, D::Expert),
                            Trick(T::OneWall, D::Advanced),
                        ]),
                        All(&[
                            Powerup(A::SunGreaves),
                            Powerup(A::HeliacalPower),
                            Trick(T::Movement, D::Advanced),
                            Trick(T::OneWall, D::Advanced),
                        ]),
                    ]),
                ]),
                All(&[
                    Powerup(A::DreamBreaker),
                    Any(&[
                        Loc(L::CsLibraryEntry),
                        All(&[Loc(L::CsKeepClimbEntrance), Lock::SmallKey]),
                    ]),
                ]),
            ]),
            L::CsTheatreEntrance => Any(&[
                Loc(L::ThCastleEntryMain),
                All(&[
                    Loc(L::CsOldSoftlockRoom),
                    Powerup(A::Sunsetter),
                    Powerup(A::ClingGem(4)),
                    Powerup(A::HeliacalPower),
                ]),
                All(&[
                    Powerup(A::SolarWind),
                    Powerup(A::SunGreaves),
                    Trick(T::Movement, D::Advanced),
                ]),
                All(&[
                    Powerup(A::ClingGem(2)),
                    Powerup(A::SunGreaves),
                    Powerup(A::Sunsetter),
                    Trick(T::OneWall, D::Advanced),
                    Trick(T::Movement, D::Advanced),
                ]),
            ]),
            // Library
            L::LibSaveNearGreaves => All(&[
                Loc(L::MainLibrary), // Can only reach here from main library OR random spawn
                Any(&[
                    // Enter from the front entrance through the slide slot.
                    All(&[Powerup(A::DreamBreaker), Powerup(A::Slide)]),
                    // Enter through Reverse route.
                    All(&[Powerup(A::SunGreaves), Trick(T::Movement, D::Advanced)]),
                    All(&[
                        Powerup(A::ClingGem(2)),
                        Any(&[Powerup(A::Sunsetter), Powerup(A::HeliacalPower)]),
                        Trick(T::Movement, D::Expert),
                    ]),
                    All(&[
                        Powerup(A::SolarWind),
                        Powerup(A::HeliacalPower),
                        Trick(T::Movement, D::Advanced),
                    ]),
                ]),
            ]),
            L::MainLibrary => Any(&[
                All(&[Loc(L::CsMain), Powerup(A::DreamBreaker)]),
                All(&[
                    Loc(L::LibSaveNearGreaves),
                    Any(&[
                        Powerup(A::SunGreaves),
                        Powerup(A::ClingGem(2)),
                        All(&[
                            Powerup(A::DreamBreaker),
                            Powerup(A::HeliacalPower),
                            Trick(T::Movement, D::Advanced),
                        ]),
                        All(&[
                            Powerup(A::SolarWind),
                            Powerup(A::HeliacalPower),
                            Trick(T::Movement, D::Normal),
                        ]),
                    ]),
                ]),
            ]),
            L::Restricted => All(&[Loc(L::MainLibrary), Lock::SmallKey]),
            // Sansa Keep
            L::SkCastleClimbEntry => Loc(L::CsKeepClimbEntrance),
            L::SkCastleMainEntry => Any(&[Loc(L::SansaKeep), Loc(L::CsKeepEntryMain)]),
            L::SkCastleRampEntry => Any(&[
                All(&[
                    Loc(L::SansaKeep),
                    Any(&[
                        Powerup(A::ClingGem(2)),
                        Powerup(A::SunGreaves),
                        All(&[
                            Powerup(A::HeliacalPower),
                            Trick(T::Movement, D::Normal),
                            Trick(T::OneWall, D::Normal),
                        ]),
                        Powerup(A::Slide),
                    ]),
                ]),
                Loc(L::CsKeepEntryRamp),
            ]),
            L::SkUnderbellyEntry => Any(&[
                All(&[
                    Loc(L::SansaKeep),
                    Any(&[
                        Powerup(A::Sunsetter),
                        Powerup(A::HeliacalPower),
                        Powerup(A::SolarWind),
                    ]),
                ]),
                Loc(L::SansaHole),
            ]),
            L::SkTheatreEntry => Any(&[
                Loc(L::ThKeepEntry),
                All(&[
                    Loc(L::SansaKeep),
                    Any(&[
                        Powerup(A::SunGreaves),
                        Powerup(A::SolarWind),
                        Powerup(A::ClingGem(2)),
                        All(&[Powerup(A::HeliacalPower), Trick(T::Movement, D::Advanced)]),
                    ]),
                ]),
            ]),
            L::SansaKeep => Any(&[
                Loc(L::SkCastleRampEntry),
                Loc(L::SkCastleMainEntry),
                All(&[
                    Loc(L::SkTheatreEntry),
                    Any(&[
                        Powerup(A::ClingGem(2)),
                        Powerup(A::SolarWind),
                        Powerup(A::SunGreaves),
                        All(&[Powerup(A::HeliacalPower), Trick(T::Movement, D::Advanced)]),
                    ]),
                ]),
                All(&[
                    Loc(L::SkUnderbellyEntry),
                    Any(&[
                        Powerup(A::Sunsetter),
                        Powerup(A::HeliacalPower),
                        Powerup(A::SolarWind),
                        Trick(T::Movement, D::Normal),
                    ]),
                ]),
            ]),
            L::Sunsetter => All(&[
                Loc(L::SansaKeep),
                Any(&[
                    Lock::SmallKey,
                    Powerup(A::SunGreaves),
                    Powerup(A::ClingGem(2)),
                    Powerup(A::Sunsetter),
                    Trick(T::Movement, D::Advanced),
                ]),
            ]),
            // Bailey
            L::EbEntryCastle => Any(&[Loc(L::CsBaileyEntry), Loc(L::EmptyBailey)]),
            L::EbEntryRuins => All(&[
                Any(&[Loc(L::TowerRuinsEntrance), Loc(L::EmptyBailey)]),
                Any(&[
                    Powerup(A::SunGreaves),
                    All(&[Powerup(A::Sunsetter), Trick(T::SunsetterAbuse, D::Advanced)]),
                    All(&[Powerup(A::ClingGem(2)), Powerup(A::HeliacalPower)]),
                    Powerup(A::SolarWind),
                ]),
            ]),
            L::EbEntryTheatre => Any(&[Loc(L::EmptyBailey), Loc(L::PillarRoom)]),
            L::EbEntryUnderBelly => Any(&[
                Loc(L::BaileyHole),
                All(&[
                    Loc(L::EmptyBailey),
                    Any(&[
                        Powerup(A::Sunsetter),
                        Powerup(A::HeliacalPower),
                        Powerup(A::SolarWind),
                    ]),
                ]),
            ]),
            L::EmptyBailey => Any(&[
                Loc(L::EbEntryCastle),
                Loc(L::EbEntryUnderBelly),
                Loc(L::EbEntryTheatre),
                All(&[
                    Loc(L::EbEntryRuins),
                    Any(&[
                        Powerup(A::SunGreaves),
                        All(&[Powerup(A::Sunsetter), Trick(T::SunsetterAbuse, D::Advanced)]),
                        All(&[Powerup(A::ClingGem(2)), Powerup(A::HeliacalPower)]),
                        Powerup(A::SolarWind),
                    ]),
                ]),
            ]),
            // Tower
            L::TowerRuinsEntrance => Any(&[
                All(&[
                    Loc(L::EbEntryRuins),
                    Any(&[
                        Powerup(A::SunGreaves),
                        All(&[Powerup(A::Sunsetter), Trick(T::SunsetterAbuse, D::Advanced)]),
                        All(&[Powerup(A::ClingGem(2)), Powerup(A::HeliacalPower)]),
                        Powerup(A::SolarWind),
                    ]),
                ]),
                Loc(L::TowerRuinsKeep),
            ]),
            L::TowerRuinsKeep => Any(&[
                All(&[
                    Loc(L::TowerRuinsEntrance),
                    Any(&[
                        All(&[Powerup(A::SunGreaves), Trick(T::Movement, D::Expert)]),
                        All(&[
                            Powerup(A::SolarWind),
                            Powerup(A::AscendantLight),
                            Trick(T::Movement, D::Normal),
                        ]),
                        //All(&[Powerup(A::Sunsetter), Powerup(A::HeliacalPower), Trick(T::Movement, D::Expert)]), // needs 2 kicks but Sungreaves already has its own
                        All(&[
                            Powerup(A::Sunsetter),
                            Powerup(A::HeliacalPower),
                            Trick(T::Movement, D::Expert),
                            Trick(T::ClingAbuse, D::Advanced),
                            Powerup(A::ClingGem(2)),
                        ]),
                        All(&[
                            Powerup(A::SolarWind),
                            Powerup(A::SunGreaves),
                            Powerup(A::Sunsetter),
                        ]), // Intended route
                    ]),
                ]),
                Loc(L::FinalBoss),
            ]),
            // Underbelly
            L::PrisonHole => Any(&[
                All(&[Loc(L::PEntryUnderBelly), Powerup(A::DreamBreaker)]),
                All(&[
                    Loc(L::MainUnderbelly), // From main to the hole (right below the gear mobs.)
                    Any(&[
                        Powerup(A::SunGreaves),
                        Powerup(A::Sunsetter),
                        Powerup(A::SolarWind),
                    ]),
                ]),
            ]),
            L::BaileyHole => Any(&[
                All(&[
                    Powerup(A::Sunsetter),
                    Any(&[Loc(L::EbEntryUnderBelly), Loc(L::SansaHole)]),
                ]),
                Loc(L::MainUnderbelly), // From main to hole.
            ]),
            L::SansaHole => Any(&[
                All(&[
                    Powerup(A::Sunsetter),
                    Any(&[
                        Loc(L::MainUnderbelly),
                        Loc(L::BaileyHole),
                        All(&[Loc(L::HpSave), Powerup(A::Slide)]),
                    ]),
                ]),
                Loc(L::SkUnderbellyEntry),
            ]),
            L::MainUnderbelly => Any(&[
                Loc(L::PrisonHole),
                All(&[
                    Loc(L::BaileyHole),
                    Powerup(A::SunGreaves),
                    Powerup(A::HeliacalPower),
                    Powerup(A::Sunsetter),
                    Trick(T::Movement, D::Advanced),
                    Trick(T::OneWall, D::Advanced),
                ]), // First bubble directly to circular platforms.
                All(&[
                    Loc(L::HpSave),
                    Any(&[
                        Powerup(A::DreamBreaker),
                        // Below is sliding through the gap above the hanging block and then doing an ultra to skip the lever.
                        All(&[
                            Powerup(A::SolarWind),
                            Powerup(A::SunGreaves),
                            Powerup(A::ClingGem(2)),
                        ]),
                    ]),
                ]),
                All(&[Loc(L::SansaHole), Powerup(A::Sunsetter), Powerup(A::Slide)]), // from Sansa hole (above going to Major Key)
            ]),
            L::VAscendantLight => All(&[Loc(L::PrisonHole), Powerup(A::DreamBreaker)]),
            L::HpSave => Any(&[
                All(&[
                    Loc(L::BaileyHole),
                    Powerup(A::Slide),
                    Any(&[
                        Powerup(A::Sunsetter),
                        All(&[Powerup(A::HeliacalPower), Trick(T::Movement, D::Normal)]),
                    ]),
                ]),
                All(&[
                    Loc(L::MainUnderbelly),
                    Powerup(A::DreamBreaker),
                    Any(&[
                        All(&[
                            Powerup(A::HeliacalPower),
                            Any(&[Powerup(A::SunGreaves), Powerup(A::SolarWind)]),
                        ]),
                        All(&[Powerup(A::ClingGem(2)), Powerup(A::Sunsetter)]),
                    ]),
                ]),
            ]),
            //Theatre
            L::ThBaileyEntry => Any(&[
                Loc(L::EbEntryTheatre),
                All(&[
                    Loc(L::PillarRoom),
                    Any(&[
                        Powerup(A::HeliacalPower),
                        Powerup(A::ClingGem(2)),
                        Powerup(A::Sunsetter),
                    ]),
                ]),
            ]),
            L::ThCastleEntryMain => Any(&[Loc(L::CsTheatreEntrance), Loc(L::TheatreEntrance)]),
            L::ThCastleEntryPillar => Any(&[
                Loc(L::CsTheatreEntryNearPrison),
                All(&[
                    Loc(L::PillarRoom),
                    Any(&[
                        Powerup(A::HeliacalPower),
                        Powerup(A::ClingGem(2)),
                        Powerup(A::Sunsetter),
                    ]),
                ]),
            ]),
            L::ThKeepEntry => Any(&[
                Loc(L::SkTheatreEntry),
                All(&[
                    Loc(L::OtherTheatrePath),
                    Any(&[
                        Powerup(A::AscendantLight),
                        Powerup(A::HeliacalPower),
                        Powerup(A::ClingGem(2)),
                    ]),
                ]),
            ]),
            L::ThDungeonEntry => Any(&[
                All(&[
                    Loc(L::OtherTheatrePath),
                    Any(&[
                        Powerup(A::AscendantLight),
                        All(&[Powerup(A::Sunsetter), Powerup(A::HeliacalPower)]),
                        Powerup(A::SunGreaves),
                        Powerup(A::ClingGem(2)),
                    ]),
                ]),
                Loc(L::PEntryTheatre),
            ]),
            L::OtherTheatrePath => Any(&[
                All(&[
                    Any(&[Loc(L::ThKeepEntry), Loc(L::ThDungeonEntry)]),
                    Any(&[Powerup(A::ClingGem(2)), Powerup(A::AscendantLight)]),
                ]),
                All(&[Loc(L::ThKeepEntry), Powerup(A::HeliacalPower)]),
                All(&[
                    Loc(L::ThDungeonEntry),
                    Any(&[
                        Powerup(A::SunGreaves),
                        All(&[Powerup(A::Sunsetter), Powerup(A::HeliacalPower)]),
                    ]),
                ]),
            ]),
            L::PillarRoom => All(&[
                Any(&[Loc(L::ThCastleEntryPillar), Loc(L::ThBaileyEntry)]),
                Any(&[
                    Powerup(A::HeliacalPower),
                    Powerup(A::ClingGem(2)),
                    Powerup(A::Sunsetter),
                ]),
            ]),
            L::TheatreEntrance => Any(&[
                All(&[
                    Loc(L::MainTheatre),
                    Any(&[
                        Powerup(A::ClingGem(1)),
                        Powerup(A::HeliacalPower),
                        Powerup(A::SolarWind),
                    ]),
                ]),
                All(&[
                    Loc(L::ThCastleEntryMain),
                    Any(&[
                        Powerup(A::ClingGem(2)),
                        All(&[
                            Powerup(A::Slide),
                            Powerup(A::SolarWind),
                            Powerup(A::SunGreaves),
                        ]),
                        All(&[Powerup(A::HeliacalPower), Powerup(A::Sunsetter)]),
                    ]),
                ]),
            ]),
            L::MainTheatre => Any(&[
                All(&[
                    Loc(L::TheatreEntrance),
                    Any(&[
                        Powerup(A::ClingGem(2)),
                        Powerup(A::SunGreaves),
                        All(&[Powerup(A::Sunsetter), Powerup(A::HeliacalPower)]),
                    ]),
                ]),
                All(&[
                    Loc(L::PillarRoom),
                    Powerup(A::Sunsetter),
                    Any(&[
                        Powerup(A::ClingGem(2)),
                        All(&[Powerup(A::SunGreaves), Powerup(A::HeliacalPower)]),
                    ]),
                ]),
                All(&[
                    Loc(L::OtherTheatrePath),
                    Powerup(A::ClingGem(2)),
                    Any(&[
                        Powerup(A::HeliacalPower),
                        All(&[Powerup(A::Slide), Powerup(A::SolarWind)]),
                    ]),
                ]),
            ]),
            // Final Boss
            L::FinalBoss => Any(&[
                All(&[
                    Loc(L::TowerRuinsKeep),
                    Powerup(A::ClingGem(2)),
                    Any(&[
                        Powerup(A::SunGreaves),
                        All(&[Powerup(A::HeliacalPower), Powerup(A::Sunsetter)]),
                    ]),
                ]),
                Lock::Ending,
            ]),
        }
    }
    pub const fn file(&self) -> &'static str {
        match self {
            L::PEntryTheatre
            | L::PEntryCastle
            | L::PEntryUnderBelly
            | L::LatePrison
            | L::EarlyPrison
            | L::StrongEyes => "ZONE_Dungeon",
            L::CsBaileyEntry
            | L::CsPrisonEntry
            | L::CsLibraryEntry
            | L::CsTheatreEntryNearPrison
            | L::CsKeepEntryMain
            | L::CsKeepEntryRamp
            | L::CsOldSoftlockRoom
            | L::CsKeepClimbEntrance
            | L::CsMain
            | L::CsTheatreEntrance => "ZONE_LowerCastle",
            L::LibSaveNearGreaves | L::MainLibrary | L::Restricted => "Zone_Library",
            L::SkTheatreEntry
            | L::SkUnderbellyEntry
            | L::SkCastleClimbEntry
            | L::SkCastleMainEntry
            | L::SkCastleRampEntry
            | L::SansaKeep
            | L::Sunsetter => "Zone_Upper",
            L::EbEntryCastle
            | L::EbEntryRuins
            | L::EbEntryTheatre
            | L::EbEntryUnderBelly
            | L::EmptyBailey => "ZONE_Exterior",
            L::TowerRuinsEntrance | L::TowerRuinsKeep => "Zone_Tower",
            L::VAscendantLight
            | L::HpSave
            | L::SansaHole
            | L::PrisonHole
            | L::BaileyHole
            | L::MainUnderbelly => "Zone_Caves",
            L::ThDungeonEntry
            | L::ThBaileyEntry
            | L::ThCastleEntryMain
            | L::ThCastleEntryPillar
            | L::ThKeepEntry
            | L::PillarRoom
            | L::TheatreEntrance
            | L::OtherTheatrePath
            | L::MainTheatre => "Zone_Theatre",
            L::FinalBoss => "Zone_PrincessChambers",
        }
    }
    pub const fn name(&self) -> &'static str {
        match self {
            L::PEntryTheatre
            | L::PEntryCastle
            | L::PEntryUnderBelly
            | L::LatePrison
            | L::EarlyPrison
            | L::StrongEyes => "Dilapidated Dungeon",
            L::CsBaileyEntry
            | L::CsPrisonEntry
            | L::CsLibraryEntry
            | L::CsTheatreEntryNearPrison
            | L::CsKeepEntryMain
            | L::CsKeepEntryRamp
            | L::CsOldSoftlockRoom
            | L::CsKeepClimbEntrance
            | L::CsMain
            | L::CsTheatreEntrance => "Castle Sansa",
            L::LibSaveNearGreaves | L::MainLibrary | L::Restricted => "Listless Library",
            L::SkTheatreEntry
            | L::SkUnderbellyEntry
            | L::SkCastleClimbEntry
            | L::SkCastleMainEntry
            | L::SkCastleRampEntry
            | L::SansaKeep
            | L::Sunsetter => "Sansa Keep",
            L::EbEntryCastle
            | L::EbEntryRuins
            | L::EbEntryTheatre
            | L::EbEntryUnderBelly
            | L::EmptyBailey => "Empty Bailey",
            L::TowerRuinsEntrance | L::TowerRuinsKeep => "Tower Ruins",
            L::VAscendantLight
            | L::HpSave
            | L::SansaHole
            | L::PrisonHole
            | L::BaileyHole
            | L::MainUnderbelly => "Underbelly",
            L::ThDungeonEntry
            | L::ThBaileyEntry
            | L::ThCastleEntryMain
            | L::ThCastleEntryPillar
            | L::ThKeepEntry
            | L::PillarRoom
            | L::TheatreEntrance
            | L::OtherTheatrePath
            | L::MainTheatre => "Twilight Theatre",
            L::FinalBoss => "Princess",
        }
    }
}
"""
spawns_file = """
use super::*;
use Location as L;

pub const SPAWNS: [(&str, L); 48] = [
    //Prison starts
    ("gameStart", L::EarlyPrison),
    //("dungeonlowestSave", L::LatePrison),
    ("dungeonWestSave", L::LatePrison),
    ("dungeonSaveNearBoss", L::StrongEyes),
    ("dungeonWest", L::PEntryUnderBelly),
    ("dungeonNorth", L::PEntryTheatre),
    ("lower1", L::PEntryCastle),
    //Castle Starts
    ("dungeon1", L::CsPrisonEntry),
    ("lowerWestSave", L::CsMain),
    ("lowerWest", L::CsTheatreEntryNearPrison),
    ("lowerSouthHigh", L::CsKeepEntryMain),
    ("startGazebo", L::CsMain),
    ("lowerNorth", L::CsKeepEntryRamp),
    ("exterior1", L::CsBaileyEntry),
    ("lowerMiddle", L::CsKeepClimbEntrance),
    ("lowerEastSave", L::CsMain),
    ("lowerNorthWestTheatre", L::CsOldSoftlockRoom),
    ("lowerEast", L::CsLibraryEntry),
    ("lowerNorthNorthWest", L::CsTheatreEntrance),
    // Library starts
    ("libraryWest", L::MainLibrary),
    ("librarySave", L::MainLibrary),
    ("saveLibraryWest", L::LibSaveNearGreaves),
    // Sansa Keep Starts
    ("upperSouth", L::SkCastleMainEntry),
    ("saveUpperMid", L::SansaKeep),
    ("upperMiddle", L::SkCastleClimbEntry),
    ("upperNorthSave", L::SansaKeep),
    ("upperNorth", L::SkCastleRampEntry),
    ("upperNorthEast", L::SkUnderbellyEntry),
    ("upperSouthWest", L::SkTheatreEntry),
    // Empty Bailey Starts
    ("lower1", L::EbEntryCastle),
    ("exteriorWest", L::EbEntryTheatre),
    ("exteriorSouthSave", L::EmptyBailey),
    ("exteriorSouthEast", L::EbEntryRuins),
    ("exteriorEast", L::EbEntryUnderBelly),
    // Underbelly starts
    ("cavesSouth", L::BaileyHole),
    ("dungeonWest", L::PrisonHole),
    ("cavesWestSave", L::VAscendantLight),
    ("postLightSave", L::VAscendantLight),
    ("cavesSouthSave", L::BaileyHole),
    ("cavesBigMiddleStart", L::MainUnderbelly),
    ("cavesEast", L::SansaHole),
    ("cavesWest", L::PrisonHole),
    ("cavesBigSideStart", L::HpSave),
    // Theatre saves
    ("theatreEast", L::ThCastleEntryMain), // Main Entrance / up and over
    ("theatreNorthEastUpper", L::ThKeepEntry), // From Keep
    ("theatreSouthEast", L::ThCastleEntryPillar), // From Castle / pillar
    ("theatreNorthEastLower", L::ThDungeonEntry), // From Dungeon
    ("theatreSaveMain", L::MainTheatre),   // Save Crystal
    ("theatreSouthWest", L::ThBaileyEntry), // From Bailey
];
"""

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



def parse_spawns_file(raw_file: str) -> Dict[str, str]:
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


def parse_checks_file(raw_file: str) -> List[Check]:
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
        checks.append(Check(
            description=description,
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


def parse_locations_file(raw_file: str) -> List[Location]:
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
checks = parse_checks_file(checks_file)
location_objects = [
            {
                "Name": o.description,
                "Logic": parse_checks_logic(o.locks, o.location, title=o.description),
                "Handling": "Location"
            }
            for o in checks
        ]

# Default handling objects are waypoints that will be transfered to become AP regions
defaults = parse_locations_file(locations_file)
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
spawns = parse_spawns_file(spawns_file)
with open("data/spawns.py", "w") as file:
    print("Writing to spawns.py")
    file.write("spawns = " + json.dumps(spawns, indent=4) + "\n" +
               # add emptyRegionsToKeep, which is a subset of the config needed for extractor so logically useless regions don't get removed
               "emptyRegionsToKeep = " + json.dumps(sorted({region for region in spawns.values()}), indent=4))