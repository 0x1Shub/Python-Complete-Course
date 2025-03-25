# # Create a Simple Class of Person
# # Create a class Person with:
# # Attributes: name, age
# # Method: display_info() – Prints the name and age.

# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# user1 = Person("John", "24")
# user1.display_info()


# # Define a class Car with:
# # Attributes: brand, model, year
# # Method: car_info() – Prints car details.

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def car_info(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Year:", self.year)

# car1 = Car("Tesla", "Model 3", 2022)
# car1.car_info()

# car2 = Car("Ford", "Mustang", 2021)
# car2.car_info()


# Intermediate Level 

class BankAccount():

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Money Credited:", amount)
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Money Debited:", amount)
        else:
            print("Not sufficient balance")
        
    def get_balance(self):
        print("Balance :", self.balance)


account1 = BankAccount(123, 0)
account1.withdraw(10000)
account1.get_balance()
