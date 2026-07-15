from Enemy import *
import random


class Zombie(Enemy):

    def __init__(self, healthPoints, attackDamage):
        super().__init__(
            typeOfEnemy="Zombie", healthPoints=healthPoints, attackDamage=attackDamage
        )

    def talk(self):
        print("*Grumbling...*")

    def spreadDisease(self):
        print("The zombie is trying to spread infection")

    def specialAttack(self):
        didSpecialAttackWork = random.random() < 0.50
        if didSpecialAttackWork:
            self.healthPoints += 2
            print("Zombie regenerated 2HP!")
