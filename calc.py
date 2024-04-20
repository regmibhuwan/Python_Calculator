#first define what function you want to use
#for every function give two default parameters, x and y
#ask to user what function they want to perform
#get two numbers as well from the user based on their choice
#perform the action with conditions which meets the function requirements 
#give output 

def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    if y == 0:
        print("Invalid Error!")
    else:
        return x/y
    
    print("Select Operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter the first number:  "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        print("Result: ", add(num1, num2))

    elif choice == 2:
        print("Result: ", subtract(num1, num2))

    elif choice == 3:
        print("Result: ", multiply(num1, num2))

    elif choice == 4:
        print("Result: ", divide(num1, num2))

    else:
        print("Invalid Error!")
