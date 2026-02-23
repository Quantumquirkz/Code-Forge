import unittest
from solucion import dijkstra, reconstruct_path

class TestDijkstra(unittest.TestCase):
    def test_simple_graph(self):
        graph = {
            0: [(1, 4), (2, 1)],
            1: [(3, 1)],
            2: [(1, 2), (3, 5)],
            3: []
        }
        distances, parents = dijkstra(graph, 0)
        self.assertEqual(distances[3], 4)
        self.assertEqual(reconstruct_path(parents, 3), [0, 2, 1, 3])

    def test_disconnected_graph(self):
        graph = {
            0: [(1, 10)],
            1: [],
            2: [(3, 1)],
            3: []
        }
        distances, _ = dijkstra(graph, 0)
        self.assertEqual(distances[2], float('inf'))

    def test_self_loop(self):
        graph = {
            0: [(0, 5), (1, 2)],
            1: []
        }
        distances, _ = dijkstra(graph, 0)
        self.assertEqual(distances[1], 2)

if __name__ == '__main__':
    unittest.main()
