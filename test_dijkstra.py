import unittest

from main import get_shortest_path_dijkstra


class TestDijkstra(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertRaises(Exception, get_shortest_path_dijkstra, None, 0, 1)

    def test_has_negative(self):
        matrix = [[3, 3],
                  [3, -2]]
        self.assertRaises(Exception, get_shortest_path_dijkstra, matrix, 0, 1)

    def test_src_out_of_range(self):
        matrix = [[3, 3],
                  [3, 2]]
        self.assertRaises(Exception, get_shortest_path_dijkstra, matrix, 2, 1)

    def test_trg_out_of_range(self):
        matrix = [[3, 3],
                  [3, 2]]
        self.assertRaises(Exception, get_shortest_path_dijkstra, matrix, 1, 2)

    def test_not_square_rectangle(self):
        matrix = [[3, 3, 5],
                  [3, 2, 4]]
        self.assertRaises(Exception, get_shortest_path_dijkstra, matrix, 1, 2)

    def test_not_square_jag(self):
        matrix = [[3, 3, 5, 8],
                  [3, 2, 4, 6],
                  [2, 5, 7]]
        self.assertRaises(Exception, get_shortest_path_dijkstra, matrix, 1, 2)

    def test_single(self):
        matrix = [[1]]
        self.assertRaises(Exception, get_shortest_path_dijkstra, matrix, 0, 0)

    def test_double(self):
        matrix = [[None, 1],
                  [None, None]]
        self.assertEqual(get_shortest_path_dijkstra(matrix, 0, 1),
                         {'distance': 1, 'path': [0, 1]})

    def test_disconnected(self):
        matrix = [[0, 1, None, None],
                  [None, 0, 1, None],
                  [None, None, 0, None],
                  [None, None, None, 0]]
        self.assertEqual(get_shortest_path_dijkstra(matrix, 0, 3),
                         {'distance': None, 'path': []})

    def test_revers_order(self):
        matrix = [[0, None, None],
                  [1, 0, None],
                  [None, 1, 0]]
        self.assertEqual(get_shortest_path_dijkstra(matrix, 0, 2),
                         {'distance': None, 'path': []})

    def test_1(self):
        matrix = [[0, 2, None, 3, None, None],
                  [None, 0, 1, None, 4, None],
                  [None, None, 0, None, None, 5],
                  [None, None, None, 0, 2, None],
                  [None, None, None, None, 0, 1],
                  [None, None, None, None, None, 0]]
        self.assertEqual(get_shortest_path_dijkstra(matrix, 0, 5),
                         {'distance': 6, 'path': [0, 3, 4, 5]})

    def test_2(self):
        matrix = [[0, 10, 30, 50, 10],
                  [None, 0, None, None, None],
                  [None, None, 0, None, 10],
                  [None, 40, 20, 0, None],
                  [10, None, 10, 30, 0]]
        self.assertEqual(get_shortest_path_dijkstra(matrix, 0, 3),
                         {'distance': 40, 'path': [0, 4, 3]})

    def test_3(self):
        matrix = [[0, 7, 9, None, None, 14],
                  [7, 0, 10, 15, None, None],
                  [9, 10, 0, 11, None, 2],
                  [None, 15, 11, 0, 6, None],
                  [None, None, None, 6, 0, 9],
                  [14, None, 2, None, 9, 0]]
        self.assertEqual(get_shortest_path_dijkstra(matrix, 0, 5),
                         {'distance': 11, 'path': [0, 2, 5]})


if __name__ == '__main__':
    unittest.main()
