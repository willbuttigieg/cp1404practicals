"""CP1404 Prac 9 SilverServiceTaxi Test"""

from prac_09.silver_service_taxi import SilverServiceTaxi

this_taxi = SilverServiceTaxi("this_taxi", 200, 2.0)
this_taxi.drive(18)
print(f"${this_taxi.get_fare():.2f}")

# Test for fanciness of 1
gold_taxi = SilverServiceTaxi("Gold", 200, 1.0)
gold_taxi.drive(10)
assert gold_taxi.get_fare() == round(1.23 * 1 * 10 + 4.5, 1)

# Test for fanciness of 2
silver_taxi = SilverServiceTaxi("Silver", 200, 2.0)
silver_taxi.drive(18)
assert silver_taxi.get_fare() == round(1.23 * 2 * 18 + 4.5, 1)

# Test for fanciness of 6
bronze_taxi = SilverServiceTaxi("Bronze", 200, 6.0)
bronze_taxi.drive(22)
assert bronze_taxi.get_fare() == round(1.23 * 6 * 22 + 4.5, 1)

print("If you see this, all is well.")

