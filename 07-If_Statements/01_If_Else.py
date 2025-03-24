temperature = 25

if temperature > 30 :
    print("It's a hot day")
    print("Stay hydrated")
elif temperature > 20: #(20, 30] greater than 20 but less than and equal to 30
    print("It's nice day")
elif temperature > 10: #(10, 20] greater than 10 but less than and equal to 20
    print("It's a cold day")
else :
    print("It's very cold day")
print("Done")