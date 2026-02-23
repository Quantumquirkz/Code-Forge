import unittest
from solucion import ladderLength

class TestWordLadder(unittest.TestCase):
    def test_example(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        self.assertEqual(ladderLength(beginWord, endWord, wordList), 5)

    def test_no_solution(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
        self.assertEqual(ladderLength(beginWord, endWord, wordList), 0)

    def test_direct_change(self):
        self.assertEqual(ladderLength("a", "c", ["a", "b", "c"]), 2)

if __name__ == '__main__':
    unittest.main()
