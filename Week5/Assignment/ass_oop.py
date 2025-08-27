# OOP Assignment
""" 
Assignment 1: Design Your Own Class! 

- Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
- Add attributes and methods to bring the class to life!
- Use constructors to initialize each object with unique values.
- Add an inheritance layer to explore polymorphism or encapsulation.

"""
# Step 1: Define the base class
class Smartphone:
    def __init__(self, brand, model, color):

        self.brand = brand
        self.model = model
        self.color = color
        self.battery = 100  # Start with full battery
        self.is_on = False

    def power_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} is now ON.")

    def call(self, number):
        if self.is_on:
            print(f"Calling {number}...")
        else:
            print("Phone is off! Turn it on first.")

    def info(self):
        print(f" {self.brand} {self.model} ({self.color}) - Battery: {self.battery}%")


# Step 2: Inheritance - Create a child class
class Smartwatch(Smartphone):
    def __init__(self, brand, model, color, strap_color):
        super().__init__(brand, model, color)  # Reuse parent constructor
        self.strap_color = strap_color

    # Polymorphism: Override the info() method
    def info(self):
        print(f" {self.brand} {self.model} Watch ({self.color}) with {self.strap_color} strap - Battery: {self.battery}%")


# Step 3: Create objects (instances)
phone = Smartphone("Apple", "iPhone", "Silver")
watch = Smartwatch("Samsung", "Galaxy Watch", "Black", "Blue")

# Step 4: Use the objects
phone.info()        #  Apple iPhone (Silver) - Battery: 100%
phone.power_on()    # Apple iPhone is now ON.
phone.call("123-456-7890")


watch.info()        #  Samsung Galaxy Watch Watch (Black) with Blue strap - Battery: 100%
watch.power_on()    # Samsung Galaxy Watch is now ON.
watch.call("999")

""" 
Activity 2: Polymorphism Challenge! 

Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving", while Plane.move() prints "Flying" ).

"""

# Step 1: Define a base class
class Vehicle:
    def move(self):
        pass  # Placeholder - each child will override this


# Step 2: Create child classes that override move() differently
class Car(Vehicle):
    def move(self):
        print("The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing on the water.")

class Bicycle(Vehicle):
    def move(self):
        print("The bicycle is pedaling down the path.")


# Step 3: Use the vehicles in a loop (demonstrates polymorphism)
def demonstrate_movement(vehicles):
    print("Let's see how each vehicle moves:")
    print("-" * 40)
    for vehicle in vehicles:
        vehicle.move()  # Same method name, different behavior!


# Step 4: Create objects
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

# Step 5: Make them move!
vehicles = [car, plane, boat, bicycle]
demonstrate_movement(vehicles)