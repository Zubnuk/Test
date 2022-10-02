import unittest

from main import invest_distribution
from custom_exception import ArgumentException


class TestDistribution(unittest.TestCase):
    def test_none(self):
        self.assertRaisesRegex(ArgumentException,
                               'parameter is not an integer rectangle matrix',
                               invest_distribution, None)

    def test_empty(self):
        self.assertRaisesRegex(ArgumentException,
                               'parameter is not an integer rectangle matrix',
                               invest_distribution, [])

    def test_jag_matrix(self):
        matrix = [[15, 18, 16, 17],
                  [20, 22, 23]]
        self.assertRaisesRegex(ArgumentException,
                               'parameter is not an integer rectangle matrix',
                               invest_distribution, matrix)

    def test_has_str(self):
        matrix = [[15, 18, 16],
                  [20, 22, 'str']]
        self.assertRaisesRegex(ArgumentException,
                               'parameter is not an integer rectangle matrix',
                               invest_distribution, matrix)

    def test_single_value(self):
        matrix = [[1]]
        result = invest_distribution(matrix)
        self.assertEqual(result['profit'], 1)
        self.assertEqual(result['parts'], [1])

    def test_single_level(self):
        matrix = [[1, 2]]
        result = invest_distribution(matrix)
        self.assertEqual(result['profit'], 2)
        self.assertEqual(result['parts'], [0, 1])

    def test_multi_level(self):
        matrix = [[1, 2],
                  [3, 5]]
        result = invest_distribution(matrix)
        self.assertEqual(result['profit'], 5)
        self.assertEqual(result['parts'], [0, 2])

    def test_1(self):
        matrix = [[15, 18, 16, 17],
                  [20, 22, 23, 19],
                  [26, 28, 27, 25],
                  [34, 33, 29, 31],
                  [40, 39, 41, 37]]
        result = invest_distribution(matrix)
        self.assertEqual(result['profit'], 73)
        self.assertEqual(result['parts'], [1, 1, 2, 1])

    def test_2(self):
        matrix = [[5, 7, 2, 10],
                  [9, 8, 4, 15],
                  [11, 10, 5, 16],
                  [12, 12, 8, 17],
                  [14, 15, 9, 18]]
        result = invest_distribution(matrix)
        self.assertEqual(result['profit'], 31)
        self.assertEqual(result['parts'], [2, 1, 0, 2])

    def test_3(self):
        matrix = [[5, 3, 7, 6],
                  [9, 10, 11, 12],
                  [17, 21, 23, 16],
                  [28, 35, 32, 29],
                  [43, 41, 40, 43]]
        result = invest_distribution(matrix)
        self.assertEqual(result['profit'], 43)
        self.assertEqual(result['parts'], [0, 0, 0, 5])


if __name__ == '__main__':
    unittest.main()
