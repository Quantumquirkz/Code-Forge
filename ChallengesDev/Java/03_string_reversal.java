/*
 * Exercise: String Reversal
 * Description: Develop a program that reverses a given string.
 * Author: Jhuomar Barria
 */

import java.util.Scanner;

public class StringReversal {
    
    // Method 1: Using StringBuilder (most efficient)
    public static String reverseStringBuilder(String str) {
        return new StringBuilder(str).reverse().toString();
    }
    
    // Method 2: Using character array
    public static String reverseCharArray(String str) {
        char[] chars = str.toCharArray();
        int left = 0;
        int right = chars.length - 1;
        
        while (left < right) {
            // Swap characters
            char temp = chars[left];
            chars[left] = chars[right];
            chars[right] = temp;
            left++;
            right--;
        }
        
        return new String(chars);
    }
    
    // Method 3: Using recursion
    public static String reverseRecursive(String str) {
        if (str == null || str.length() <= 1) {
            return str;
        }
        return reverseRecursive(str.substring(1)) + str.charAt(0);
    }
    
    // Method 4: Using loop
    public static String reverseLoop(String str) {
        String reversed = "";
        for (int i = str.length() - 1; i >= 0; i--) {
            reversed += str.charAt(i);
        }
        return reversed;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== String Reversal Program ===");
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();
        
        System.out.println("\nOriginal string: " + input);
        System.out.println("\n--- Different Methods ---");
        
        // Method 1: StringBuilder
        System.out.println("1. Using StringBuilder: " + reverseStringBuilder(input));
        
        // Method 2: Character Array
        System.out.println("2. Using Character Array: " + reverseCharArray(input));
        
        // Method 3: Recursion
        System.out.println("3. Using Recursion: " + reverseRecursive(input));
        
        // Method 4: Loop
        System.out.println("4. Using Loop: " + reverseLoop(input));
        
        // Check if palindrome
        String reversed = reverseStringBuilder(input);
        if (input.equalsIgnoreCase(reversed)) {
            System.out.println("\n✓ The string is a palindrome!");
        } else {
            System.out.println("\n✗ The string is not a palindrome.");
        }
        
        scanner.close();
    }
}

