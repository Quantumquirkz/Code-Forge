"""
Exercise: Simple Calculator
Description: Create a calculator that performs basic operations like addition, subtraction, multiplication, and division.
Author: Jhuomar Barria
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Division by zero is not allowed!")
    return a / b

def power(a, b):
    """Raise a to the power of b"""
    return a ** b

def modulo(a, b):
    """Return the remainder of a divided by b"""
    if b == 0:
        raise ValueError("Modulo by zero is not allowed!")
    return a % b

def display_menu():
    """Display the calculator menu"""
    print("\n=== Simple Calculator ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulo (%)")
    print("7. Exit")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '7':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice! Please try again.")
            continue
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            result = None
            operation = ""
            
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            elif choice == '5':
                result = power(num1, num2)
                operation = "^"
            elif choice == '6':
                result = modulo(num1, num2)
                operation = "%"
            
            print(f"\nResult: {num1} {operation} {num2} = {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

