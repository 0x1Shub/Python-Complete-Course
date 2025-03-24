# Write a program for weight converter from Kilogram to Pounds

weight = input("Enter your weight: ")
uint = input("(K)g or (L)bs: ")

if uint.upper() == 'L':
    weight_converter = float(weight) * 2.205
    print("Weight in Pounds: " + str(weight_converter))
elif uint.upper() == 'K':
    weight_converter = float(weight) / 2.205
    print("Weight is Kilogram:" + str(weight_converter))

print("Conversion Completed")