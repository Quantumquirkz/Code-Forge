class TrieNode:
    """Individual node of the Trie."""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """
    Trie data structure (Prefix Tree).
    Searches and insertions are O(L), where L is the length of the word.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie.
        Time Complexity: O(L)
        """
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if there is any word that starts with the given prefix.
        Time Complexity: O(L)
        """
        return self._find_node(prefix) is not None

    def _find_node(self, text: str) -> TrieNode:
        """Helper to navigate to the node corresponding to a string."""
        node = self.root
        for char in text:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

# --- Complexity Analysis ---
# Time:
#   - Insert/Search/StartsWith: O(L) where L is the length of the input.
# Space:
#   - O(W * L) in the worst case, where W is the number of words and L their average length.
#   - However, the Trie saves space by sharing common prefixes.
