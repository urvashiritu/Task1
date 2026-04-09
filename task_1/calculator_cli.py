import math

# -----------------------------
# Calculator Functions
# -----------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a % b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error: Cannot calculate square root of a negative number."
    return math.sqrt(a)


# -----------------------------
# Main Calculator Program
# -----------------------------

def calculator():
    while True:
        print("\n========== Advanced Calculator ==========")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '8':
            print("Thank you for using the calculator.")
            break

        elif choice == '7':
            try:
                num = float(input("Enter a number: "))
                print("Result:", square_root(num))
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print("Result:", add(num1, num2))

                elif choice == '2':
                    print("Result:", subtract(num1, num2))

                elif choice == '3':
                    print("Result:", multiply(num1, num2))

                elif choice == '4':
                    print("Result:", divide(num1, num2))

                elif choice == '5':
                    print("Result:", modulus(num1, num2))

                elif choice == '6':
                    print("Result:", power(num1, num2))

            except ValueError:
                print("Invalid input! Please enter numeric values.")

        else:
            print("Invalid choice! Please select from 1 to 8.")


# Run calculator
calculator()