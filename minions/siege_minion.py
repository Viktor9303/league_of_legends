class Siegeminion():
    def __init__(self):
        self.name = "siege minion"
        self.gold = 60
        self.health = 912
        self.attack_dmg = 41
        self.experience = 116
        self.attack_speed = 1.00
        self.range = 300
        self.armor = 0
        self.magic_resist = 0

        #print("{} has been created".format(self.name))

    def __str__(self):
        return "health: {} attackdmg: {} ".format(self.health,self.attack_dmg)

