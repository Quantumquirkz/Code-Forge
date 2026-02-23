# Challenge 003: Trie (Prefix Tree)

## Problem Description
A **Trie** (also known as a prefix tree) is a tree-like data structure used to store and retrieve keys in a set of string data. Implement the `Trie` class with the following methods:

- `insert(word)`: Inserts the string `word` into the trie.
- `search(word)`: Returns `true` if the string `word` is in the trie.
- `startsWith(prefix)`: Returns `true` if there is any previously inserted string that starts with the prefix `prefix`.

## Input and Output Format
- **Input**: Strings (typically lowercase `a-z`).
- **Output**: Booleans for `search` and `startsWith`.

## Constraints and Edge Cases
- Strings consist only of lowercase letters of the English alphabet.
- The total number of calls to the methods will be at most $3 \times 10^4$.
- Consider the case of empty strings or prefixes that are the full word.

## Usage Example
```python
trie = Trie()
trie.insert("python")
trie.search("python")     # true
trie.search("py")         # false
trie.startsWith("py")     # true
```

## Key Concepts
- **Nodes with Dictionary**: Each node contains a map of characters to child nodes.
- **End of Word**: A boolean in each node that indicates if a valid string ends there.
- **Time Complexity**: $O(L)$ for each operation, where $L$ is the length of the word/prefix.
