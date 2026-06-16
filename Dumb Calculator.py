def add(x, y):
    return x + y
    

def subtract(x, y):
    return x - y
    

def multiply(x, y):
    return x * y
    

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y
    

print("Welcome to Dumb Calculator")
x = float(input("Enter your first number: "))
y = float(input("Enter your second number:"))

print("Please select which of the following arithematic operation you want me to perform-\n" 
        "1. Add\n" 
        "2. Subtract\n" 
        "3. Multiply\n" 
        "4. Divide\n")


operation = int(input("Enter your Choice: "))

if operation == 1:
    add(x, y)
    print("Addtion is", x+y)
elif operation == 2:
    subtract(x, y)
    print("Subtraction is", x+y)
elif operation == 3:
    multiply(x, y)
    print("Multiplication is", x+y)
elif operation == 4:
    divide(x, y)
    print("Division is", x+y)
else:
    print("You dumb bitch enter valid input")



    