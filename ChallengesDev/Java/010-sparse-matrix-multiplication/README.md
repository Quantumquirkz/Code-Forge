# Challenge 010: Sparse Matrix Multiplication

## Problem Description
Given two sparse matrices (with many zeros) `mat1` of size $m \times k$ and `mat2` of size $k \times n$, return the result of `mat1 * mat2`. You must optimize the multiplication to skip cells that contain zero.

## Input and Output Format
- **Input**: Two integer matrices `int[][] mat1`, `int[][] mat2`.
- **Output**: The resulting matrix `int[][]`.

## Constraints and Edge Cases
- $1 \le m, n, k \le 300$.
- Most elements are zero.
- A standard $O(m \times k \times n)$ solution is acceptable, but the optimized version is preferred for this "deep coding" challenge.

## Usage Example
```java
int[][] mat1 = {{1, 0, 0}, {-1, 0, 3}};
int[][] mat2 = {{7, 0, 0}, {0, 0, 0}, {0, 0, 1}};
// Result: {{7, 0, 0}, {-7, 0, 3}}
```

## Key Concepts
- **Sparse Matrix**: Matrices where most elements are zero.
- **Optimization**: Iterate only over non-zero elements to avoid $0 \times x$ operations.
- **Time Complexity**: $O(m \times k \times n)$ in the worst case, but much faster for sparse matrices.
