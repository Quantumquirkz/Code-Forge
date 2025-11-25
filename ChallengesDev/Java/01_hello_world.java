/*
 * Exercise: Hello World Application
 * Description: Create a simple Java application that prints "Hello, World!" to the console.
 * Author: Jhuomar Barria
 */

public class HelloWorld {
    public static void main(String[] args) {
        // Simple Hello World program
        System.out.println("Hello, World!");
        
        // Enhanced version with additional information
        System.out.println("\n=== Welcome to Java Programming ===");
        System.out.println("This is a basic Hello World program.");
        System.out.println("Author: Jhuomar Barria");
        
        // Display system information
        System.out.println("\nJava Version: " + System.getProperty("java.version"));
        System.out.println("Operating System: " + System.getProperty("os.name"));
    }
}

