# Challenge 006: Longest Increasing Subsequence (LIS)

## Problem Description
Given an integer array `nums`, return the length of the **longest increasing subsequence**. A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

## Input and Output Format
- **Input**: An integer array `int[] nums`.
- **Output**: An integer representing the length of the LIS.

## Constraints and Edge Cases
- $1 \le \text{nums.length} \le 2500$.
- $-10^4 \le \text{nums[i]} \le 10^4$.
- The solution should attempt to be better than $O(n^2)$, ideally $O(n \log n)$.

## Usage Example
```java
int[] nums = {10, 9, 2, 5, 3, 7, 101, 18};
// Subsequence: [2, 3, 7, 18]
// Result: 4
```

## Key Concepts
- **Dynamic Programming**: Define `dp[i]` as the LIS ending at `i`.
- **Binary Search Optimization**: Maintain a "tails" array where each element is the minimum possible tail value for an LIS of length `i`.
- **Time Complexity**: $O(n \log n)$.
