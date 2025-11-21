"""CP1404 Prac 9 - Testing Unreliable Car class"""

from unreliable_car import UnreliableCar

good_car = UnreliableCar("Ford - reliable", 100, 95)
bad_car = UnreliableCar("Holden - not reliable", 100, 5)

for i in range(1, 20):
    print(f"Distance: {i}km")
    print(f"{good_car.name:22} drove {good_car.drive(i)}km")
    print(f"{bad_car.name:22} drove {bad_car.drive(i)}km")
