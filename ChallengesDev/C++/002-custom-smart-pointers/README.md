# Challenge 002: Custom Smart Pointers (Shared Ptr)

## Problem Description
Implement a simplified version of `std::shared_ptr`. This smart pointer must manage an object's lifecycle using reference counting. When the last `shared_ptr` pointing to the object is destroyed or reassigned, the managed object must be automatically deleted.

## Input and Output Format
- **Class**: `CustomSharedPtr<T>`
- **Operations**:
  - Constructor, Copy Constructor, Assignment Operator.
  - Destructor (memory release if `refCount == 0`).
  - `T& operator*()`, `T* operator->()`.
  - `int use_count()`: Returns the current number of references.

## Constraints and Edge Cases
- Reference counting must be stored on the heap to be shared between instances.
- Handle self-assignment (`ptr = ptr`).
- No need to handle thread-safety for the simplicity of this challenge.

## Usage Example
```cpp
{
    CustomSharedPtr<int> ptr1(new int(10));
    {
        CustomSharedPtr<int> ptr2 = ptr1;
        // use_count() == 2
    }
    // use_count() == 1
}
// The integer is released here.
```

## Key Concepts
- **RAII (Resource Acquisition Is Initialization)**: Manage resource lifecycle through the lifecycle of objects on the stack.
- **Reference Counting**: Basic technique for shared memory management.
- **Operator Overloading**: Making the class behave like a real pointer.
