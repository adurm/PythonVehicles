from Vehicles.Vehicle import Vehicle


class Plane(Vehicle):

    def __init__(self, passengers, cargo_size):
        super(Plane, self).__init__(passengers=passengers, cargo_size=cargo_size)

    def take_off(self):
        return "Taking off!"

    def touch_down(self):
        return "Touching down!"