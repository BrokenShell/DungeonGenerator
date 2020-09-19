from DungeonGenerator.npc_lib import npc_dict


things_dict = {
    'actions': npc_dict["quests"],
    'trinkets': [f"Find {itm}" for itm in npc_dict["trinkets"]],
    "skills": (
        "Acrobatics, DEX",
        "Animal handling, WIS",
        "Arcana, INT",
        "Athletics, STR",
        "Deception, CHA",
        "History, INT",
        "Insight, WIS",
        "Intimidation, CHA",
        "Investigation, INT",
        "Medicine, WIS",
        "Nature, INT",
        "Perception, WIS",
        "Performance, CHA",
        "Persuasion, CHA",
        "Religion, INT",
        "Sleight of hand, DEX",
        "Stealth, DEX",
        "Survival, WIS"
    )
}
