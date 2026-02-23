# Challenge 003: Merge K Sorted Lists

## Problem Description
You have an array of $k$ linked lists `lists`, where each linked list is sorted in ascending order. Combine all the linked lists into a single sorted linked list and return it.

## Input and Output Format
- **Input**: An array of objects `ListNode[] lists`.
- **Output**: The `ListNode` head of the final combined list.

## Constraints and Edge Cases
- $k$ is the number of linked lists, $0 \le k \le 10^4$.
- The total number of nodes in all lists is up to $10^4$.
- Handle cases where `lists` is null, empty, or contains empty lists.

## Usage Example
```java
// Lists: [1->4->5, 1->3->4, 2->6]
// Result: 1->1->2->3->4->4->5->6
```

## Key Concepts
- **Priority Queue (Min-Heap)**: To always obtain the node with the smallest value among the heads of the $k$ lists in logarithmic time.
- **Time Complexity**: $O(N \log k)$, where $N$ is the total number of nodes.
- **Space Complexity**: $O(k)$ to store elements in the heap.
