import hashlib
import time
from typing import Tuple

def mine_block(block_data: str, difficulty: int) -> Tuple[int, str]:
    """
    Simulates block mining by finding a nonce that satisfies the difficulty.
    """
    prefix = '0' * difficulty
    nonce = 0
    
    while True:
        # Concatenate data and nonce
        text = block_data + str(nonce)
        # Calculate SHA-256 hash
        hash_result = hashlib.sha256(text.encode()).hexdigest()
        
        # Check if it meets the difficulty
        if hash_result.startswith(prefix):
            return nonce, hash_result
            
        nonce += 1

# --- Complexity Analysis ---
# Time: O(16^D)
#   Where D is the difficulty (number of zeros). Each position has 16 possibilities (hex).
# Space: O(1)
#   Only a few variables are stored in memory.
