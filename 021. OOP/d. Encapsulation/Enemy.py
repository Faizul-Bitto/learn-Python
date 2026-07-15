class Enemy:
    typeOfEnemy: str
    healthPoints: int
    attackDamage: int

    def __init__(self, typeOfEnemy, healthPoints, attackDamage):
        self.__typeOfEnemy = typeOfEnemy
        self.healthPoints = healthPoints
        self.attackDamage = attackDamage

    def getTypeOfEnemy(self):
        return self.__typeOfEnemy

    def setTypeOfEnemy(self, typeOfEnemy):
        self.__typeOfEnemy = typeOfEnemy
