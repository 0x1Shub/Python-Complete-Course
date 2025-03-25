name = "Shubham"
age = 22

print(type(name))
print(type(age))


# Class Creation
class Car:

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def color(self):
        print("red")

# Object Creation for variable name car
car1 = Car("BMW", "Q8")
car1.color() # access methods on objects
print(car1.name)
print(car1.model)

