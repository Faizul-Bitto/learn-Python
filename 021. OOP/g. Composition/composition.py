class Engine:
    def start(self):
        print("Engine Started")


class Car:
    def __init__(self):
        self.engine = Engine()  #! Composition

    def drive(self):
        self.engine.start()
        print("Driving...")


car = Car()
car.drive()
