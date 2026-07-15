class Enemy:

    def __init__(self, typeOfEnemy, healthPoints, attackDamage):
        self.__typeOfEnemy = typeOfEnemy
        self.healthPoints = healthPoints
        self.attackDamage = attackDamage

    def talk(self):
        print(f"I am a {self.__typeOfEnemy}. Be prepared to fight!")

    def walkForward(self):
        print(f"{self.__typeOfEnemy} moves closer to you")

    def attack(self):
        print(f"{self.__typeOfEnemy} attacks for {self.attackDamage} damage")

    def getTypeOfEnemy(self):
        return self.__typeOfEnemy

    def specialAttack(self):
        print("Enemy has no special attack!")

    