/*
 * Exercise: Factorial Calculator
 * Description: Implement a program that calculates the factorial of a given number using both iterative and recursive methods.
 * Author: Jhuomar Barria
 */

#include <iostream>
using namespace std;

// Iterative approach to calculate factorial
unsigned long long factorialIterative(int n) {
    if (n < 0) {
        return 0; // Factorial is not defined for negative numbers
    }
    
    unsigned long long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

// Recursive approach to calculate factorial
unsigned long long factorialRecursive(int n) {
    // Base case
    if (n < 0) {
        return 0; // Factorial is not defined for negative numbers
    }
    if (n == 0 || n == 1) {
        return 1;
    }
    
    // Recursive case
    return n * factorialRecursive(n - 1);
}

int main() {
    int number;
    int choice;
    
    cout << "=== Factorial Calculator ===" << endl;
    cout << "Enter a number: ";
    cin >> number;
    
    if (number < 0) {
        cout << "Factorial is not defined for negative numbers." << endl;
        return 1;
    }
    
    if (number > 20) {
        cout << "Warning: Factorial of numbers greater than 20 may cause overflow." << endl;
    }
    
    cout << "\nChoose method:" << endl;
    cout << "1. Iterative" << endl;
    cout << "2. Recursive" << endl;
    cout << "3. Both (for comparison)" << endl;
    cout << "Enter choice (1, 2, or 3): ";
    cin >> choice;
    
    switch (choice) {
        case 1: {
            unsigned long long result = factorialIterative(number);
            cout << "\nFactorial of " << number << " (Iterative) = " << result << endl;
            break;
        }
        case 2: {
            unsigned long long result = factorialRecursive(number);
            cout << "\nFactorial of " << number << " (Recursive) = " << result << endl;
            break;
        }
        case 3: {
            unsigned long long iterResult = factorialIterative(number);
            unsigned long long recResult = factorialRecursive(number);
            cout << "\nFactorial of " << number << ":" << endl;
            cout << "Iterative: " << iterResult << endl;
            cout << "Recursive: " << recResult << endl;
            if (iterResult == recResult) {
                cout << "Both methods produce the same result!" << endl;
            }
            break;
        }
        default:
            cout << "Invalid choice!" << endl;
            return 1;
    }
    
    return 0;
}

