# Challenge 008: AVL Tree (Self-Balancing Binary Search Tree)

## Problem Description
Implement an **AVL Tree**, a binary search tree that automatically keeps itself balanced. For each node, the heights of its two child subtrees differ by at most one. You must implement the basic insertion and balancing operations (rotations).

## Input and Output Format
- **Operations**:
  - `Node insert(Node node, int key)`: Inserts a key and performs rotations if necessary.
  - `int getBalance(Node node)`: Calculates the balance factor.
  - `Node rotateLeft(Node y)`, `Node rotateRight(Node x)`: Performs simple rotations.

## Constraints and Edge Cases
- Handle duplicated key insertions (optional, here we will ignore them).
- Update node heights after each insertion.

## Usage Example
```java
AVLTree tree = new AVLTree();
tree.root = tree.insert(tree.root, 10);
tree.root = tree.insert(tree.root, 20);
tree.root = tree.insert(tree.root, 30);
// The tree should rotate so that 20 becomes the root.
```

## Key Concepts
- **Height-Balanced**: Maintains a search complexity of $O(\log n)$.
- **Rotations**: Four cases: Left-Left, Right-Right, Left-Right, Right-Left.
- **Time Complexity**: $O(\log n)$ for insertion and search.
