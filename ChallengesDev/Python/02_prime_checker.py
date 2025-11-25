"""
Exercise: Prime Number Checker
Description: Create a function that determines if a given number is prime.
Author: Jhuomar Barria
"""

import math

def is_prime(n):
    """
    Check if a number is prime.
    Optimized by checking divisors up to the square root of n.
    """
    # Handle edge cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check for factors from 5 to sqrt(n)
    # Only check odd numbers (i and i+2)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def get_prime_factors(n):
    """Get all prime factors of a number"""
    factors = []
    # Check for 2
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check for odd factors
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    # If n is still greater than 2, it's a prime factor
    if n > 2:
        factors.append(n)
    
    return factors

def generate_primes_up_to(limit):
    """Generate all prime numbers up to a given limit using Sieve of Eratosthenes"""
    if limit < 2:
        return []
    
    # Create a boolean array
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    
    primes = [i for i in range(2, limit + 1) if sieve[i]]
    return primes

def main():
    print("=== Prime Number Checker ===")
    
    while True:
        try:
            number = int(input("\nEnter a number (or 0 to exit): "))
            
            if number == 0:
                print("Goodbye!")
                break
            
            if number < 0:
                print("Please enter a positive number.")
                continue
            
            # Check if prime
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
                factors = get_prime_factors(number)
                if factors:
                    print(f"Prime factors: {factors}")
            
            # Ask if user wants to see all primes up to this number
            if number > 1:
                show_all = input(f"\nShow all prime numbers up to {number}? (y/n): ").lower()
                if show_all == 'y':
                    primes = generate_primes_up_to(number)
                    print(f"Prime numbers up to {number}: {primes}")
                    print(f"Total count: {len(primes)}")
        
        except ValueError:
            print("Please enter a valid integer.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

