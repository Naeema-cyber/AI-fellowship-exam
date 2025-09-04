# AI_ENGINEERING EXAMS
Question 1
Write a Python program that works as a basic calculator with continuous use.

Instruction

The program should repeatedly allow the user to perform operations until they choose to exit.
Ask the user to enter two numbers.
Then ask them to choose an operation: addition, subtraction, multiplication, or division.
Use functions to define each operation.
Use try-except to handle invalid input and division by zero.
Use control flow (if-elif-else) to select the correct operation.
Use a while loop to keep running until the user chooses to exit.



Question 2
Complete the missing parts of the program below so that it keeps asking the user for a number and tells whether it is even or odd.
Instruction

Use input, int conversion, if-else control flow, and print output.
Use a while loop that runs until the user types 'exit'.
while ____
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit"__
        print("Goodbye!")
        ______        # break out of loop
    
    num = __________(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is ______")
    ___
        print("The number is ______")


Question 3
The following code is supposed to ask for a user’s age repeatedly and say whether they are allowed to vote (18+).
It should also exit if the user types 'exit'. However, the code contains errors.
while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == exit:
        print("Goodbye!")
        break
    
    try:
        if age >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input")
