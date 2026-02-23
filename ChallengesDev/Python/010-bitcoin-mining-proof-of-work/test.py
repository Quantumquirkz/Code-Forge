import unittest
from solucion import mine_block

class TestMining(unittest.TestCase):
    def test_difficulty_1(self):
        nonce, hash_res = mine_block("test", 1)
        self.assertTrue(hash_res.startswith('0'))

    def test_difficulty_3(self):
        nonce, hash_res = mine_block("bitcoin", 3)
        self.assertTrue(hash_res.startswith('000'))
        
    def test_consistency(self):
        block = "data"
        diff = 2
        n1, h1 = mine_block(block, diff)
        n2, h2 = mine_block(block, diff)
        self.assertEqual(n1, n2)
        self.assertEqual(h1, h2)

if __name__ == '__main__':
    unittest.main()
