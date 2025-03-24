# Print and even numbers from 1 to 10

numbers = range(1, 11)
count = 0
for num in numbers : 
    if(num % 2 == 0):
        print(num)
        count += 1  
    else:
        continue

print(f"We have {count} even numbers")