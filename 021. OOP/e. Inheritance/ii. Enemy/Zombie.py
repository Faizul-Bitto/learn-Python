from Enemy import *


class Zombie(Enemy):

    def __init__(self, healthPoints, attackDamage):
        super().__init__(
            typeOfEnemy="Zombie",
            healthPoints=healthPoints,
            attackDamage=attackDamage,
        )

    def talk(self):
        print("*Grumbling...*")

    def spreadDisease(self):
        print("The zombie is trying to spread infection")
