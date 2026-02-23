from typing import List

def solveSudoku(board: List[List[str]]) -> None:
    """
    Solves Sudoku in-place using backtracking.
    """
    def is_valid(r: int, c: int, char: str) -> bool:
        for i in range(9):
            # Check row
            if board[r][i] == char:
                return False
            # Check column
            if board[i][c] == char:
                return False
            # Check 3x3 block
            if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == char:
                return False
        return True

    def backtrack() -> bool:
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for char in "123456789":
                        if is_valid(r, c, char):
                            board[r][c] = char
                            if backtrack():
                                return True
                            # Undo choice
                            board[r][c] = "."
                    return False # No valid number found for this cell
        return True # All cells filled correctly

    backtrack()

# --- Complexity Analysis ---
# Time: O(9^(N*N)) in the worst case, but much less in practice thanks to sudoku pruning.
# Space: O(N*N) for the recursion stack (depth of empty cells).
