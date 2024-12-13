# This file is programmatically generated, do not modify by hand

regions = [
    {
        "name": "EarlyPrison",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Trick_Knowledge_Normal",
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "LatePrison"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_2",
                            "Powerup_AirKick_3",
                            "Powerup_AirKick_1",
                            "Powerup_Sunsetter",
                            "Powerup_ClingPart_6",
                            "Trick_ClingAbuse_Expert",
                            "Trick_Movement_Expert",
                            "Trick_Momentum_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "CsPrisonEntry"
            }
        ],
        "locations": [
            "the goatling who fell out his cage",
            "Dilapidated Dungeon - Time Trial",
            "Dilapidated Dungeon - Dream Breaker",
            "Dilapidated Dungeon - Alcove Near Mirror"
        ],
        "transitions": []
    },
    {
        "name": "LatePrison",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Trick_Knowledge_Normal"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "EarlyPrison"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "StrongEyes"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_6"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AscendantLight"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "PEntryTheatre"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "PrisonHole"
            }
        ],
        "locations": [
            "Dilapidated Dungeon - Slide",
            "Dilapidated Dungeon - Dark Orbs"
        ],
        "transitions": []
    },
    {
        "name": "StrongEyes",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1",
                            "Lock::SmallKey"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Trick_Knowledge_Normal",
                            "Lock::SmallKey"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Trick_Knowledge_Normal",
                            "Powerup_ProgressiveDreamBreaker_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "EarlyPrison"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Lock::SmallKey"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "CsPrisonEntry"
            }
        ],
        "locations": [
            "Dilapidated Dungeon - Rafters",
            "Dilapidated Dungeon - Past Poles",
            "Dilapidated Dungeon - Strong Eyes"
        ],
        "transitions": []
    },
    {
        "name": "CsMain",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Trick_Knowledge_Normal",
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "LatePrison"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Trick_Knowledge_Normal"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "EarlyPrison"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Lock::SmallKey"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Powerup_ProgressiveDreamBreaker_1",
                            "Trick_Knowledge_Normal"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "StrongEyes"
            },
            {
                "logic": [],
                "target": "CsPrisonEntry"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "CsLibraryEntry"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_1",
                            "Trick_Movement_Advanced",
                            "Trick_Momentum_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Powerup_AirKick_3"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_1",
                            "Powerup_ProgressiveSlide_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3",
                            "Trick_Movement_Normal"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Trick_Movement_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_4",
                            "Trick_ClingAbuse_Normal"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_1",
                            "Powerup_ProgressiveSlide_2",
                            "Trick_Movement_Normal"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "CsTheatreEntryNearPrison"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "CsOldSoftlockRoom"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Lock::SmallKey"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "CsKeepClimbEntrance"
            },
            {
                "logic": [],
                "target": "CsKeepEntryMain"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Trick_Movement_Normal"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "CsKeepEntryRamp"
            },
            {
                "logic": [],
                "target": "CsBaileyEntry"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "MainLibrary"
            }
        ],
        "locations": [
            "the goatling lamenting the skill issue of players who need a map",
            "Castle Sansa - Memento",
            "the goatling who wants to lick the checkpoint",
            "the third chair next to the goatling who wants to lick the checkpoint",
            "the second chair next to the goatling who wants to lick the checkpoint",
            "the first chair next to the goatling who wants to lick the checkpoint",
            "Castle Sansa - Indignation",
            "Castle Sansa - Platform In Main Halls",
            "the goatling who wanted to see the armour display",
            "Castle Sansa - Time Trial",
            "Castle Sansa - Corner Corridor",
            "Castle Sansa - Wheel Crawlers",
            "Castle Sansa - Tall Room Near Wheel Crawlers",
            "Castle Sansa - Balcony",
            "the goatling in the gazebo",
            "the chair in the gazebo",
            "Castle Sansa - Floater In Courtyard",
            "Castle Sansa - High Climb From Courtyard"
        ],
        "transitions": []
    },
    {
        "name": "CsOldSoftlockRoom",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_4"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3",
                            "Trick_Movement_Expert",
                            "Trick_OneWall_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3",
                            "Powerup_AirKick_1",
                            "Trick_Movement_Advanced",
                            "Trick_OneWall_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "CsMain"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Powerup_ClingPart_4",
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "CsTheatreEntrance"
            }
        ],
        "locations": [
            "Castle Sansa - Alcove Near Scythe Corridor",
            "the goatling about to jump into the haze"
        ],
        "transitions": []
    },
    {
        "name": "CsTheatreEntrance",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_2",
                            "Powerup_AirKick_1",
                            "Trick_Movement_Normal"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_1",
                            "Powerup_ClingPart_2",
                            "Trick_Movement_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "CsOldSoftlockRoom"
            },
            {
                "logic": [],
                "target": "ThCastleEntryMain"
            }
        ],
        "locations": [
            "Castle Sansa - Near Theatre Front"
        ],
        "transitions": []
    },
    {
        "name": "CsTheatreEntryNearPrison",
        "exits": [
            {
                "logic": [],
                "target": "CsMain"
            },
            {
                "logic": [],
                "target": "ThCastleEntryPillar"
            }
        ],
        "locations": [
            "Castle Sansa - Alcove Near Dungeon",
            "the goatling that calls you bubble girl"
        ],
        "transitions": []
    },
    {
        "name": "MainLibrary",
        "exits": [
            {
                "logic": [],
                "target": "CsLibraryEntry"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1",
                            "Powerup_ProgressiveSlide_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3",
                            "Trick_Movement_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2",
                            "Powerup_Sunsetter",
                            "Trick_Movement_Expert"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2",
                            "Powerup_AirKick_1",
                            "Trick_Movement_Expert"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_2",
                            "Powerup_AirKick_1",
                            "Trick_Movement_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "LibSaveNearGreaves"
            }
        ],
        "locations": [
            "the chair at the entrance",
            "Listless Library - Time Trial",
            "the note next to the egg nest",
            "the chair next to the egg nest",
            "Listless Library - Upper Back",
            "Listless Library - Locked Door Across",
            "Listless Library - Locked Door Left"
        ],
        "transitions": []
    },
    {
        "name": "LibSaveNearGreaves",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1",
                            "Powerup_AirKick_1",
                            "Trick_Movement_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_2",
                            "Powerup_AirKick_1",
                            "Trick_Movement_Normal"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "MainLibrary"
            }
        ],
        "locations": [
            "Listless Library - Sun Greaves",
            "the chair after the normal sun greaves location"
        ],
        "transitions": []
    },
    {
        "name": "SansaKeep",
        "exits": [
            {
                "logic": [],
                "target": "CsKeepEntryMain"
            },
            {
                "logic": [],
                "target": "CsKeepEntryRamp"
            },
            {
                "logic": [],
                "target": "SkCastleMainEntry"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_1",
                            "Trick_Movement_Normal",
                            "Trick_OneWall_Normal"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "SkCastleRampEntry"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "SkUnderbellyEntry"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_1",
                            "Trick_Movement_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "SkTheatreEntry"
            }
        ],
        "locations": [
            "the goatling sad about the lack of furniture",
            "Sansa Keep - Strikebreak",
            "Sansa Keep - Sunsetter",
            "Sansa Keep - Alcove Near Locked Door",
            "Sansa Keep - Levers Room",
            "Sansa Keep - Near Theatre",
            "Sansa Keep - Lonely Throne",
            "Sansa Keep - Time Trial",
            "the chair in the middle of the parkour"
        ],
        "transitions": []
    },
    {
        "name": "SkCastleRampEntry",
        "exits": [
            {
                "logic": [],
                "target": "SansaKeep"
            }
        ],
        "locations": [
            "the goatling collapsing out of reality",
            "the chair collapsing out of reality"
        ],
        "transitions": []
    },
    {
        "name": "EmptyBailey",
        "exits": [
            {
                "logic": [],
                "target": "EbEntryCastle"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Trick_SunsetterAbuse_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2",
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "EbEntryRuins"
            },
            {
                "logic": [],
                "target": "EbEntryTheatre"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "EbEntryUnderBelly"
            }
        ],
        "locations": [
            "the goatling who's hiding",
            "Empty Bailey - Inside Building",
            "Empty Bailey - Guarded Hand",
            "Empty Bailey - Solar Wind",
            "Empty Bailey - Center Steeple",
            "Empty Bailey - Cheese Bell",
            "Empty Bailey - Time Trial"
        ],
        "transitions": []
    },
    {
        "name": "SansaHole",
        "exits": [
            {
                "logic": [],
                "target": "SkUnderbellyEntry"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "BaileyHole"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Powerup_ProgressiveSlide_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "MainUnderbelly"
            }
        ],
        "locations": [
            "The Underbelly - Rafters Near Keep",
            "The Underbelly - Surrounded By Holes"
        ],
        "transitions": []
    },
    {
        "name": "VAscendantLight",
        "exits": [],
        "locations": [
            "The Underbelly - Ascendant Light",
            "The Underbelly - Alcove Near Light"
        ],
        "transitions": []
    },
    {
        "name": "MainUnderbelly",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "PrisonHole"
            },
            {
                "logic": [],
                "target": "BaileyHole"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "SansaHole"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1",
                            "Powerup_AirKick_1",
                            "Powerup_AirKick_3"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1",
                            "Powerup_AirKick_1",
                            "Powerup_ProgressiveSlide_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1",
                            "Powerup_ClingPart_2",
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "HpSave"
            }
        ],
        "locations": [
            "The Underbelly - Main Room",
            "the note on a high ledge in the big room",
            "The Underbelly - Strikebreak Wall",
            "The Underbelly - Time Trial"
        ],
        "transitions": []
    },
    {
        "name": "HpSave",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Powerup_ProgressiveSlide_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "SansaHole"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_2",
                            "Powerup_AirKick_3",
                            "Powerup_ClingPart_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "MainUnderbelly"
            }
        ],
        "locations": [
            "The Underbelly - Locked Door",
            "the note behind the locked door"
        ],
        "transitions": []
    },
    {
        "name": "BaileyHole",
        "exits": [
            {
                "logic": [],
                "target": "EbEntryUnderBelly"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "SansaHole"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3",
                            "Powerup_AirKick_1",
                            "Powerup_Sunsetter",
                            "Trick_Movement_Advanced",
                            "Trick_OneWall_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "MainUnderbelly"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_1",
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_1",
                            "Powerup_AirKick_1",
                            "Trick_Movement_Normal"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "HpSave"
            }
        ],
        "locations": [
            "the note near the empty bailey entrance",
            "The Underbelly - Building Near Little Guy"
        ],
        "transitions": []
    },
    {
        "name": "TowerRuinsKeep",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2",
                            "Powerup_AirKick_3",
                            "Lock::Ending"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2",
                            "Powerup_AirKick_1",
                            "Powerup_Sunsetter",
                            "Lock::Ending"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "FinalBoss"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Trick_SunsetterAbuse_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2",
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "EbEntryRuins"
            }
        ],
        "locations": [
            "Tower Remains - Cling Gem",
            "Tower Remains - Atop The Tower",
            "Tower Remains - Time Trial"
        ],
        "transitions": []
    },
    {
        "name": "PillarRoom",
        "exits": [
            {
                "logic": [],
                "target": "CsTheatreEntryNearPrison"
            },
            {
                "logic": [],
                "target": "EbEntryTheatre"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "ThBaileyEntry"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "ThCastleEntryPillar"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Powerup_ClingPart_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Powerup_AirKick_3",
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "MainTheatre"
            }
        ],
        "locations": [
            "Twilight Theatre - Corner Beam",
            "Twilight Theatre - Time Trial"
        ],
        "transitions": []
    },
    {
        "name": "OtherTheatrePath",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_AscendantLight"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "ThKeepEntry"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_AscendantLight"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "ThDungeonEntry"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2",
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2",
                            "Powerup_ProgressiveSlide_1",
                            "Powerup_ProgressiveSlide_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "MainTheatre"
            }
        ],
        "locations": [
            "the third chair around the table",
            "the second chair around the table",
            "the first chair around the table",
            "the chair next to the books"
        ],
        "transitions": []
    },
    {
        "name": "TheatreEntrance",
        "exits": [
            {
                "logic": [],
                "target": "ThCastleEntryMain"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "MainTheatre"
            }
        ],
        "locations": [
            "the goatling who can eat 20 beans at least",
            "the goatling who thought the theatre was safe",
            "the second goatling who really wanted to see the show",
            "the first goatling who really wanted to see the show"
        ],
        "transitions": []
    },
    {
        "name": "MainTheatre",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "TheatreEntrance"
            }
        ],
        "locations": [
            "Twilight Theatre - Murderous Goat",
            "the goatling that will kill again",
            "the chair near the courtyard",
            "the chair in the soul cutter zone",
            "Twilight Theatre - Center Stage",
            "Twilight Theatre - Soul Cutter",
            "Twilight Theatre - Back Of Auditorium",
            "Twilight Theatre - Locked Door"
        ],
        "transitions": []
    },
    {
        "name": "PrisonHole",
        "exits": [
            {
                "logic": [],
                "target": "MainUnderbelly"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "VAscendantLight"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_AscendantLight",
                            "Powerup_ProgressiveDreamBreaker_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AscendantLight",
                            "Trick_Knowledge_Normal",
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "LatePrison"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "CsPrisonEntry",
        "exits": [
            {
                "logic": [],
                "target": "CsMain"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "PEntryTheatre",
        "exits": [
            {
                "logic": [],
                "target": "ThDungeonEntry"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "ThDungeonEntry",
        "exits": [
            {
                "logic": [],
                "target": "PEntryTheatre"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AscendantLight"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "OtherTheatrePath"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "CsLibraryEntry",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "CsMain"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "CsKeepClimbEntrance",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveDreamBreaker_1",
                            "Lock::SmallKey"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "CsMain"
            },
            {
                "logic": [],
                "target": "SkCastleClimbEntry"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "CsKeepEntryMain",
        "exits": [
            {
                "logic": [],
                "target": "SkCastleMainEntry"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "CsKeepEntryRamp",
        "exits": [
            {
                "logic": [],
                "target": "SkCastleRampEntry"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "CsBaileyEntry",
        "exits": [
            {
                "logic": [],
                "target": "CsMain"
            },
            {
                "logic": [],
                "target": "EbEntryCastle"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "EbEntryCastle",
        "exits": [
            {
                "logic": [],
                "target": "CsBaileyEntry"
            },
            {
                "logic": [],
                "target": "EmptyBailey"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "ThCastleEntryMain",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3",
                            "Powerup_ProgressiveSlide_2",
                            "Trick_Movement_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3",
                            "Powerup_ClingPart_2",
                            "Powerup_Sunsetter",
                            "Trick_OneWall_Advanced",
                            "Trick_Movement_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "CsTheatreEntrance"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_1",
                            "Powerup_ProgressiveSlide_2",
                            "Powerup_AirKick_3"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_1",
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "TheatreEntrance"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "SkCastleClimbEntry",
        "exits": [],
        "locations": [],
        "transitions": []
    },
    {
        "name": "SkCastleMainEntry",
        "exits": [
            {
                "logic": [],
                "target": "SansaKeep"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "SkUnderbellyEntry",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Trick_Movement_Normal"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "SansaKeep"
            },
            {
                "logic": [],
                "target": "SansaHole"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "SkTheatreEntry",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_1",
                            "Trick_Movement_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "SansaKeep"
            },
            {
                "logic": [],
                "target": "ThKeepEntry"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "ThKeepEntry",
        "exits": [
            {
                "logic": [],
                "target": "SkTheatreEntry"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AscendantLight"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "OtherTheatrePath"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "EbEntryRuins",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter",
                            "Trick_SunsetterAbuse_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2",
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "EmptyBailey"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_AirKick_3",
                            "Trick_Movement_Expert"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2",
                            "Powerup_AirKick_1",
                            "Powerup_Sunsetter",
                            "Trick_Movement_Expert",
                            "Trick_ClingAbuse_Advanced"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_2",
                            "Powerup_AscendantLight",
                            "Trick_Movement_Normal"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ProgressiveSlide_2",
                            "Powerup_AirKick_3",
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "TowerRuinsKeep"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "EbEntryTheatre",
        "exits": [
            {
                "logic": [],
                "target": "EmptyBailey"
            },
            {
                "logic": [],
                "target": "ThBaileyEntry"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "EbEntryUnderBelly",
        "exits": [
            {
                "logic": [],
                "target": "EmptyBailey"
            },
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "BaileyHole"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "FinalBoss",
        "exits": [
            {
                "logic": [],
                "target": "TowerRuinsKeep"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "ThBaileyEntry",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "PillarRoom"
            }
        ],
        "locations": [],
        "transitions": []
    },
    {
        "name": "ThCastleEntryPillar",
        "exits": [
            {
                "logic": [
                    {
                        "item_requirements": [
                            "Powerup_AirKick_1"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_ClingPart_2"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    },
                    {
                        "item_requirements": [
                            "Powerup_Sunsetter"
                        ],
                        "location_requirements": [],
                        "region_requirements": [],
                        "state_modifiers": []
                    }
                ],
                "target": "PillarRoom"
            }
        ],
        "locations": [],
        "transitions": []
    }
]
locations = [
    {
        "name": "the goatling who fell out his cage",
        "logic": [],
        "is_event": False
    },
    {
        "name": "Dilapidated Dungeon - Time Trial",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_3",
                    "Powerup_ClingPart_6",
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Dilapidated Dungeon - Dream Breaker",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3",
                    "Trick_Movement_Expert",
                    "Trick_OneWall_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3",
                    "Powerup_ProgressiveSlide_2",
                    "Trick_Movement_Advanced",
                    "Trick_OneWall_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Trick_Knowledge_Expert"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Dilapidated Dungeon - Alcove Near Mirror",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AscendantLight"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Trick_Movement_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_4",
                    "Trick_ClingAbuse_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [],
                "location_requirements": [],
                "region_requirements": [
                    "CsMain"
                ],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Dilapidated Dungeon - Slide",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Powerup_AirKick_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_1",
                    "Trick_Movement_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Trick_Movement_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Dilapidated Dungeon - Dark Orbs",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ClingPart_6"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AscendantLight",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3",
                    "Powerup_ProgressiveSlide_2",
                    "Trick_Movement_Advanced",
                    "Trick_OneWall_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Dilapidated Dungeon - Rafters",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_AirKick_3",
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_4",
                    "Trick_ClingAbuse_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Dilapidated Dungeon - Past Poles",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_ClingPart_4"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Trick_Knowledge_Normal",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Trick_Knowledge_Normal",
                    "Powerup_ClingPart_4"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Dilapidated Dungeon - Strong Eyes",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "the goatling lamenting the skill issue of players who need a map",
        "logic": [],
        "is_event": False
    },
    {
        "name": "Castle Sansa - Memento",
        "logic": [],
        "is_event": False
    },
    {
        "name": "the goatling who wants to lick the checkpoint",
        "logic": [],
        "is_event": False
    },
    {
        "name": "the third chair next to the goatling who wants to lick the checkpoint",
        "logic": [],
        "is_event": False
    },
    {
        "name": "the second chair next to the goatling who wants to lick the checkpoint",
        "logic": [],
        "is_event": False
    },
    {
        "name": "the first chair next to the goatling who wants to lick the checkpoint",
        "logic": [],
        "is_event": False
    },
    {
        "name": "Castle Sansa - Indignation",
        "logic": [],
        "is_event": False
    },
    {
        "name": "Castle Sansa - Platform In Main Halls",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_1",
                    "Trick_Movement_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_2",
                    "Trick_ClingAbuse_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "the goatling who wanted to see the armour display",
        "logic": [],
        "is_event": False
    },
    {
        "name": "Castle Sansa - Time Trial",
        "logic": [
            {
                "item_requirements": [
                    "Lock::SmallKey"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Castle Sansa - Corner Corridor",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ClingPart_6"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3",
                    "Powerup_AirKick_1",
                    "Trick_Movement_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Castle Sansa - Wheel Crawlers",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_AscendantLight"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3",
                    "Trick_OneWall_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Castle Sansa - Alcove Near Scythe Corridor",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ClingPart_6",
                    "Trick_ClingAbuse_Expert",
                    "Trick_Movement_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_3",
                    "Powerup_AirKick_1",
                    "Powerup_AscendantLight"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_1",
                    "Trick_Movement_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3",
                    "Powerup_Sunsetter",
                    "Trick_OneWall_Advanced",
                    "Trick_SunsetterAbuse_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "the goatling about to jump into the haze",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Trick_Knowledge_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Castle Sansa - Near Theatre Front",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ClingPart_6",
                    "Trick_ClingAbuse_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_3",
                    "Powerup_AirKick_1",
                    "Trick_Movement_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Powerup_ClingPart_4",
                    "Trick_ClingAbuse_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Powerup_AirKick_3",
                    "Powerup_ClingPart_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_ClingPart_2",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Castle Sansa - Tall Room Near Wheel Crawlers",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_ClingPart_6"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_ClingPart_2",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_ClingPart_2",
                    "Powerup_AirKick_1",
                    "Trick_Movement_Advanced",
                    "Trick_OneWall_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Trick_Knowledge_Normal",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Trick_Knowledge_Normal",
                    "Powerup_ClingPart_6"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Trick_Knowledge_Normal",
                    "Powerup_ClingPart_2",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Trick_Knowledge_Normal",
                    "Powerup_ClingPart_2",
                    "Powerup_AirKick_1",
                    "Trick_Movement_Advanced",
                    "Trick_OneWall_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3",
                    "Powerup_AirKick_1",
                    "Trick_OneWall_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_1",
                    "Trick_Movement_Normal",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_1",
                    "Trick_Movement_Normal",
                    "Powerup_ClingPart_6"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_1",
                    "Trick_Movement_Normal",
                    "Powerup_ClingPart_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Trick_Movement_Advanced",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Trick_Movement_Advanced",
                    "Powerup_ClingPart_6"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Trick_Movement_Advanced",
                    "Powerup_ClingPart_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Castle Sansa - Alcove Near Dungeon",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ClingPart_4"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "the goatling that calls you bubble girl",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_AirKick_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_4"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Castle Sansa - Balcony",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_AirKick_3",
                    "Powerup_AirKick_1",
                    "Trick_Movement_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_4"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "the goatling in the gazebo",
        "logic": [],
        "is_event": False
    },
    {
        "name": "the chair in the gazebo",
        "logic": [],
        "is_event": False
    },
    {
        "name": "Castle Sansa - Floater In Courtyard",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_AscendantLight",
                    "Trick_Movement_Normal",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AscendantLight",
                    "Trick_Movement_Normal",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3",
                    "Powerup_AirKick_1",
                    "Trick_OneWall_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_6",
                    "Powerup_AirKick_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_6",
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_6",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_6",
                    "Powerup_AscendantLight"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Castle Sansa - High Climb From Courtyard",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ClingPart_6",
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_6",
                    "Powerup_AirKick_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_6",
                    "Trick_ClingAbuse_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_1",
                    "Trick_Movement_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Trick_Movement_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "the chair at the entrance",
        "logic": [],
        "is_event": False
    },
    {
        "name": "Listless Library - Time Trial",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_Sunsetter",
                    "Trick_Movement_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_AirKick_3",
                    "Trick_Movement_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_ProgressiveSlide_2",
                    "Trick_Movement_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_ClingPart_6",
                    "Trick_Movement_Advanced",
                    "Trick_ClingAbuse_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_Sunsetter",
                    "Powerup_AirKick_1",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Trick_Knowledge_Normal",
                    "Trick_Movement_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Trick_Knowledge_Normal",
                    "Powerup_AirKick_3",
                    "Trick_Movement_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Trick_Knowledge_Normal",
                    "Powerup_ProgressiveSlide_2",
                    "Trick_Movement_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Trick_Knowledge_Normal",
                    "Powerup_AirKick_1",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Listless Library - Sun Greaves",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Trick_Knowledge_Advanced",
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "the chair after the normal sun greaves location",
        "logic": [],
        "is_event": False
    },
    {
        "name": "the note next to the egg nest",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_4"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "the chair next to the egg nest",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_4"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Listless Library - Upper Back",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_4"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Listless Library - Locked Door Across",
        "logic": [
            {
                "item_requirements": [
                    "Lock::SmallKey",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Lock::SmallKey",
                    "Powerup_AirKick_1",
                    "Trick_Movement_Expert"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Lock::SmallKey",
                    "Powerup_ClingPart_4"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Listless Library - Locked Door Left",
        "logic": [
            {
                "item_requirements": [
                    "Lock::SmallKey",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Lock::SmallKey",
                    "Powerup_AirKick_1",
                    "Trick_Movement_Expert"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Lock::SmallKey",
                    "Powerup_ClingPart_4"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "the goatling sad about the lack of furniture",
        "logic": [],
        "is_event": False
    },
    {
        "name": "the goatling collapsing out of reality",
        "logic": [],
        "is_event": False
    },
    {
        "name": "the chair collapsing out of reality",
        "logic": [],
        "is_event": False
    },
    {
        "name": "Sansa Keep - Strikebreak",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_2",
                    "Powerup_AirKick_1",
                    "Trick_Movement_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_2",
                    "Powerup_ClingPart_4"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_2",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Sansa Keep - Sunsetter",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ClingPart_2",
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Trick_ClingAbuse_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Powerup_ProgressiveDreamBreaker_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Trick_Movement_Advanced",
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_AirKick_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Sansa Keep - Alcove Near Locked Door",
        "logic": [
            {
                "item_requirements": [
                    "Lock::SmallKey",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Lock::SmallKey",
                    "Trick_Movement_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_2",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_2",
                    "Trick_Movement_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Trick_Movement_Advanced",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Trick_Movement_Advanced",
                    "Trick_Movement_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Sansa Keep - Levers Room",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Trick_Knowledge_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Sansa Keep - Near Theatre",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_4"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Sansa Keep - Lonely Throne",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_AscendantLight",
                    "Powerup_ClingPart_4",
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AscendantLight",
                    "Powerup_ClingPart_4",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AscendantLight",
                    "Powerup_Sunsetter",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_ProgressiveSlide_1",
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_Sunsetter",
                    "Powerup_ClingPart_2",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Sansa Keep - Time Trial",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_3",
                    "Powerup_ClingPart_6",
                    "Powerup_Sunsetter",
                    "Powerup_AscendantLight"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "the chair in the middle of the parkour",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_AscendantLight",
                    "Powerup_ClingPart_4",
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AscendantLight",
                    "Powerup_ClingPart_4",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AscendantLight",
                    "Powerup_Sunsetter",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_ProgressiveSlide_1",
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_Sunsetter",
                    "Powerup_ClingPart_2",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "the goatling who's hiding",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Empty Bailey - Inside Building",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Empty Bailey - Guarded Hand",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_4"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Trick_Movement_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [
                    "EbEntryUnderBelly"
                ],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Empty Bailey - Solar Wind",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_1",
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_1",
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_AirKick_1",
                    "Trick_Movement_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_1",
                    "Powerup_Sunsetter",
                    "Trick_Knowledge_Normal",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_1",
                    "Powerup_Sunsetter",
                    "Trick_Knowledge_Normal",
                    "Powerup_AirKick_1",
                    "Trick_Movement_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Empty Bailey - Center Steeple",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_1",
                    "Trick_ReverseKick_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3",
                    "Trick_OneWall_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_ClingPart_6"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Empty Bailey - Cheese Bell",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_ClingPart_6"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_Sunsetter",
                    "Powerup_AirKick_1",
                    "Trick_Movement_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Trick_Movement_Advanced",
                    "Powerup_Sunsetter",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_4",
                    "Powerup_Sunsetter",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Empty Bailey - Time Trial",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_3",
                    "Powerup_ClingPart_6",
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "The Underbelly - Rafters Near Keep",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Powerup_AirKick_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "The Underbelly - Surrounded By Holes",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_Sunsetter",
                    "Powerup_ProgressiveDreamBreaker_3",
                    "Powerup_AscendantLight"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_Sunsetter",
                    "Powerup_ProgressiveDreamBreaker_3",
                    "Powerup_ClingPart_6"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_Sunsetter",
                    "Powerup_AirKick_3",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "The Underbelly - Ascendant Light",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Trick_Knowledge_Expert"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "The Underbelly - Alcove Near Light",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Trick_Knowledge_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "The Underbelly - Main Room",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "the note on a high ledge in the big room",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_AirKick_1",
                    "Powerup_Sunsetter",
                    "Powerup_ClingPart_6"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_1",
                    "Powerup_Sunsetter",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_1",
                    "Powerup_Sunsetter",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "The Underbelly - Strikebreak Wall",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_2",
                    "Powerup_AscendantLight",
                    "Powerup_AirKick_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_2",
                    "Powerup_AscendantLight",
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_2",
                    "Powerup_AscendantLight",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_2",
                    "Powerup_AscendantLight",
                    "Powerup_ClingPart_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "The Underbelly - Time Trial",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_3",
                    "Powerup_ClingPart_6",
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "The Underbelly - Locked Door",
        "logic": [
            {
                "item_requirements": [
                    "Lock::SmallKey"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "the note behind the locked door",
        "logic": [
            {
                "item_requirements": [
                    "Lock::SmallKey"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "the note near the empty bailey entrance",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_1",
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_6"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AscendantLight"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_1",
                    "Trick_ReverseKick_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter",
                    "Trick_Movement_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "The Underbelly - Building Near Little Guy",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Tower Remains - Cling Gem",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ClingPart_6"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_1",
                    "Powerup_Sunsetter",
                    "Trick_Movement_Normal"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Tower Remains - Atop The Tower",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ClingPart_2",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_2",
                    "Powerup_AirKick_1",
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3",
                    "Powerup_ProgressiveSlide_2",
                    "Trick_Movement_Expert",
                    "Trick_OneWall_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Tower Remains - Time Trial",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_3",
                    "Powerup_ClingPart_6",
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Twilight Theatre - Corner Beam",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_AirKick_3",
                    "Powerup_ClingPart_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3",
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_ClingPart_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Twilight Theatre - Time Trial",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_1",
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_3",
                    "Powerup_ClingPart_6",
                    "Powerup_Sunsetter"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "the third chair around the table",
        "logic": [],
        "is_event": False
    },
    {
        "name": "the second chair around the table",
        "logic": [],
        "is_event": False
    },
    {
        "name": "the first chair around the table",
        "logic": [],
        "is_event": False
    },
    {
        "name": "the chair next to the books",
        "logic": [],
        "is_event": False
    },
    {
        "name": "the goatling who can eat 20 beans at least",
        "logic": [],
        "is_event": False
    },
    {
        "name": "the goatling who thought the theatre was safe",
        "logic": [],
        "is_event": False
    },
    {
        "name": "the second goatling who really wanted to see the show",
        "logic": [],
        "is_event": False
    },
    {
        "name": "the first goatling who really wanted to see the show",
        "logic": [],
        "is_event": False
    },
    {
        "name": "Twilight Theatre - Murderous Goat",
        "logic": [],
        "is_event": False
    },
    {
        "name": "the goatling that will kill again",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_6"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "the chair near the courtyard",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ClingPart_4"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_1",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "the chair in the soul cutter zone",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_2",
                    "Powerup_ClingPart_6",
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_1",
                    "Powerup_AirKick_3",
                    "Powerup_Sunsetter",
                    "Trick_ClingAbuse_Expert",
                    "Trick_OneWall_Expert",
                    "Trick_Movement_Insane",
                    "Trick_Momentum_Expert"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_2",
                    "Powerup_ClingPart_6",
                    "Powerup_ProgressiveDreamBreaker_3",
                    "Powerup_AirKick_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_2",
                    "Powerup_ClingPart_6",
                    "Powerup_ProgressiveDreamBreaker_3",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Twilight Theatre - Center Stage",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_2",
                    "Powerup_ClingPart_6",
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_1",
                    "Powerup_AirKick_3",
                    "Powerup_Sunsetter",
                    "Trick_ClingAbuse_Expert",
                    "Trick_OneWall_Expert",
                    "Trick_Movement_Insane",
                    "Trick_Momentum_Expert"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_2",
                    "Powerup_ClingPart_6",
                    "Powerup_ProgressiveDreamBreaker_3",
                    "Powerup_AirKick_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_2",
                    "Powerup_ClingPart_6",
                    "Powerup_ProgressiveDreamBreaker_3",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Twilight Theatre - Soul Cutter",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_2",
                    "Powerup_ProgressiveSlide_2",
                    "Trick_Movement_Expert",
                    "Powerup_AirKick_3",
                    "Powerup_AirKick_1",
                    "Powerup_ClingPart_6",
                    "Powerup_Sunsetter",
                    "Trick_OneWall_Expert",
                    "Trick_Knowledge_Advanced"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_2",
                    "Powerup_ProgressiveSlide_2",
                    "Powerup_AirKick_1",
                    "Powerup_AirKick_3",
                    "Powerup_Sunsetter",
                    "Trick_ClingAbuse_Expert",
                    "Trick_OneWall_Expert",
                    "Trick_Movement_Insane",
                    "Trick_Momentum_Expert"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_2",
                    "Powerup_ProgressiveDreamBreaker_3",
                    "Powerup_AirKick_1"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ProgressiveDreamBreaker_2",
                    "Powerup_ProgressiveDreamBreaker_3",
                    "Powerup_ProgressiveSlide_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Twilight Theatre - Back Of Auditorium",
        "logic": [
            {
                "item_requirements": [
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Powerup_ClingPart_6"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    },
    {
        "name": "Twilight Theatre - Locked Door",
        "logic": [
            {
                "item_requirements": [
                    "Lock::SmallKey",
                    "Powerup_AirKick_3"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            },
            {
                "item_requirements": [
                    "Lock::SmallKey",
                    "Powerup_ClingPart_2"
                ],
                "location_requirements": [],
                "region_requirements": [],
                "state_modifiers": []
            }
        ],
        "is_event": False
    }
]
transitions = []
transition_to_region_map = {}
