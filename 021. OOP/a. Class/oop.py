from Enemy import *

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.typeOfEnemy = "Zombie"

print(
    f"{enemy1.typeOfEnemy} has {enemy1.healthPoints} health points and can make an attack of {enemy1.attackDamage} damage"
)
