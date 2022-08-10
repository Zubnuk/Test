import unittest

from determinant import determinant


class TestDeterminant(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertRaises(Exception, determinant, None)

    def test_first_order(self):
        matrix = [[1]]
        self.assertEqual(determinant(matrix), 1)

    def test_second_order(self):
        matrix = [[1, 2],
                  [3, 4]]
        self.assertEqual(determinant(matrix), -2)

    def test_third_order(self):
        matrix = [[1, -2, 3],
                  [-4, 5, -6],
                  [7, -8, 9]]
        self.assertEqual(determinant(matrix), 0)

    def test_fourth_order(self):
        matrix = [[3, -3, -5, 8],
                  [-3, 2, 4, -6],
                  [2, -5, -7, 5],
                  [-4, 3, 5, -6]]
        self.assertEqual(determinant(matrix), 18)

    def test_not_square_rectangle(self):
        matrix = [[3, -3, -5, 8],
                  [-3, 2, 4, -6],
                  [-4, 3, 5, -6]]
        self.assertRaises(Exception, determinant, matrix)

    def test_not_square_jag(self):
        matrix = [[3, -3, -5, 8],
                  [-3, 2, 4, -6],
                  [2, -5, -7],
                  [-4, 3, 5, -6]]
        self.assertRaises(Exception, determinant, matrix)


if __name__ == '__main__':
    unittest.main()
