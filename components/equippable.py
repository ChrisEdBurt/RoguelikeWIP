class Equippable:
    def __init__(self, slot, strength_bonus=0, intelligence_bonus = 0, defense_bonus=0, max_hp_bonus=0):
        self.slot = slot
        self.strength_bonus = strength_bonus
        self.intelligence_bonus = intelligence_bonus
        self.defense_bonus = defense_bonus
        self.max_hp_bonus = max_hp_bonus