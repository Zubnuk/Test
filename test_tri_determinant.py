import unittest

from main import tridiagonal_determinant
from custom_exception import ArgumentException


class TestTridiagonalDeterminant(unittest.TestCase):
    def test_none(self):
        self.assertRaisesRegex(ArgumentException,
                               'parameter is not a tridiagonal integer matrix',
                               tridiagonal_determinant, None)

    def test_empty_matrix(self):
        self.assertRaisesRegex(ArgumentException,
                               'parameter is not a tridiagonal integer matrix',
                               tridiagonal_determinant, [])

    def test_not_square_rectangle(self):
        matrix = [[1, 2, 0, 0],
                  [3, 1, 2, 0],
                  [0, 3, 1, 2]]
        self.assertRaisesRegex(ArgumentException,
                               'parameter is not a tridiagonal integer matrix',
                               tridiagonal_determinant, matrix)

    def test_not_square_jag(self):
        matrix = [[1, 2, 0, 0],
                  [3, 1, 2, 0],
                  [0, 3, 1],
                  [0, 0, 3, 1]]
        self.assertRaisesRegex(ArgumentException,
                               'parameter is not a tridiagonal integer matrix',
                               tridiagonal_determinant, matrix)

    def test_not_tridiag_replace_zero(self):
        matrix = [[1, 2, 0, 7],
                  [3, 1, 2, 0],
                  [0, 3, 1, 2],
                  [0, 0, 3, 1]]
        self.assertRaisesRegex(ArgumentException,
                               'parameter is not a tridiagonal integer matrix',
                               tridiagonal_determinant, matrix)

    def test_wrong_main_diag(self):
        matrix = [[1, 2, 0, 0],
                  [3, 7, 2, 0],
                  [0, 3, 1, 2],
                  [0, 0, 3, 1]]
        self.assertRaisesRegex(ArgumentException,
                               'parameter is not a tridiagonal integer matrix',
                               tridiagonal_determinant, matrix)

    def test_wrong_up_diag(self):
        matrix = [[1, 7, 0, 0],
                  [3, 1, 2, 0],
                  [0, 3, 1, 2],
                  [0, 0, 3, 1]]
        self.assertRaisesRegex(ArgumentException,
                               'parameter is not a tridiagonal integer matrix',
                               tridiagonal_determinant, matrix)

    def test_wrong_low_diag(self):
        matrix = [[1, 2, 0, 0],
                  [3, 1, 2, 0],
                  [0, 3, 1, 2],
                  [0, 0, 7, 1]]
        self.assertRaisesRegex(ArgumentException,
                               'parameter is not a tridiagonal integer matrix',
                               tridiagonal_determinant, matrix)

    def test_first_order(self):
        matrix = [[1]]
        self.assertEqual(tridiagonal_determinant(matrix), 1)

    def test_second_order(self):
        matrix = [[1, 2],
                  [2, 1]]
        self.assertEqual(tridiagonal_determinant(matrix), -3)

    def test_third_order(self):
        matrix = [[1, -2, 0],
                  [-4, 1, -2],
                  [0, -4, 1]]
        self.assertEqual(tridiagonal_determinant(matrix), -15)

    def test_fourth_order(self):
        matrix = [[2, -3, 0, 0],
                  [5, 2, -3, 0],
                  [0, 5, 2, -3],
                  [0, 0, 5, 2]]
        self.assertEqual(tridiagonal_determinant(matrix), 421)


if __name__ == '__main__':
    unittest.main()
