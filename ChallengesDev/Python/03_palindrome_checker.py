"""
Exercise: Palindrome Checker
Description: Develop a program that checks if a text string is a palindrome (reads the same forwards and backwards).
Author: Jhuomar Barria
"""

def is_palindrome_simple(text):
    """Check if text is palindrome using string slicing"""
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def is_palindrome_loop(text):
    """Check if text is palindrome using loop"""
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    left = 0
    right = len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

def is_palindrome_recursive(text):
    """Check if text is palindrome using recursion"""
    cleaned = text.replace(" ", "").lower()
    
    def check(left, right):
        if left >= right:
            return True
        if cleaned[left] != cleaned[right]:
            return False
        return check(left + 1, right - 1)
    
    return check(0, len(cleaned) - 1)

def is_palindrome_advanced(text):
    """Advanced palindrome checker that handles punctuation and special characters"""
    import re
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]

def find_palindromes_in_text(text):
    """Find all palindromic words in a text"""
    words = text.split()
    palindromes = []
    
    for word in words:
        if is_palindrome_simple(word):
            palindromes.append(word)
    
    return palindromes

def main():
    print("=== Palindrome Checker ===")
    
    while True:
        print("\nOptions:")
        print("1. Check if a string is a palindrome")
        print("2. Find palindromic words in a text")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '3':
            print("Goodbye!")
            break
        
        if choice not in ['1', '2']:
            print("Invalid choice! Please try again.")
            continue
        
        text = input("Enter a string: ")
        
        if not text.strip():
            print("Please enter a non-empty string.")
            continue
        
        if choice == '1':
            print(f"\nOriginal: '{text}'")
            print(f"Reversed: '{text[::-1]}'")
            
            # Test different methods
            result_simple = is_palindrome_simple(text)
            result_loop = is_palindrome_loop(text)
            result_recursive = is_palindrome_recursive(text)
            result_advanced = is_palindrome_advanced(text)
            
            print(f"\n--- Results ---")
            print(f"Simple method: {'✓ Palindrome' if result_simple else '✗ Not a palindrome'}")
            print(f"Loop method: {'✓ Palindrome' if result_loop else '✗ Not a palindrome'}")
            print(f"Recursive method: {'✓ Palindrome' if result_recursive else '✗ Not a palindrome'}")
            print(f"Advanced method (ignores punctuation): {'✓ Palindrome' if result_advanced else '✗ Not a palindrome'}")
        
        elif choice == '2':
            palindromes = find_palindromes_in_text(text)
            if palindromes:
                print(f"\nPalindromic words found: {palindromes}")
            else:
                print("\nNo palindromic words found in the text.")

if __name__ == "__main__":
    main()

