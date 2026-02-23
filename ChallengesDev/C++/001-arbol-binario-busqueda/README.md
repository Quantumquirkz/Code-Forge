# Challenge 001: Binary Search Tree (BST)

## Problem Description
Implement a **Binary Search Tree (BST)** that supports the basic operations: search, insertion, and deletion. The tree must maintain the property that for any node, all elements in its left subtree are smaller and all elements in its right subtree are larger.

## Input and Output Format
- **Insert**: Key (integer).
- **Search**: Key (integer). Returns `true` if it exists.
- **Delete**: Key (integer).

## Constraints and Edge Cases
- Handling duplicates (optional, here they are not allowed).
- Deleting a node with two children (requires finding the in-order successor).
- The height of the tree can be $O(n)$ in the worst case if it is not balanced.

## Usage Example
```cpp
BST tree;
tree.insert(50);
tree.insert(30);
tree.insert(70);
cout << tree.search(30); // true
tree.remove(30);
cout << tree.search(30); // false
```

## Key Concepts
- **Recursion**: Fundamental for navigating the tree structure.
- **Pointers**: Manual memory management in C++.
- **Deletion Case**: The most complex case is deleting a node with two children.
