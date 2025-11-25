/*
 * Exercise: Even and Odd Number Checker
 * Description: Write a program that checks if a number entered by the user is even or odd.
 * Author: Jhuomar Barria
 */

import java.util.Scanner;

public class EvenOddChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== Even and Odd Number Checker ===");
        System.out.print("Enter a number: ");
        
        int number = scanner.nextInt();
        
        // Check if number is even or odd using modulus operator
        if (number % 2 == 0) {
            System.out.println(number + " is an even number.");
        } else {
            System.out.println(number + " is an odd number.");
        }
        
        // Bonus: Check multiple numbers
        System.out.println("\n--- Check Multiple Numbers ---");
        System.out.print("Enter the range (start end): ");
        int start = scanner.nextInt();
        int end = scanner.nextInt();
        
        System.out.println("\nEven numbers in range [" + start + ", " + end + "]:");
        for (int i = start; i <= end; i++) {
            if (i % 2 == 0) {
                System.out.print(i + " ");
            }
        }
        
        System.out.println("\n\nOdd numbers in range [" + start + ", " + end + "]:");
        for (int i = start; i <= end; i++) {
            if (i % 2 != 0) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
        
        scanner.close();
    }
}

