/*
 * Exercise: Fibonacci Series Generator
 * Description: Implement a program that generates and prints the Fibonacci series up to a specified number of terms.
 * Author: Jhuomar Barria
 */

#include <iostream>
#include <vector>
using namespace std;

// Iterative approach to generate Fibonacci series
vector<long long> fibonacciIterative(int n) {
    vector<long long> fib;
    
    if (n <= 0) {
        return fib;
    }
    
    if (n >= 1) {
        fib.push_back(0);
    }
    if (n >= 2) {
        fib.push_back(1);
    }
    
    for (int i = 2; i < n; i++) {
        fib.push_back(fib[i - 1] + fib[i - 2]);
    }
    
    return fib;
}

// Recursive function to get nth Fibonacci number
long long fibonacciRecursive(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

int main() {
    int terms;
    int choice;
    
    cout << "=== Fibonacci Series Generator ===" << endl;
    cout << "Enter the number of terms: ";
    cin >> terms;
    
    if (terms <= 0) {
        cout << "Please enter a positive number." << endl;
        return 1;
    }
    
    cout << "\nChoose method:" << endl;
    cout << "1. Iterative (Recommended for large numbers)" << endl;
    cout << "2. Recursive (Shows nth term only)" << endl;
    cout << "Enter choice (1 or 2): ";
    cin >> choice;
    
    if (choice == 1) {
        // Iterative approach
        vector<long long> fib = fibonacciIterative(terms);
        
        cout << "\nFibonacci series (first " << terms << " terms):" << endl;
        for (int i = 0; i < fib.size(); i++) {
            cout << fib[i];
            if (i < fib.size() - 1) {
                cout << ", ";
            }
        }
        cout << endl;
    } else if (choice == 2) {
        // Recursive approach
        cout << "\nFibonacci series (first " << terms << " terms):" << endl;
        for (int i = 0; i < terms; i++) {
            cout << fibonacciRecursive(i);
            if (i < terms - 1) {
                cout << ", ";
            }
        }
        cout << endl;
        cout << "\nNote: Recursive method is slower for large numbers." << endl;
    } else {
        cout << "Invalid choice!" << endl;
        return 1;
    }
    
    return 0;
}

