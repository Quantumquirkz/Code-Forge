from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    """
    Solves the N-Queens problem using backtracking.
    """
    solutions = []
    board = [["."] * n for _ in range(n)]
    
    # Sets to track attacks
    cols = set()
    pos_diag = set() # (r + c)
    neg_diag = set() # (r - c)
    
    def backtrack(r: int):
        # Base case: all queens placed
        if r == n:
            copy = ["".join(row) for row in board]
            solutions.append(copy)
            return
            
        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
                
            # Place queen
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"
            
            backtrack(r + 1)
            
            # Backtrack
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."
            
    backtrack(0)
    return solutions

# --- Complexity Analysis ---
# Time: O(N!)
#   In the first row we have N options, in the second fewer than N-2, etc.
# Space: O(N^2)
#   For the board and the recursion stack.
