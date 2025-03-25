# Combining Two Objects
# Car -> Brand, Model, Year

class Car:
    def __init__(self, brand, model, year, owner):
        self.brand = brand
        self.model = model
        self.year = year
        self.owner = owner

    def car_detail(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)
        print("Car Year:", self.year)
        print



class Owner:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact 
    
    def owner_info(self):
        print("Owner Name:", self.name)
        print("Owner Address:", self.address)
        print("Owner Contact:", self.contact)
    

owner1 = Owner("Shubham", "Mumbai", 1100012)

car1 = Car("tesla", "Model 3", 2023, owner1)
car1.car_detail()
print(car1.owner.name)


# Accessing and Modifying data
# Two Users
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_message(self, user):
        print(f"Send message to {user.name}: Hii {user.name} this is {self.name}")
    
user1 = User("John", 28)
user2 = User("Shubham", 22)

user1.get_message(user2)