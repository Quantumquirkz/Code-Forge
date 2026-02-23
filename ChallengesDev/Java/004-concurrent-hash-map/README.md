# Challenge 004: Concurrent Hash Map (Simplified)

## Problem Description
Implement a simplified version of a `ConcurrentHashMap` in Java. The data structure must allow concurrent access from multiple threads for `put` and `get` operations without data corruption and while minimizing global locking.

## Input and Output Format
- **Operations**:
  - `void put(K key, V value)`: Inserts or updates a key-value pair.
  - `V get(K key)`: Retrieves the value associated with a key.
  - `int size()`: Returns the total number of elements.

## Constraints and Edge Cases
- Use **Segmented Locking** or an array of `ReentrantLock` to reduce contention between threads.
- Handle collisions using chaining (linked lists).
- Implementing re-hash (resizing) is not necessary for the simplicity of this challenge, but it should be mentioned.

## Usage Example
```java
SimpleConcurrentHashMap<String, Integer> map = new SimpleConcurrentHashMap<>(16);
map.put("key1", 10);
Integer val = map.get("key1");
```

## Key Concepts
- **Thread-Safety**: Ensuring the map state is consistent under concurrency.
- **Lock Granularity**: Locking only a part of the map (a "bucket" or segment) instead of the entire map.
- **Atomicity**: Operations that execute as a single indivisible unit.
