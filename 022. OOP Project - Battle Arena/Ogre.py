from Enemy import *
import random


class Ogre(Enemy):

    def __init__(self, healthPoints, attackDamage):
        super().__init__(
            typeOfEnemy="Ogre", healthPoints=healthPoints, attackDamage=attackDamage
        )

    def talk(self):
        print("Ogre is slamming hands all around!")

    def specialAttack(self):
        didSpecialAttackWork = random.random() < 0.20
        if didSpecialAttackWork:
            self.attackDamage += 4
            print("Ogre gets angry and increases attack by 4!")
