"""CP1404 Prac 9 - Taxi tests for cars."""
from prac_09.taxi import Taxi

# 1.
my_taxi = Taxi("Prius 1", 100)

# 2.
my_taxi.drive(40)

# 3.
print(f"{my_taxi}, Current fare ${my_taxi.get_fare()}")

# 4.
my_taxi.start_fare()
my_taxi.drive(100)

# 5.
print(f"{my_taxi}, Current fare ${my_taxi.get_fare()}")
