# Challenge 009: Sudoku Solver

## Problem Description
Write a program to solve a **Sudoku** board by filling the empty cells. A Sudoku board is solved if all the following rules are met:
1. Each of the digits `1-9` must appear exactly once in each row.
2. Each of the digits `1-9` must appear exactly once in each column.
3. Each of the digits `1-9` must appear exactly once in each of the 9 $3 \times 3$ sub-boxes of the grid.

Empty cells are indicated by the character `'.'`.

## Input and Output Format
- **Input**: A $9 \times 9$ board represented by a list of lists of characters (`List[List[str]]`).
- **Output**: None (modifies the original board *in-place*).

## Constraints and Edge Cases
- The given board always has a unique solution.
- The input board is always $9 \times 9$.

## Usage Example
```python
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
# After calling solveSudoku(board), the board will be complete.
```

## Key Concepts
- **Backtracking**: Try placing numbers from 1 to 9 and backtrack if we find a violation.
- **Efficient Validation**: Check row, column, and 3x3 block.
- **Recursion**: Dive into the decision tree of empty cells.
