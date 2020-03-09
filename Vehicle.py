class Vehicle:

    def __init__(self, passengers, cargo_size):
        self.passengers = passengers
        self.cargo_size = cargo_size

    def accelerate(self):
        return "Accelerating!"

    def decelerate(self):
        return "Breaking!"
