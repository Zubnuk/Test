import unittest

from main import dijkstra_algorithm


class TestDijkstra(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertRaises(Exception, dijkstra_algorithm, None, 0, 1)

    def test_has_negative(self):
        matrix = [[3, 3],
                  [3, -2]]
        self.assertRaises(Exception, dijkstra_algorithm, matrix, 0, 1)

    def test_src_out_of_range(self):
        matrix = [[3, 3],
                  [3, 2]]
        self.assertRaises(Exception, dijkstra_algorithm, matrix, 2, 1)

    def test_trg_out_of_range(self):
        matrix = [[3, 3],
                  [3, 2]]
        self.assertRaises(Exception, dijkstra_algorithm, matrix, 1, 2)

    def test_not_square_rectangle(self):
        matrix = [[3, 3, 5],
                  [3, 2, 4]]
        self.assertRaises(Exception, dijkstra_algorithm, matrix, 1)

    def test_not_square_jag(self):
        matrix = [[3, 3, 5, 8],
                  [3, 2, 4, 6],
                  [2, 5, 7]]
        self.assertRaises(Exception, dijkstra_algorithm, matrix, 1)

    def test_single(self):
        matrix = [[1]]
        self.assertEqual(dijkstra_algorithm(matrix, 0, 0), {'weight': 1,
                                                            'path': [0]})

    def test_double(self):
        matrix = [[None, 1],
                  [None, None]]
        self.assertEqual(dijkstra_algorithm(matrix, 0, 1), {'weight': 1,
                                                            'path': [0, 1]})

    def test_1(self):
        matrix = [[0, 2, None, 3, None, None],
                  [None, 0, 1, None, 4, None],
                  [None, None, 0, None, None, 5],
                  [None, None, None, 0, 2, None],
                  [None, None, None, None, 0, 1],
                  [None, None, None, None, None, 0]]
        self.assertEqual(dijkstra_algorithm(matrix, 0, 5),
                         {'weight': 6, 'path': [0, 3, 4, 5]})


if __name__ == '__main__':
    unittest.main()
