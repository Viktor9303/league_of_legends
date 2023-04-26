class Casterminion():
    def __init__(self):
        self.name = "caster minion"
        self.gold = 14
        self.health = 296
        self.attack_dmg = 24
        self.experience = 75
        self.attack_speed = 0.667
        self.range = 550
        self.armor = 0
        self.magic_resist = 0
        #print("{} has been created".format(self.name))

    def __str__(self):
        return "health: {} attackdmg: {} ".format(self.health,self.attack_dmg)

