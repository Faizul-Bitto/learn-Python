class Enemy:
    typeOfEnemy: str
    healthPoints: int = 100
    attackDamage: int = 1

    def talk(self):
        print(f"I am a {self.typeOfEnemy}. Be prepared for fight.")

    def walkForward(self):
        print(f"{self.typeOfEnemy} moves closer to you.")

    def attack(self):
        print(f"{self.typeOfEnemy} attacks for {self.attackDamage} damage.")
