from Vehicle import *


class Bike(Vehicle):

    def __init__(self, brand, color):
        super().__init__(typeOfVehicle="Bike", brand=brand, color=color)

    def displayInfo(self):
        print(f"Bike -> Brand : {self.brand}, Color: {self.color}")
