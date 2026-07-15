from Enemy import *


class Ogre(Enemy):

    def __init__(self, healthPoints, attackDamage):
        super().__init__(
            typeOfEnemy="Ogre", healthPoints=healthPoints, attackDamage=attackDamage
        )

    def talk(self):
        print("Ogre is slamming hands all around!")
