# Challenge 010: Matrix Chain Multiplication

## Problem Description
Given a sequence of matrices, the goal is to find the most efficient way to multiply these matrices together (i.e., find the order of parentheses that minimizes the total number of scalar multiplications). You are not asked to perform the multiplication, but to determine the minimum cost.

## Input and Output Format
- **Input**: An integer array `vector<int>& p`, where matrix $A_i$ has dimensions $p[i-1] \times p[i]$.
- **Output**: An integer representing the minimum number of scalar multiplications needed.

## Constraints and Edge Cases
- $2 \le \text{p.size()} \le 100$.
- Dimension values are positive.
- Use dynamic programming to solve the problem in $O(n^3)$.

## Usage Example
```cpp
vector<int> p = {10, 30, 5, 60};
// Matrices: A1(10x30), A2(30x5), A3(5x60)
// Possibilities:
// (A1*A2)*A3 = (10*30*5) + (10*5*60) = 1500 + 3000 = 4500
// A1*(A2*A3) = (30*5*60) + (10*30*60) = 9000 + 18000 = 27000
// Result: 4500
```

## Key Concepts
- **Optimal Substructure**: The optimal solution to the problem depends on the optimal solutions to its sub-problems.
- **Overlapping Subproblems**: The problem can be divided into sub-problems that repeat.
- **Dynamic Programming Table**: Storing results of sub-ranges `[i, j]`.
 pieces of code.
