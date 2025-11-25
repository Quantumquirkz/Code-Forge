"""
Exercise: Fibonacci Sequence
Description: Implement a function that generates the Fibonacci sequence up to a given number.
Author: Jhuomar Barria
"""

def fibonacci_iterative(n):
    """Generate Fibonacci sequence using iterative approach"""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    
    return fib

def fibonacci_recursive(n):
    """Get nth Fibonacci number using recursion"""
    if n <= 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_generator(n):
    """Generate Fibonacci sequence using generator (memory efficient)"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def fibonacci_up_to(limit):
    """Generate Fibonacci numbers up to a given limit"""
    fib = []
    a, b = 0, 1
    while a <= limit:
        fib.append(a)
        a, b = b, a + b
    return fib

def is_fibonacci_number(num):
    """Check if a number is a Fibonacci number"""
    # A number is Fibonacci if one of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square
    import math
    
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x
    
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

def main():
    print("=== Fibonacci Sequence Generator ===")
    
    while True:
        print("\nOptions:")
        print("1. Generate first N Fibonacci numbers")
        print("2. Generate Fibonacci numbers up to a limit")
        print("3. Check if a number is Fibonacci")
        print("4. Get nth Fibonacci number (recursive)")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            print("Goodbye!")
            break
        
        try:
            if choice == '1':
                n = int(input("Enter the number of terms: "))
                if n < 0:
                    print("Please enter a non-negative number.")
                    continue
                
                # Iterative method
                fib_list = fibonacci_iterative(n)
                print(f"\nFirst {n} Fibonacci numbers (iterative):")
                print(fib_list)
                
                # Generator method
                print(f"\nFirst {n} Fibonacci numbers (generator):")
                fib_gen = list(fibonacci_generator(n))
                print(fib_gen)
            
            elif choice == '2':
                limit = int(input("Enter the upper limit: "))
                if limit < 0:
                    print("Please enter a non-negative number.")
                    continue
                
                fib_list = fibonacci_up_to(limit)
                print(f"\nFibonacci numbers up to {limit}:")
                print(fib_list)
                print(f"Total count: {len(fib_list)}")
            
            elif choice == '3':
                num = int(input("Enter a number to check: "))
                if is_fibonacci_number(num):
                    print(f"{num} is a Fibonacci number!")
                else:
                    print(f"{num} is not a Fibonacci number.")
            
            elif choice == '4':
                n = int(input("Enter the position (n): "))
                if n < 1:
                    print("Please enter a positive number.")
                    continue
                
                result = fibonacci_recursive(n)
                print(f"\nThe {n}th Fibonacci number (recursive): {result}")
                print("Note: Recursive method is slower for large numbers.")
            
            else:
                print("Invalid choice! Please try again.")
        
        except ValueError:
            print("Please enter a valid integer.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

