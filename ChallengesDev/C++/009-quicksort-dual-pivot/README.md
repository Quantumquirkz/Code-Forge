# Challenge 009: Quicksort Dual-Pivot

## Problem Description
Implement the **Dual-Pivot Quicksort** sorting algorithm, an improvement over standard Quicksort that uses two pivots to divide the array into three parts. This is the variant used in Java's `Arrays.sort()` implementation for primitive types due to its superior efficiency on many real-world datasets.

## Input and Output Format
- **Input**: An integer array `vector<int>& nums`.
- **Output**: None (sorts the array *in-place*).

## Constraints and Edge Cases
- Handle empty arrays or arrays with a single element.
- Implement partitioned efficiently to move elements smaller than the smaller pivot to the left, greater than the larger pivot to the right, and intermediates to the center.

## Usage Example
```cpp
vector<int> nums = {24, 8, 42, 75, 29, 77, 38, 57};
dualPivotQuickSort(nums, 0, nums.size() - 1);
// nums is now sorted.
```

## Key Concepts
- **Multi-Pivot Partitioning**: Dividing the range into more than two sub-ranges.
- **Pivot Selection**: Choosing the two pivots appropriately (usually the ends after ensuring $P_1 \le P_2$).
- **Time Complexity**: $O(n \log n)$ average, $O(n^2)$ worst case (though less likely than standard).
