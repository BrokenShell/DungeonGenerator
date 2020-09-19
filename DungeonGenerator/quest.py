from Fortuna import *
from DungeonGenerator.dungeon import Dungeon, Wilderness, Settlement
from DungeonGenerator.npc import Npc
from DungeonGenerator.treasure import magic_table_by_cr, get_villain_loot, Loot
from DungeonGenerator.utilities import cr_adapter
from DungeonGenerator.quest_lib import things_dict


class Quest:
    trinkets = TruffleShuffle(things_dict['trinkets'])
    actions = TruffleShuffle(things_dict["actions"])
    skills = TruffleShuffle(things_dict["skills"])

    def __init__(self, cr, dungeon_name=None, dungeon_size=4, wilderness_size=1, settlement_size=1):
        self.cr = smart_clamp(cr, -3, 30)
        self.npc = Npc(self.cr)
        self.race = self.npc.race
        self.appearance = self.npc.appearance
        self.mannerism = self.npc.mannerism
        self.background = self.npc.background
        self.objective = self.trinkets() if percent_true(50) else self.actions()
        self.skill = self.skills()
        self.wilderness = Wilderness(self.cr, num_levels=wilderness_size, areas_per_level=10)
        self.dungeon_name = dungeon_name
        self.dungeon = Dungeon(self.cr + wilderness_size, dungeon_name, dungeon_levels=dungeon_size)
        self.reward = get_villain_loot(self.dungeon.threats[-1].threat.cr)
        self.reward.magic_items.append(magic_table_by_cr(self.cr))
        self.dc = self.dungeon.threats[-1].threat.save_dc
        self.city = Settlement(cr=self.cr, num_people=settlement_size*10)
        self.total_xp = self.dungeon.total_xp + self.wilderness.total_xp
        self.summary = '\n'.join((
            f"NPC: Primary Quest Giver",
            f"Race: {self.race}",
            f"Appearance: {self.appearance}",
            f"Mannerism: {self.mannerism}",
            f"Background: {self.background}",
            f"",
            f"Quest Details:",
            f"Starting Location: {self.city.name}",
            f"Objective: {self.objective}.",
            f"Location: Beyond the {self.wilderness.name}, deep inside the {self.dungeon.name}.",
            f"Primary Villain: {self.dungeon.threats[-1].threat.name}",
            f"Quest Skill Check: {self.skill} {self.dc}",
            f"Reward: {self.reward}",
            f"",
        ))
        self.total_treasure = sum((
            self.dungeon.total_treasure,
            self.wilderness.total_treasure,
            self.city.total_treasure,
            self.reward,
        ), Loot())

    def __repr__(self):
        output = (
            f"{self.summary}",
            f"{self.city}",
            f"{self.wilderness}",
            f"{self.dungeon}",
        )
        return '\n'.join(output)


if __name__ == "__main__":
    print("")
    quest = Quest(
        cr=cr_adapter(num_players=5, average_level=5, difficulty=0),
    )
    print(quest)
    print(quest.dungeon)
