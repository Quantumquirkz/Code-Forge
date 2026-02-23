# Challenge 006: Segment Tree

## Problem Description
Implement a **Segment Tree** to perform range sum queries and individual element updates in an array efficiently. A Segment Tree is a tree-based data structure that allows responding to range queries in logarithmic time.

## Input and Output Format
- **Class**: `SegmentTree`
- **Operations**:
  - `void update(int index, int val)`: Updates the value at a specific position.
  - `int query(int left, int right)`: Returns the sum of elements in the range `[left, right]`.
  - Constructor that initializes the tree from a `vector<int>`.

## Constraints and Edge Cases
- The size of the original array can be up to $10^5$.
- Queries and updates must be performed in $O(\log n)$.
- Handle out-of-bounds ranges (optional, here we will assume valid ranges).

## Usage Example
```cpp
vector<int> nums = {1, 3, 5, 7, 9, 11};
SegmentTree st(nums);
st.query(1, 3); // 3 + 5 + 7 = 15
st.update(1, 10);
st.query(1, 3); // 10 + 5 + 7 = 22
```

## Key Concepts
- **Divide and Conquer**: The tree divides the range into two halves at each level.
- **Tree Storage**: Generally implemented as an array of size $4n$.
- **Range Queries**: Combine results from nodes covering sub-ranges of the requested range.
