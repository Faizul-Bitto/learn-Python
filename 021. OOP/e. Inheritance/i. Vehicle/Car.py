from Vehicle import *


class Car(Vehicle):

    def __init__(self, brand, color):
        super().__init__(typeOfVehicle="Car", brand=brand, color=color)

    def displayInfo(self):
        print(f"Car -> Brand : {self.brand}, Color: {self.color}")
