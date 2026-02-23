# Challenge 008: N-Queens

## Problem Description
The **n-queens** puzzle is the problem of placing $n$ queens on an $n \times n$ chessboard such that no two queens attack each other. Given an integer $n$, return all distinct solutions to the puzzle. Each solution should be represented as a board of strings where 'Q' and '.' indicate a queen and an empty space respectively.

## Input and Output Format
- **Input**: An integer $n$.
- **Output**: A list of lists of strings (`List[List[str]]`), where each inner list is a valid configuration.

## Constraints and Edge Cases
- $1 \le n \le 9$ (For this challenge, but the code should be efficient).
- No queens should be in the same row, column, or diagonal.
- Edge case: $n=1, n=2, n=3$ (consider empty solutions).

## Usage Example
```python
# For n = 4, there are 2 solutions:
# Solution 1: [".Q..","...Q","Q...","..Q."]
# Solution 2: ["..Q.","Q...","...Q",".Q.."]
```

## Key Concepts
- **Backtracking**: Try positions row by row and backtrack if a queen cannot be placed.
- **Efficiency with Sets**: Use sets to track occupied columns and diagonals in $O(1)$.
- **Diagonal Equations**:
  - Principal diagonal: $row - col$ is constant.
  - Anti-diagonal: $row + col$ is constant.
