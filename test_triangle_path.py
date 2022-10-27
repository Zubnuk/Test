import unittest

from main import get_triangle_path_count
from custom_exception import ArgumentException


class TestTrianglePath(unittest.TestCase):
    @staticmethod
    def __calculate_result(length):
        return 1/3 * 2**length + 2/3 * (-1)**length

    def test_none(self):
        self.assertRaisesRegex(ArgumentException,
                               'The parameter length must be an integer '
                               'greater than 0',
                               get_triangle_path_count, None)

    def test_zero(self):
        self.assertRaisesRegex(ArgumentException,
                               'The parameter length must be an integer '
                               'greater than 0',
                               get_triangle_path_count, 0)

    def test_negative(self):
        self.assertRaisesRegex(ArgumentException,
                               'The parameter length must be an integer '
                               'greater than 0',
                               get_triangle_path_count, -1)

    def test_not_int(self):
        self.assertRaisesRegex(ArgumentException,
                               'The parameter length must be an integer '
                               'greater than 0',
                               get_triangle_path_count, 1.1)

    def test_triangle_path(self):
        for i in range(1, 10):
            self.assertEqual(get_triangle_path_count(i),
                             TestTrianglePath.__calculate_result(i))


if __name__ == '__main__':
    unittest.main()
