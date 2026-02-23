import unittest
from solucion import solveNQueens

class TestNQueens(unittest.TestCase):
    def test_n4(self):
        solutions = solveNQueens(4)
        self.assertEqual(len(solutions), 2)
        # Verificar que una de las soluciones sea la esperada
        expected = [".Q..", "...Q", "Q...", "..Q."]
        self.assertIn(expected, solutions)

    def test_n1(self):
        self.assertEqual(solveNQueens(1), [["Q"]])

    def test_n2_n3(self):
        # No hay soluciones para 2 y 3
        self.assertEqual(solveNQueens(2), [])
        self.assertEqual(solveNQueens(3), [])

if __name__ == '__main__':
    unittest.main()
