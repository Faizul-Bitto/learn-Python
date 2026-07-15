class Enemy:
    typeOfEnemy: str
    healthPoints: int
    attackDamage: int

    def __init__(self, typeOfEnemy, healthPoints, attackDamage):
        self.typeOfEnemy = typeOfEnemy
        self.healthPoints = healthPoints
        self.attackDamage = attackDamage
