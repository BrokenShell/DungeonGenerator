from Fortuna import *
from DungeonGenerator.npc_lib import npc_dict


class SkillSet:

    def __init__(self, level, prof_bonus, abilities, background):
        self.skills = set()
        for ability, score in abilities.items():
            if score > 10:
                skill_bonus = prof_bonus + (score - 10) // 2
                for _ in range(-1, level // 4):
                    if skill_bonus > 0 and percent_true(score * 2):
                        self.skills.add(f"{random_value(npc_dict['skills'][ability])} {skill_bonus}")
        for skill in background.skills:
            ability = skill[-3:]
            if ability in ("STR", "DEX", "CON", "INT", "WIS", "CHA"):
                score = abilities[ability]
                self.skills.add(skill + f" {prof_bonus + (score - 10) // 2}")

    def __repr__(self):
        return ", ".join(self.skills)
