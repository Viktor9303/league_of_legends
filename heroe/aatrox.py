import json
class Aatrox:
    def __init__(self):
        self.name = "Aatrox"
        self.level = 1
        with open('../conf/json/ahri.json') as f:
            data = json.load(f)
            self.health_min = data['health'][0]
            self.health_max = data['health'][1]
            self.current_health = data['health'][0]

            self.health_regen_min = data['healthregen'][0]
            self.health_regen_max = data['healthregen'][1]
            self.current_health_regen = data['healthregen'][0]

            self.armor_min = data['armor'][0]
            self.armor_max = data['armor'][1]
            self.current_armor = data['armor'][0]

            self.attackdamage_min = data['attackdamage'][0]
            self.attackdamage_max = data['attackdamage'][1]
            self.current_attackdamage = data['attackdamage'][0]

            self.magicresist_min = data['magicresist'][0]
            self.magicresist_max = data['magicresist'][1]
            self.current_magicresist = data['magicresist'][0]

            self.move_speed = data['movespeed']
            self.attackrange = data['attackrange']
        print("{}  has been created".format(self.name))

    def level_up(self):
        self.increase_health()
        self.increase_healthregen()
        self.increase_armor()
        self.increase_attackdamage()
        self.increase_magicresist()
        self.increase_level()

    def increase_health(self):
        self.current_health += (self.health_max - self.health_min)/18

    def increase_healthregen(self):
        self.current_health_regen += (self.health_regen_max - self.health_regen_min)/18

    def increase_armor(self):
        self.current_armor += (self.armor_max - self.armor_min)/18

    def increase_attackdamage(self):
        self.current_attackdamage += (self.attackdamage_max - self.attackdamage_min)/18

    def increase_magicresist(self):
        self.current_magicresist += (self.magicresist_max - self.magicresist_min)/18

    def increase_level(self):
        if self.level < 18:
            self.level += 1

    def skill_q(self):
        pass

    def skill_w(self):
        pass

    def skill_e(self):
        pass

    def skill_r(self):
        pass

    def __str__(self):
        return "level: {} health:{} healthregen:{} armor:{} attackdamage:{} magicresist:{} movespeed:{} attackrange:{}".format(self.level,self.current_health,
                self.current_health_regen,self.current_armor,self.current_attackdamage,self.current_magicresist,self.move_speed,self.attackrange)

aatrox = Aatrox()
print(aatrox)
aatrox.level_up()
print(aatrox)
