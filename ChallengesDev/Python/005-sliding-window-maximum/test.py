import unittest
from solucion import maxSlidingWindow

class TestSlidingWindow(unittest.TestCase):
    def test_example(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        self.assertEqual(maxSlidingWindow(nums, k), [3, 3, 5, 5, 6, 7])

    def test_single_element(self):
        self.assertEqual(maxSlidingWindow([1], 1), [1])

    def test_decreasing_sequence(self):
        self.assertEqual(maxSlidingWindow([5, 4, 3, 2, 1], 2), [5, 4, 3, 2])

    def test_increasing_sequence(self):
        self.assertEqual(maxSlidingWindow([1, 2, 3, 4, 5], 3), [3, 4, 5])

if __name__ == '__main__':
    unittest.main()
