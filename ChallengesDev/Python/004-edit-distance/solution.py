def minDistance(word1: str, word2: str) -> int:
    """
    Calculates the Levenshtein distance between two words using DP.
    
    Time Complexity: O(M * N)
    Space Complexity: O(M * N) -> Can be optimized to O(min(M, N))
    """
    m, n = len(word1), len(word2)
    
    # dp[i][j] will be the edit distance between word1[:i] and word2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialization: convert empty string to word or vice versa
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
        
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Minimum between: (Insert, Delete, Replace) + 1
                dp[i][j] = 1 + min(
                    dp[i][j-1],    # Insert
                    dp[i-1][j],    # Delete
                    dp[i-1][j-1]   # Replace
                )
                
    return dp[m][n]

# --- Complexity Analysis ---
# Time: O(M * N)
# Space: O(M * N) for the DP table.
