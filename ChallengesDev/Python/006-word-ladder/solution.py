from collections import deque, defaultdict
from typing import List

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    Finds the length of the shortest transformation sequence using BFS.
    """
    if endWord not in wordList:
        return 0
        
    L = len(beginWord)
    
    # Pre-processing: Dictionary of all generic word states.
    # Ex: "hot" -> {"*ot": ["hot"], "h*t": ["hot"], "ho*": ["hot"]}
    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(L):
            all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
            
    # Queue for BFS: (current_word, level)
    queue = deque([(beginWord, 1)])
    # Set to avoid cycles
    visited = {beginWord}
    
    while queue:
        current_word, level = queue.popleft()
        
        for i in range(L):
            # Get all possible intermediate words
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]
            
            for word in all_combo_dict[intermediate_word]:
                if word == endWord:
                    return level + 1
                if word not in visited:
                    visited.add(word)
                    queue.append((word, level + 1))
            # Optional: clear to save space if words are unique
            all_combo_dict[intermediate_word] = []
            
    return 0

# --- Complexity Analysis ---
# Time: O(M^2 * N)
#   Where M is the word length and N is the number of words in the set.
# Space: O(M^2 * N)
#   To store the combination dictionary.
