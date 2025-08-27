# Defining a class
class Car:
    color = "red"  # Attribute
    # Method
    def drive(self):
        print("The car is driving 🚗")

# Creating an object
my_car = Car()
print(my_car.color)
my_car.drive()

# Constructors: The __init__ Method and Instance Variables 

class Car:
    def __init__(self, color, model):
        self.color = color    # Instance variable
        self.model = model    # Instance variable

# Creating objects with unique attributes
car1 = Car("blue", "Sedan")
car2 = Car("red", "SUV")

print(car1.color)  # Output: blue
print(car2.model)  # Output: SUV



# OOP Principles: Inheritance, Polymorphism, and Encapsulation

#Inheritance 

""" 
Just like humans inherit traits from their parents, classes can inherit attributes and methods from other classes. This helps reduce code repetition and create a natural hierarchy in your code!

Example: Imagine a Vehicle class with general features (like wheels). We can create subclasses like Car and Bike that inherit those features!

"""
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Car(Vehicle):
    pass

car = Car(4)
print(car.wheels)  # Output: 4


# Polymorphism

""" 
Derived classes can behave differently for the same method inherited from a base class. With polymorphism, a method name can mean different things across multiple classes.

Example: Imagine a speak() method. Dogs bark(), while cats meow(), even though both use speak()!

"""
  
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Polymorphism in action
for animal in [Dog(), Cat()]:
    print(animal.speak())



#Encapsulation : 

""" 
This is the practice of keeping attributes and methods private to prevent unwanted interference from outside the class. It’s like hiding your chocolate stash  from everyone else!

"""
class SecretStash:
    def __init__(self):
        self.__chocolates = 10  # Private attribute

    def take_chocolate(self):
        if self.__chocolates > 1:
            self.__chocolates -= 1
            print("One chocolate taken!")
        else:
            print("No chocolates left 😢")

stash = SecretStash()
stash.take_chocolate()

