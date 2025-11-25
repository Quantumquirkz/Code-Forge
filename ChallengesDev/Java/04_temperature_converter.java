/*
 * Exercise: Basic Temperature Converter
 * Description: Implement a temperature converter that converts temperatures between Celsius and Fahrenheit.
 * Author: Jhuomar Barria
 */

import java.util.Scanner;

public class TemperatureConverter {
    
    // Convert Celsius to Fahrenheit
    public static double celsiusToFahrenheit(double celsius) {
        return (celsius * 9.0 / 5.0) + 32.0;
    }
    
    // Convert Fahrenheit to Celsius
    public static double fahrenheitToCelsius(double fahrenheit) {
        return (fahrenheit - 32.0) * 5.0 / 9.0;
    }
    
    // Convert Celsius to Kelvin
    public static double celsiusToKelvin(double celsius) {
        return celsius + 273.15;
    }
    
    // Convert Kelvin to Celsius
    public static double kelvinToCelsius(double kelvin) {
        return kelvin - 273.15;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== Temperature Converter ===");
        System.out.println("1. Celsius to Fahrenheit");
        System.out.println("2. Fahrenheit to Celsius");
        System.out.println("3. Celsius to Kelvin");
        System.out.println("4. Kelvin to Celsius");
        System.out.println("5. Fahrenheit to Kelvin");
        System.out.println("6. Kelvin to Fahrenheit");
        System.out.print("Enter your choice (1-6): ");
        
        int choice = scanner.nextInt();
        
        if (choice < 1 || choice > 6) {
            System.out.println("Invalid choice!");
            scanner.close();
            return;
        }
        
        System.out.print("Enter the temperature: ");
        double temperature = scanner.nextDouble();
        
        System.out.printf("\nResult: ");
        
        switch (choice) {
            case 1:
                System.out.printf("%.2f°C = %.2f°F\n", temperature, celsiusToFahrenheit(temperature));
                break;
            case 2:
                System.out.printf("%.2f°F = %.2f°C\n", temperature, fahrenheitToCelsius(temperature));
                break;
            case 3:
                System.out.printf("%.2f°C = %.2fK\n", temperature, celsiusToKelvin(temperature));
                break;
            case 4:
                System.out.printf("%.2fK = %.2f°C\n", temperature, kelvinToCelsius(temperature));
                break;
            case 5:
                double kelvin = celsiusToKelvin(fahrenheitToCelsius(temperature));
                System.out.printf("%.2f°F = %.2fK\n", temperature, kelvin);
                break;
            case 6:
                double fahrenheit = celsiusToFahrenheit(kelvinToCelsius(temperature));
                System.out.printf("%.2fK = %.2f°F\n", temperature, fahrenheit);
                break;
        }
        
        // Display common temperature reference points
        System.out.println("\n--- Common Temperature Reference Points ---");
        System.out.println("Water Freezing Point: 0°C = 32°F = 273.15K");
        System.out.println("Water Boiling Point: 100°C = 212°F = 373.15K");
        System.out.println("Room Temperature: ~20°C = ~68°F = ~293.15K");
        
        scanner.close();
    }
}

