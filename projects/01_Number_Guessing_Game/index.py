# Number Guessing Game
# Random Number Generation
# Give hints higher and lower
# Limit the number of attempts

import random;

number = random.randint(1, 50)

def guess_number():
    count = 5
    i = 1
    while i<=count:
        x = int(input("Guess the Number: ", ))
        if x==number:
            return print(f"You guessed correct output: {number}")
        elif x > number:
            print("Too high! Try a lower number.")
        elif x< number:
            print("Too low! Try a higher number.")
        i += 1

    if i > count :
        print("Time out, you have only 5 attempts")


guess_number()