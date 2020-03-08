from Vehicles.Vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, passengers, cargo_size, brand, horsepower, max_speed):
        super(Car, self).__init__(passengers=passengers, cargo_size=cargo_size)
        self.brand = brand
        self.horsepower = horsepower
        self.max_speed = max_speed

    def park(self):
        return "Parking!"

    def honk(self):
        return "Honk honk!"
