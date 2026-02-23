# Challenge 001: LRU Cache (Least Recently Used)

## Problem Description
Design and implement a data structure for a **Least Recently Used (LRU) cache**. It should support the following operations in $O(1)$ constant time:

- `get(key)`: Gets the value of the key if it exists in the cache, otherwise returns -1. Accessing a key marks it as "recently used".
- `put(key, value)`: Inserts or updates the value of the key. If the cache capacity has been reached, it must remove the **least recently used** item before inserting the new element.

## Input and Output Format
- **Input (put)**: Key (integer) and Value (integer).
- **Input (get)**: Key (integer).
- **Output (get)**: Associated value or -1.

## Constraints and Edge Cases
- The cache capacity will be a positive integer.
- If a key already exists, `put` updates its value and marks it as recently used.
- $O(1)$ for both operations is mandatory.

## Usage Example
```python
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # Returns 1
cache.put(3, 3)        # Evicts key 2
print(cache.get(2))    # Returns -1 (not found)
```

## Key Concepts
- **Hash Map**: For fast $O(1)$ node lookups.
- **Doubly Linked List**: To move elements to the front (recently used) and remove from the end (least used) in $O(1)$.
