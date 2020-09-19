from Fortuna import smart_clamp


class CR:
    """ The CR class is a numeric system representing the relative power of a monster in D&D 5e.
    This system is a bit funky with values below 1, be careful... here be dragons!
    CR less than 1 are printed as fractions but valued mathematically as integers [-3, 0].
    CR(-3) is CR 1/16 - same as CR 0 in the books.
    CR(-2) is CR 1/8
    CR(-1) is CR 1/4
    CR(0) is CR 1/2
    CR(1)..CR(30) is CR 1 to CR 30
    Why is this system so crazy? Because wizards are bad at math!
    And I wanted to ignore the fractions...
    So that subtracting 1 always takes you to the next CR down.
    Currently: CR(1) + CR(1) is CR(2)
    what is CR 1/2 + CR 1/4 ???
    This is an open question! It may cause me to switch to floats internally, eww.
    """

    def __init__(self, val):
        self.val = smart_clamp(val, -3, 30)

    @property
    def value(self):
        return self.val

    @property
    def key(self):
        return self.val + 3

    @property
    def string(self):
        if self.val > 0:
            str_cr = f"{self.val}"
        else:
            str_cr = ("1/16", "1/8", "1/4", "1/2")[self.key]
        return f"CR {str_cr}"

    @property
    def tier(self):
        return (
            1, 1, 1, 1,
            1, 1, 1, 1, 1,
            2, 2, 2, 2, 2,
            3, 3, 3, 3, 3,
            4, 4, 4, 4, 4,
            4, 4, 4, 4, 4,
            4, 4, 4, 4, 4,
        )[self.key]

    @classmethod
    def party_adapter(cls, average_level, num_players=5, difficulty=0):
        average_level = smart_clamp(average_level, 1, 20)
        num_players = smart_clamp(num_players, 1, 9) - 5
        magic_bonus = (0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4)[average_level]
        diff_modifier = smart_clamp(difficulty, -5, 5)
        return CR(num_players + average_level + magic_bonus + diff_modifier)

    def __repr__(self):
        return self.string

    def __add__(self, other):
        self.val = smart_clamp(self.val + other, -3, 30)
        return self

    def __sub__(self, other):
        self.val = smart_clamp(self.val - other, -3, 30)
        return self


if __name__ == "__main__":
    for i in range(-3, 31):
        cr = CR(i)
        print(f"{cr}, Tier: {cr.tier}")
