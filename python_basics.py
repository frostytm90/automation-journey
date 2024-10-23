# Functions recap
def greet(name):
    print(f"Hello, {name}!")

greet("TM")

# Loops recap
for i in range(1, 10):
    print(f"Number: {i}")

count = 0
while count < 7:
    print(f"Count: {count}")
    count += 1

# Conditional recap
number = 12
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Classes rerap
class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
    
    def start(self):
        print(f"The {self.color} {self.year} {self.model} car is for sale!")

my_car = Car("purple", "Toyota", 1999)
my_car.start()
