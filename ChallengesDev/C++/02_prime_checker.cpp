/*
 * Exercise: Prime Number Checker
 * Description: Develop a program to check if a number is a prime number.
 * Author: Jhuomar Barria
 */

#include <iostream>
#include <cmath>
using namespace std;

// Function to check if a number is prime
bool isPrime(int n) {
    // Handle edge cases
    if (n <= 1) {
        return false;
    }
    if (n <= 3) {
        return true;
    }
    
    // Check if n is divisible by 2 or 3
    if (n % 2 == 0 || n % 3 == 0) {
        return false;
    }
    
    // Check for factors from 5 to sqrt(n)
    // Only check odd numbers (i and i+2)
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    
    return true;
}

int main() {
    int number;
    
    cout << "=== Prime Number Checker ===" << endl;
    cout << "Enter a number: ";
    cin >> number;
    
    if (isPrime(number)) {
        cout << number << " is a prime number." << endl;
    } else {
        cout << number << " is not a prime number." << endl;
    }
    
    // Bonus: Display all prime numbers up to the given number
    if (number > 1) {
        cout << "\nPrime numbers up to " << number << ": ";
        for (int i = 2; i <= number; i++) {
            if (isPrime(i)) {
                cout << i << " ";
            }
        }
        cout << endl;
    }
    
    return 0;
}

