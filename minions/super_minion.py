class Superminion():
    def __init__(self):
        self.name = "super minion"
        self.gold = 60
        self.health = 1600
        self.health_regen = 67.5
        self.attack_dmg = 240
        self.experience = 116
        self.attack_speed = 0.85
        self.range = 170
        self.armor = 100
        self.magic_resist = -30

        #print("{} has been created".format(self.name))

    def __str__(self):
        return "health: {} attackdmg: {} ".format(self.health,self.attack_dmg)


