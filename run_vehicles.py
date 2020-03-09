from Vehicles.Car import *
from Vehicles.Plane import *

vehicle1 = Vehicle(6, 20)
vehicle2 = Vehicle(2, 10)

print("Vehicle Tests")
print(vehicle1.accelerate())
print(vehicle2.decelerate())
print("Passengers:", vehicle1.passengers)
print("Cargo Size:", vehicle2.cargo_size)
print("\n")

car1 = Car(4, 10, "Toyota", 500, 160)
car2 = Car(2, 0, "Ferrari", 1000, 400)

print("Car Tests")
print(car1.accelerate())
print(car1.decelerate())
print(car2.park())
print(car2.honk())
print("\n")

plane1 = Plane(200, 1000)
plane2 = Plane(2, 10)

print("Plane Tests")
print(plane1.accelerate())
print(plane1.decelerate())
print(plane2.take_off())
print(plane2.touch_down())
print("\n")
