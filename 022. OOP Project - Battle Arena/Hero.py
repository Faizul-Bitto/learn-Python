from Weapon import *


class Hero:

    def __init__(self, healthPoints, attackDamage):
        self.healthPoints = healthPoints
        self.attackDamage = attackDamage
        self.isWeaponEquipped = False
        self.weapon: Weapon = None

    def equipWeapon(self):
        if self.weapon is not None and not self.isWeaponEquipped:
            self.attackDamage += self.weapon.attackIncrease
            self.isWeaponEquipped = True
