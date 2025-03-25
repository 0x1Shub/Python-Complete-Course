# Basic Calculator
# Input Valiation
# Add, Multiply, Substract, Divide
# Exceptional Handling
# different function for different operators

result = 0

try: 
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
except ValueError:  # Value Error is type of error if I provide invalid value
    print("Error: Please enter valid numbers")


def add(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1*num2

def divide(num1, num2):
    try:
        return num1/num2 
    except ZeroDivisionError: # Zero Division Error occurs when the any number is divide by 0
        print("Error: Division by zero is not possible")


print("\nSelect an operation")
print("1. Add")
print("2. Subtract")
print("3. Multiplication")
print("4. Division")

operation = int(input("Enter the desired operation for calculation. 1/2/3/4: "))

# Created a dictionary for storing key-value pair for efficient retrieval
calculations = {
    1: add,
    2: subtraction,
    3: multiplication,
    4: divide
}

if operation in calculations:
    result = calculations[operation](num1, num2)
    print(f"Result is: {result}")
else:
    print("Error: Invalid operation selected")
