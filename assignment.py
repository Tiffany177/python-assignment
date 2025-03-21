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
