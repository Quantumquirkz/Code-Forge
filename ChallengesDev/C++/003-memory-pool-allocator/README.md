# Challenge 003: Memory Pool Allocator

## Problem Description
Implement a **Memory Pool**, a custom memory allocator that pre-allocates a large memory block and divides it into smaller fixed-size chunks. This reduces external fragmentation and improves performance by avoiding frequent calls to `malloc`/`new`.

## Input and Output Format
- **Class**: `MemoryPool`
- **Operations**:
  - `void* allocate()`: Returns a pointer to a free block.
  - `void deallocate(void* ptr)`: Returns the block to the pool for reuse.
  - Constructor that specifies each block's size and the number of blocks.

## Constraints and Edge Cases
- If the pool is full, `allocate()` can throw an exception or return `nullptr`.
- The pool must manage a "free list" to track available blocks.
- Use pointers to link free blocks within the pool memory itself (*in-place linking* technique).

## Usage Example
```cpp
MemoryPool pool(sizeof(MyObject), 10);
void* m1 = pool.allocate();
pool.deallocate(m1);
```

## Key Concepts
- **Custom Allocators**: Total control over how memory is reserved and released.
- **Fragmentation**: Minimization of small holes in system memory.
- **Cache Locality**: Since objects are contiguous, CPU cache performance is improved.
