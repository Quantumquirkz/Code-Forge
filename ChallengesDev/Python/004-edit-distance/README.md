# Challenge 004: Edit Distance (Levenshtein Distance)

## Problem Description
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`. You are allowed the following three operations:

1. Insert a character.
2. Delete a character.
3. Replace a character.

## Input and Output Format
- **Input**: Two strings `word1` and `word2`.
- **Output**: An integer representing the minimum edit distance.

## Constraints and Edge Cases
- $0 \le \text{word1.length, word2.length} \le 500$.
- The strings consist of lowercase English letters.
- Edge case: One of the strings is empty.

## Usage Example
```python
distance = minDistance("horse", "ros")
# Output: 3
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (delete 'r')
# rose -> ros (delete 'e')
```

## Key Concepts
- **Dynamic Programming (DP)**: Use of a 2D matrix to store subproblems.
- **Subproblems**: `dp[i][j]` represents the minimum distance between `word1[:i]` and `word2[:j]`.
- **Time Complexity**: $O(M \times N)$, where $M$ and $N$ are the word lengths.
