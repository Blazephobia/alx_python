#!/usr/bin/python3
def inherits_from(obj, a_class):
    return issubclass(type(obj), a_class) and type(obj) is not a_class

# Example usage:
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

class Bird(Animal):
    pass

dog_obj = Dog()
bird_obj = Bird()
mammal_obj = Mammal()
animal_obj = Animal()
string = "Hello"

print(inherits_from(dog_obj, Mammal))  # Output: True
print(inherits_from(dog_obj, Animal))  # Output: True
print(inherits_from(bird_obj, Animal))  # Output: True
print(inherits_from(bird_obj, Mammal))  # Output: False
print(inherits_from(mammal_obj, Animal))  # Output: True
print(inherits_from(animal_obj, Animal))  # Output: False
print(inherits_from(string, str))  # Output: False
print(inherits_from(dog_obj, str))  # Output: False
