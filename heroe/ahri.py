import json

class Ahri:
    def __init__(self):
        self.name = "Ahri"
        self.level = 1
        self.q_level = 0
        self.w_level = 0
        self.e_level = 0
        self.r_level = 0


        with open('../conf/json/ahri.json') as f:
            data = json.load(f)
            self.health_min = data['health'][0]
            self.health_max = data['health'][1]
            self.current_health = data['health'][0]
            self.mana_min = data['mana'][0]
            self.mana_max = data['mana'][1]
            self.current_mana = data['mana'][0]

            self.manaregen_min = data['manaregen'][0]
            self.manaregen_max = data['manaregen'][1]
            self.current_manaregen= data['manaregen'][0]

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
            self.q_cost_json = data['abilities'][0]['cost']
            self.q_cost = self.calculate_q_cost()
            self.w_cost_json = data['abilities'][1]['cost']
            self.w_cost = self.calculate_w_cost()
            self.e_cost_json = data['abilities'][2]['cost']
            self.e_cost = self.calculate_e_cost()
            self.r_cost_json = data['abilities'][3]['cost']
            self.r_cost = self.calculate_r_cost()

            print("r cost:",self.r_cost)
            print("w cost:",self.w_cost)
            print("e cost:",self.e_cost)




        print("{}  has been created".format(self.name))

    def level_up(self):
        self.increase_health()
        self.increase_mana()
        self.increase_manaregen()
        self.increase_healthregen()
        self.increase_armor()
        self.increase_attackdamage()
        self.increase_magicresist()
        self.increase_level()

    def calculate_q_cost(self):
        if self.q_level == 0:
            return 0
        if type(self.q_cost_json) == list:
            return self.q_cost_json[self.q_level]
        return self.q_cost_json

    def calculate_w_cost(self):
        if self.w_level == 0:
            return 0
        if type(self.w_cost_json) == list:
            return self.w_cost_json[self.w_level]
        return self.w_cost_json

    def calculate_e_cost(self):
        if self.e_level == 0:
            return 0
        if type(self.e_cost_json) == list:
            return self.e_cost_json[self.w_level]
        return self.e_cost_json

    def calculate_r_cost(self):
        if self.r_level == 0:
            return 0
        if type(self.r_cost_json) == list:
            return self.r_cost_json[self.r_level]
        return self.r_cost_json

    def increase_q_level(self):
        self.q_level += 1

    def increase_w_level(self):
        self.w_level += 1

    def increase_e_level(self):
        self.e_level += 1

    def increase_r_level(self):
        if self.is_increase_r():
            self.r_level += 1

    def is_increase_r(self):
        if self.level >=6 and self.level < 11 and self.r_level == 0:
            return True
        if self.level >= 11 and self.level < 16 and self.r_level < 2:
            return True
        if self.level >=16 and self.r_level <3:
            return True
        return False

    def increase_health(self):
        self.current_health += (self.health_max - self.health_min)/18

    def increase_mana(self):
        self.current_mana += (self.mana_max - self.mana_min)/18

    def increase_manaregen(self):
        self.current_manaregen += (self.manaregen_max - self.manaregen_min)/18

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

    def skill_q(self,enemyList):
        if self.q_level > 0 and self.q_cost < self.current_mana:
            AhriShoot.animateQ()
            self.current_mana -= self.q_cost

    def skill_w(self):
        if self.w_level > 0 and self.w_cost < self.current_mana:
            AhriShoot.animateW()
            self.current_mana -= self.w_cost


    def skill_e(self):
        if self.e_level > 0 and self.e_cost < self.current_mana:
            AhriShoot.animateE()
            self.current_mana -= self.e_cost

    def skill_r(self):
        if self.r_level > 0 and self.r_cost < self.current_mana:
            AhriShoot.animateR()
            self.current_mana -= self.r_cost


    def __str__(self):
        return "level: {} health:{} mana:{} manaregen:{} healthregen:{} armor:{} attackdamage:{} magicresist:{} movespeed:{} attackrange:{}".format(self.level,self.current_health,self.current_mana,
                self.current_manaregen,self.current_health_regen,self.current_armor,self.current_attackdamage,self.current_magicresist,self.move_speed,self.attackrange)

class AhriShoot:

    @staticmethod
    def animateQ():
        print("Q has been shot from Ahri")

    @staticmethod
    def animateW():
        print("W has been shot from Ahri")

    @staticmethod
    def animateE():
        print("E has been shot from Ahri")

    @staticmethod
    def animateR():
        print("R has been shot from Ahri")
































ahri = Ahri()
print(ahri)
ahri.level_up()
print(ahri)

