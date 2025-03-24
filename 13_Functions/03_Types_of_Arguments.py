# Types of Arguments

# Positional Arguments
def add(a, b):
    return a+b

print(add(5, 5))

# Keyword Argument
def greet(f_name, last_name):
    print(f"Hello, {f_name} {last_name}")

greet(f_name= "Shubham", last_name="Yeram")

# Default Argument

def welcome(name="User"):
    print(f"Hello {name}")

welcome()


# Variable-length arguments

def totalSum(*number):
    return sum(number)

print(totalSum(1, 2, 3, 4, 5))