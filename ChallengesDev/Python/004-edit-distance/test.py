import unittest
from solucion import minDistance

class TestEditDistance(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(minDistance("horse", "ros"), 3)
        self.assertEqual(minDistance("intention", "execution"), 5)

    def test_empty_strings(self):
        self.assertEqual(minDistance("", ""), 0)
        self.assertEqual(minDistance("abc", ""), 3)
        self.assertEqual(minDistance("", "abc"), 3)

    def test_identical_strings(self):
        self.assertEqual(minDistance("hello", "hello"), 0)

if __name__ == '__main__':
    unittest.main()
