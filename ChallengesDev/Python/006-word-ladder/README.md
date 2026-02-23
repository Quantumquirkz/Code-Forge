# Challenge 006: Word Ladder

## Problem Description
Given two words, `beginWord` and `endWord`, and a dictionary's word list `wordList`, return the number of words in the **shortest transformation sequence** from `beginWord` to `endWord`, such that:

1. Every intermediate word must be in the `wordList`.
2. Only one letter can be changed at a time.

## Input and Output Format
- **Input**: `beginWord` (str), `endWord` (str), `wordList` (List[str]).
- **Output**: An integer representing the length of the sequence (including start and end). If no such sequence exists, return 0.

## Constraints and Edge Cases
- $1 \le \text{beginWord.length} \le 10$.
- $1 \le \text{wordList.length} \le 5000$.
- All words consist of lowercase letters.
- `endWord` must be in `wordList` for a solution to exist.

## Usage Example
```python
beginWord = "hit", endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# Sequence: hit -> hot -> dot -> dog -> cog
# Length: 5
```

## Key Concepts
- **BFS (Breadth-First Search)**: Ideal for finding the shortest path in an unweighted graph.
- **Pattern Pre-processing**: Grouping words by patterns (e.g., `h*t`) to avoid $O(N^2)$ comparisons.
- **Time Complexity**: $O(M^2 \times N)$, where $M$ is the word length and $N$ the number of words.
