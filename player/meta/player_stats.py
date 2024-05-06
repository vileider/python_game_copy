from dataclass_and_protocols.statistics import Statistics

class PlayerStats(Statistics):
    def __init__(self):
        self.stats = Statistics(hp = 100,
                        max_hp = 100,
                        mana = 50,
                        max_mana = 50,
                        speed = 1,
                        acceleration = 0.1,
                        max_speed = 10,                    
                        attack =  3,
                        capacity = 100,
                        gold = 100,
                        exp = 0,
                        level = 1,
                        intelligence=1,
                        dexterity=1,
                        strength = 1)
