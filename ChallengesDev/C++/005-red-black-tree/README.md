# Challenge 005: Red-Black Tree

## Problem Description
Implement a **Red-Black Tree**, a self-balancing binary search tree that uses an extra bit per node to indicate its "color" (Red or Black). These color rules guarantee that no path from the root to a leaf is more than twice as long as any other path.

## Input and Output Format
- **Operations**:
  - `Node* insert(int key)`: Inserts a key and rebalances the tree.
  - `void rotateLeft(Node* &root, Node* &x)`, `void rotateRight(Node* &root, Node* &y)`.
  - `void fixViolation(Node* &root, Node* &ptr)`: Corrects violations of red-black tree properties.

## Constraints and Edge Cases
- Red-black tree properties must be maintained at all times:
  1. Every node is either red or black.
  2. The root is black.
  3. Every leaf (NIL) is black.
  4. If a node is red, both its children are black.
  5. For each node, all simple paths from the node to descendant leaves contain the same number of black nodes.

## Usage Example
```cpp
RedBlackTree tree;
tree.insert(7);
tree.insert(3);
tree.insert(18);
tree.insert(10);
// The tree will balance itself automatically.
```

## Key Concepts
- **Self-Balancing**: Guarantees $O(\log n)$ for insertion, deletion, and search.
- **Color Rules**: Simplify balancing conditions compared to AVL trees.
- **Rotations & Recoloring**: Mechanisms to restore balance.
