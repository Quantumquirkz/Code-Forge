# Challenge 001: Reverse a Linked List

## Problem Description
Given the head of a singly linked list, reverse the list and return the new head. You must implement both **iterative** and **recursive** solutions.

## Input and Output Format
- **Input**: The `head` node of a linked list.
- **Output**: The new `head` node of the reversed list.

## Constraints and Edge Cases
- The number of nodes is in the range $[0, 5000]$.
- Node values are in the range $[-5000, 5000]$.
- Edge case: Empty list (`null`) or list with a single node.

## Usage Example
```java
// Original list: 1 -> 2 -> 3 -> 4 -> 5
// Reversed list: 5 -> 4 -> 3 -> 2 -> 1
```

## Key Concepts
- **Pointer Manipulation**: Reassign the `next` of each node.
- **Recursion**: Understand how the change propagates from the end to the beginning.
- **Time/Space Complexity**: $O(n)$ time for both, $O(1)$ space for iterative vs $O(n)$ for recursive (stack).
