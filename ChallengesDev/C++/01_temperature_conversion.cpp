/*
 * Exercise: Temperature Conversion Program
 * Description: Create a program that converts temperatures between Celsius, Fahrenheit, and Kelvin.
 * Author: Jhuomar Barria
 */

#include <iostream>
#include <iomanip>
using namespace std;

// Function to convert Celsius to Fahrenheit
double celsiusToFahrenheit(double celsius) {
    return (celsius * 9.0 / 5.0) + 32.0;
}

// Function to convert Fahrenheit to Celsius
double fahrenheitToCelsius(double fahrenheit) {
    return (fahrenheit - 32.0) * 5.0 / 9.0;
}

// Function to convert Celsius to Kelvin
double celsiusToKelvin(double celsius) {
    return celsius + 273.15;
}

// Function to convert Kelvin to Celsius
double kelvinToCelsius(double kelvin) {
    return kelvin - 273.15;
}

// Function to convert Fahrenheit to Kelvin
double fahrenheitToKelvin(double fahrenheit) {
    return celsiusToKelvin(fahrenheitToCelsius(fahrenheit));
}

// Function to convert Kelvin to Fahrenheit
double kelvinToFahrenheit(double kelvin) {
    return celsiusToFahrenheit(kelvinToCelsius(kelvin));
}

int main() {
    int choice;
    double temperature;
    
    cout << "=== Temperature Conversion Program ===" << endl;
    cout << "1. Celsius to Fahrenheit" << endl;
    cout << "2. Fahrenheit to Celsius" << endl;
    cout << "3. Celsius to Kelvin" << endl;
    cout << "4. Kelvin to Celsius" << endl;
    cout << "5. Fahrenheit to Kelvin" << endl;
    cout << "6. Kelvin to Fahrenheit" << endl;
    cout << "Enter your choice (1-6): ";
    cin >> choice;
    
    if (choice < 1 || choice > 6) {
        cout << "Invalid choice!" << endl;
        return 1;
    }
    
    cout << "Enter the temperature: ";
    cin >> temperature;
    
    cout << fixed << setprecision(2);
    
    switch (choice) {
        case 1:
            cout << temperature << "°C = " << celsiusToFahrenheit(temperature) << "°F" << endl;
            break;
        case 2:
            cout << temperature << "°F = " << fahrenheitToCelsius(temperature) << "°C" << endl;
            break;
        case 3:
            cout << temperature << "°C = " << celsiusToKelvin(temperature) << "K" << endl;
            break;
        case 4:
            cout << temperature << "K = " << kelvinToCelsius(temperature) << "°C" << endl;
            break;
        case 5:
            cout << temperature << "°F = " << fahrenheitToKelvin(temperature) << "K" << endl;
            break;
        case 6:
            cout << temperature << "K = " << kelvinToFahrenheit(temperature) << "°F" << endl;
            break;
    }
    
    return 0;
}

