from minions.melee_minion import *
from minions.siege_minion import *
from minions.melee_minion import *
from minions.super_minion import *
from minions.caster_minion import *

#1 super 2 caster minions
class FieldA:
    def __init__(self):
        superminion = Superminion()
        caster1 = Casterminion()
        caster2 = Casterminion()

        self.minions = [superminion,caster1, caster2]
        self.show_minions()

    def show_minions(self):
        for minion in self.minions:
            print(minion)

#1 super 8 caster minions
class FieldB:
    def __init__(self):
        superminion = Superminion()
        caster1 = Casterminion()
        caster2 = Casterminion()
        caster3 = Casterminion()
        caster4 = Casterminion()
        caster5 = Casterminion()
        caster6 = Casterminion()
        caster7 = Casterminion()
        caster8 = Casterminion()

        self.minions = [superminion,caster1,caster2,caster3,caster4,caster5,caster6,caster7,caster8]
        self.show_minions()

    def show_minions(self):
        for minion in self.minions:
            print(minion)
#1super 3 melee
class FieldC:
    def __init__(self):
        superminion = Superminion()
        melee1 = Meleeminion()
        melee2 = Meleeminion()
        melee3 = Meleeminion()

        self.minions = [superminion,melee1,melee2,melee3]
        self.show_minions()

    def show_minions(self):
        for minion in self.minions:
            print(minion)


#5caster
class FieldD:
    def __init__(self):
        caster1 = Casterminion()
        caster2 = Casterminion()
        caster3 = Casterminion()
        caster4 = Casterminion()
        caster5 = Casterminion()

        self.minions = [caster1,caster2,caster3,caster4,caster5]
        self.show_minions()

    def show_minions(self):
        for minion in self.minions:
            print(minion)
