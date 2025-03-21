# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.
# Note: Upload the code to GitHub and submit the GitHub link


print("Welcome to Tiffany's Calculator.")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operator = input("Enter the operator: ")

# operators +, -, *, /

if operator == "+":
    print(f"{number1} + {number2} = {number1 + number2}")
elif operator == "-":
    print(f"{number1} - {number2} = {number1 - number2}")
elif operator == "*":
    print(f"{number1} * {number2} = {number1 * number2}")
elif operator == "/":
    if number2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"{number1} / {number2} = {number1 / number2}")
else:
    print("Invalid operator. Please use +, -, *, or /.")
