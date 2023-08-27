#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class)

# Example usage:
class Vehicle:
    pass

class Car(Vehicle):
    pass

class Bicycle(Vehicle):
    pass

car_obj = Car()
bicycle_obj = Bicycle()
vehicle_obj = Vehicle()
string = "Hello"

print(is_kind_of_class(car_obj, Car))  # Output: True
print(is_kind_of_class(car_obj, Vehicle))  # Output: True
print(is_kind_of_class(bicycle_obj, Bicycle))  # Output: True
print(is_kind_of_class(bicycle_obj, Vehicle))  # Output: True
print(is_kind_of_class(vehicle_obj, Vehicle))  # Output: True
print(is_kind_of_class(string, str))  # Output: True
print(is_kind_of_class(car_obj, str))  # Output: False
