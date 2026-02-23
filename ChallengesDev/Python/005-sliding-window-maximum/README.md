# Challenge 005: Sliding Window Maximum

## Problem Description
You are given an array of integers `nums` and there is a sliding window of size `k` that moves from left to right. You can only see the `k` numbers in the window. Each time the window moves, you must find the **maximum value** within it.

## Input and Output Format
- **Input**: A list of integers `nums` and an integer `k`.
- **Output**: A list with the maximum values for each window.

## Constraints and Edge Cases
- $1 \le \text{nums.length} \le 10^5$.
- $-10^4 \le \text{nums[i]} \le 10^4$.
- $1 \le k \le \text{nums.length}$.
- The solution must be $O(n)$. An $O(n \times k)$ solution is not acceptable for this deep code challenge.

## Usage Example
```python
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# Output: [3, 3, 5, 5, 6, 7]
# Windows:
# [1 3 -1] -> 3
#   [3 -1 -3] -> 3
#     [-1 -3 5] -> 5
#       [-3 5 3] -> 5
#         [5 3 6] -> 6
#           [3 6 7] -> 7
```

## Key Concepts
- **Monotonic Queue**: A double-ended queue (`deque`) that maintains the indices of elements in descending order of their values.
- **Deque**: For efficient insertion and deletion at both ends.
- **Time Complexity**: $O(n)$ because each element is inserted and removed at most once.
