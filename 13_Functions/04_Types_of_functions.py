# 1. Perform Task function
# 2. Return Value function

# Perform task function and prints the value
def greet(f_name):
    print(f"Hello, {f_name}")

greet("Shubham")

print(greet("Yeram")) # This will give by default None output because the functions doesn't return any value


# Return Value function
def get_greeting(f_name):
    return f"Hello, {f_name}"

message = get_greeting("Shubham")
file = open('content.txt', 'r+')
file.write("Welcome here shubham")

file.seek(0)

content = file.read()
print(content)

file.close()


# Using With Open The syntax is a cleaner and safer way to handle files. It automatically closes the file when you're done

with open('content.txt', 'r+') as file:
    file.write("Welcome here Shubham")
    file.seek(0)
    content = file.read()

print(content)