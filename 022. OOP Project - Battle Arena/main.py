from Zombie import *
from Ogre import *


def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.healthPoints > 0 and e2.healthPoints > 0:
        print("______")
        e1.specialAttack()
        e2.specialAttack()
        print(f"{e1.getTypeOfEnemy()} : {e1.healthPoints} HP left")
        print(f"{e2.getTypeOfEnemy()} : {e2.healthPoints} HP left")
        e2.attack()
        e1.healthPoints -= e2.attackDamage
        e1.attack()
        e2.healthPoints -= e1.attackDamage

    print("______")

    if e1.healthPoints > 0:
        print(f"{e1.getTypeOfEnemy()} wins")
    else:
        print(f"{e2.getTypeOfEnemy()} wins")


zombie = Zombie(30, 1)
ogre = Ogre(20, 3)

battle(zombie, ogre)
