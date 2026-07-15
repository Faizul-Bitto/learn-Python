class Vehicle:

    def __init__(self, typeOfVehicle, brand, color):
        self.__typeOfVehicle = typeOfVehicle
        self.brand = brand
        self.color = color

    def vehicleType(self):
        print(f"Vehicle type : {self.__typeOfVehicle}")

    def vehicleStart(self):
        print(f"Engine of the {self.brand}'s {self.__typeOfVehicle} starts.")

    def vehicleStop(self):
        print(f"Engine of the {self.brand}'s {self.__typeOfVehicle} stops.")

    def displayInfo(self):
        print(f"Brand : {self.brand}, Color : {self.color}")
