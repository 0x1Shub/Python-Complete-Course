# Tuple is similar to List we used to stored the sequence of objects but tuples are immutable
# Tuple elements stored in parenthesis ()

numbers = (1, 2, 3, 3, 3, 4, 5)
print(numbers[0])

# numbers[0] = 15
# print(numbers) # This will give me error because tuples are immutable

print(numbers.count(3)) # Count method is used to count particular element in tuples
