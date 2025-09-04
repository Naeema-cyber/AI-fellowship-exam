# QUESTION 1 ANSWER:
# Functiom to add:
def add(a, b):
    return (a + b)
#Function to subtract:
def subtract(a, b):
    return (a - b)
#Function to multiply:
def multiply(a , b):
    return (a * b)
#Function to divide
def divide(a , b):
    if b != 0:
        return a / b
    else:
        print("Number cannot be zero")

try:
    while True:
        choice = input("Select an operation(+, -, *, /) or exit to quit:")
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        if choice == "exit":
            print("Exiting the app")
            break
    
        elif choice == "+":
            print("Result: ", add(num1, num2))
        elif choice == "-":
            print("Result: ", subtract(num1, num2))
        elif choice == "*":
            print("Result:", multiply(num1, num2))
        elif choice == "/":
            print("Result: ", divide(num1, num2))
        else:
            print("Invalid input. Please try again")
    else:
        print("Invalid input")
except ValueError as e:
        print("Invalid choice")
finally:
        print("Continue your program")
            


#QUESTION 2

while True:

    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break       # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")



#QUESTION 3

while True:
    age = (input("Enter your age (or type exit to quit): "))
    if age == exit:
        print("Goodbye!")
        break
    
    try:
        user = int(age)
        if user >= 18:
            print("You can vote")
            continue
        else:
            print("You cannot vote")
    except:
        print("Invalid input")
    finally:
        print("Try again later")




