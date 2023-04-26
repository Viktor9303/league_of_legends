class Meleeminion():
    def __init__(self):
        self.name = "melee minions"
        self.gold = 21
        self.health = 477
        self.health_regen = 67.5
        self.attack_dmg = 12
        self.experience = 75
        self.attack_speed = 1.25
        self.range = 110
        self.armor = 0
        self.magic_resist = 0

        #print("{} has been created".format(self.name))

    def __str__(self):
        return "health: {} attackdmg: {} ".format(self.health,self.attack_dmg)

