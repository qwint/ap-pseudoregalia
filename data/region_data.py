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
            "the time trial in the starting room",
            "where dream breaker normally is",
            "where the first health piece is"
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
            "where slide normally is",
            "black hole parkour off the beaten path"
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
            "up in the rafters",
            "missable high walled room",
            "strong eyes' lair"
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
            "where memento normally is",
            "the goatling who wants to lick the checkpoint",
            "the third chair next to the goatling who wants to lick the checkpoint",
            "the second chair next to the goatling who wants to lick the checkpoint",
            "the first chair next to the goatling who wants to lick the checkpoint",
            "where indignation normally is",
            "chillin' on a ledge by the window",
            "the goatling who wanted to see the armour display",
            "the time trial behind a locked door",
            "tucked deep in a corner in the bouncer room",
            "the extremely slappable wheel guy room",
            "through the wallkick tunnel",
            "on the ledge above the bailey entrance",
            "the goatling in the gazebo",
            "the chair in the gazebo",
            "next to a bouncer in the massive room",
            "in the room with two other ones to each side"
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
            "the old softlock room",
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
            "cool moon room"
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
            "in the pit next to the dungeon entrance",
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
            "the time trial amidst the books",
            "the note next to the egg nest",
            "the chair next to the egg nest",
            "in the buttress room",
            "in the hay behind the locked door",
            "tucked deep behind the locked door"
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
            "where sun greaves normally is",
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
            "where strikebreak normally is",
            "where sunsetter normally is",
            "in an alcove next to the locked door",
            "in the room with a lever on each side",
            "tucked near the theatre entrance",
            "at the end of the parkour",
            "the time trial at the end of the parkour",
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
            "in the building you slide into",
            "guarded by the hand and soldier",
            "where solar wind normally is",
            "in the tower in the middle",
            "under the cheese bell",
            "the third locked up time trial"
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
            "near the entrance from sansa keep",
            "the soul cutter lever room"
        ],
        "transitions": []
    },
    {
        "name": "VAscendantLight",
        "exits": [],
        "locations": [
            "where ascendant light normally is",
            "in an alcove behind some pillars"
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
            "on a missable ledge in the centre",
            "the note on a high ledge in the big room",
            "black hole parkour behind strikebreak wall",
            "the second locked up time trial"
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
            "behind the second locked door",
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
            "on top of the big building"
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
            "where cling gem normally is",
            "atop the tower",
            "the time trial at the tower entrance"
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
            "on a beam in the corner",
            "the first locked up time trial"
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
            "hiding amid the boxes",
            "the goatling that will kill again",
            "the chair near the courtyard",
            "the chair in the soul cutter zone",
            "behind three maximum security cages",
            "where soul cutter normally is",
            "in the back on a pillar",
            "behind the first locked door"
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
        "name": "the time trial in the starting room",
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
        "name": "where dream breaker normally is",
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
        "name": "where the first health piece is",
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
        "name": "where slide normally is",
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
        "name": "black hole parkour off the beaten path",
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
        "name": "up in the rafters",
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
        "name": "missable high walled room",
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
        "name": "strong eyes' lair",
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
        "name": "where memento normally is",
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
        "name": "where indignation normally is",
        "logic": [],
        "is_event": False
    },
    {
        "name": "chillin' on a ledge by the window",
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
        "name": "the time trial behind a locked door",
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
        "name": "tucked deep in a corner in the bouncer room",
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
        "name": "the extremely slappable wheel guy room",
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
        "name": "the old softlock room",
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
        "name": "cool moon room",
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
        "name": "through the wallkick tunnel",
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
        "name": "in the pit next to the dungeon entrance",
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
        "name": "on the ledge above the bailey entrance",
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
        "name": "next to a bouncer in the massive room",
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
        "name": "in the room with two other ones to each side",
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
        "name": "the time trial amidst the books",
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
        "name": "where sun greaves normally is",
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
        "name": "in the buttress room",
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
        "name": "in the hay behind the locked door",
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
        "name": "tucked deep behind the locked door",
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
        "name": "where strikebreak normally is",
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
        "name": "where sunsetter normally is",
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
        "name": "in an alcove next to the locked door",
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
        "name": "in the room with a lever on each side",
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
        "name": "tucked near the theatre entrance",
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
        "name": "at the end of the parkour",
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
        "name": "the time trial at the end of the parkour",
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
        "name": "in the building you slide into",
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
        "name": "guarded by the hand and soldier",
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
        "name": "where solar wind normally is",
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
        "name": "in the tower in the middle",
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
        "name": "under the cheese bell",
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
        "name": "the third locked up time trial",
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
        "name": "near the entrance from sansa keep",
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
        "name": "the soul cutter lever room",
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
        "name": "where ascendant light normally is",
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
        "name": "in an alcove behind some pillars",
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
        "name": "on a missable ledge in the centre",
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
        "name": "black hole parkour behind strikebreak wall",
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
        "name": "the second locked up time trial",
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
        "name": "behind the second locked door",
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
        "name": "on top of the big building",
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
        "name": "where cling gem normally is",
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
        "name": "atop the tower",
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
        "name": "the time trial at the tower entrance",
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
        "name": "on a beam in the corner",
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
        "name": "the first locked up time trial",
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
        "name": "hiding amid the boxes",
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
        "name": "behind three maximum security cages",
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
        "name": "where soul cutter normally is",
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
        "name": "in the back on a pillar",
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
        "name": "behind the first locked door",
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
