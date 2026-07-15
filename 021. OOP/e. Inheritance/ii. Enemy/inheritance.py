from Zombie import *
from Ogre import *

zombie = Zombie(10, 1)

print(
    f"{zombie.getTypeOfEnemy()} has {zombie.healthPoints} health points and can do attack of {zombie.attackDamage}"
)

zombie.talk()
zombie.walkForward()
zombie.attack()
zombie.spreadDisease()

ogre = Ogre(20, 3)
print(
    f"{ogre.getTypeOfEnemy()} has {ogre.healthPoints} health points and can do attack of {ogre.attackDamage}"
)

ogre.talk()
