# Procedural vs OOP

# Procedural
car_brand = 'Toyota'
car_model = 'Corolla'

def drive(brand, model):
  print(f"{brand} {model} is driving!")

drive(car_brand, car_model)

# OOP

class Car:

  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def drive(self):
    print(f"{self.brand} {self.model} is driving!")

my_car = Car('Toyota', 'Corolla')
my_car.drive()



# 1. Encapsulation

# Encapsulation means hiding details using private or protected attributes.

class BankAccount:
  def __init__(self, balance):
   self.__balance = balance
  def deposit(self, amount):
    self.__balance += amount
  def get_balance(self):
    return self.__balance
  
  
# 2. Inheritance

# Inheritance allows a class to reuse code from another class.

class Animal:
  def speak(self):
    print('This animal makes a sound.')

class Dog(Animal):
  def speak(self):
    print('Woof! Woof!')

class Cat(Animal):
  def speak(self):
    print('Meow! Meow!')
    
#Polymorphism

# Polymorphism allows the same method name to behave differently.

for animal in [Dog(), Cat()]:
 animal.speak()



# Abstraction

# Abstraction forces subclasses to implement methods (using abc module).

from abc import ABC, abstractmethod

class Shape(ABC):
 @abstractmethod
 def area(self):
    pass

class Square(Shape):
  def __init__(self, side):
    self.side = side
  def area(self):
    return self.side * self.side

sq = Square(4)
print(sq.area())


