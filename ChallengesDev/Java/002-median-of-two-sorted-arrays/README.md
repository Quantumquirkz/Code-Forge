# Challenge 002: Median of Two Sorted Arrays

## Problem Description
Given two sorted arrays `nums1` and `nums2` of sizes $m$ and $n$ respectively, return the **median** of the two combined sorted arrays. The overall time complexity should be $O(\log(m+n))$. This is a classic deep-coding problem that requires a solid understanding of binary search applied to partitions.

## Input and Output Format
- **Input**: Two integer arrays `int[] nums1`, `int[] nums2`.
- **Output**: A `double` value representing the median.

## Constraints and Edge Cases
- $0 \le m, n \le 1000$.
- $1 \le m + n \le 2000$.
- Arrays can have different sizes. One of them can be empty.

## Usage Example
```java
int[] nums1 = {1, 3};
int[] nums2 = {2};
// Result: 2.0

int[] nums1 = {1, 2};
int[] nums2 = {3, 4};
// Result: 2.5
```

## Key Concepts
- **Binary Search**: Instead of combining the arrays ($O(m+n)$), we search for the ideal partition point in the smaller array.
- **Partition**: Split both arrays into two parts such that the left half contains the same number of elements as the right (or one more) and all elements on the left are less than or equal to those on the right.
- **Time Complexity**: $O(\log(\min(m, n)))$.
