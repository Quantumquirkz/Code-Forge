# Challenge 008: Bit Manipulation Mastery

## Problem Description
Implement a series of utility functions for low-level bit manipulation. These functions are fundamental for performance optimizations and systems programming.

## Input and Output Format
Implement the following functions:
1. `int countSetBits(unsigned int n)`: Counts the number of set bits (1s) in an integer (Popcount).
2. `unsigned int reverseBits(unsigned int n)`: Reverses the bit order of a 32-bit integer.
3. `bool isPowerOfTwo(int n)`: Determines if a number is a power of two without using loops.
4. `int getSingleNumber(const std::vector<int>& nums)`: In an array where every element appears twice except for one, finds the single element.

## Constraints and Edge Cases
- Use bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`).
- Solutions must be $O(1)$ in space and as time-efficient as possible.

## Usage Example
```cpp
countSetBits(7); // Result: 3 (binary 111)
isPowerOfTwo(16); // Result: true
isPowerOfTwo(15); // Result: false
```

## Key Concepts
- **Bitwise Logic**: Direct bit manipulation for speed.
- **Kernighan's Algorithm**: Efficient way to count bits.
- **XOR Properties**: Useful for finding unique numbers and fast swaps.
