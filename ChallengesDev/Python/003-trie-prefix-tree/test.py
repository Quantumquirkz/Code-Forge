import unittest
from solucion import Trie

class TestTrie(unittest.TestCase):
    def test_basic_operations(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))

    def test_overlap_and_prefix(self):
        trie = Trie()
        trie.insert("code")
        trie.insert("coder")
        self.assertTrue(trie.search("code"))
        self.assertTrue(trie.search("coder"))
        self.assertTrue(trie.startsWith("cod"))
        self.assertFalse(trie.search("cod"))

    def test_not_found(self):
        trie = Trie()
        trie.insert("hello")
        self.assertFalse(trie.search("world"))
        self.assertFalse(trie.startsWith("wo"))

if __name__ == '__main__':
    unittest.main()
