import unittest

from main import generate_strings
from custom_exception import ArgumentException


class TestZeroOne(unittest.TestCase):
    @staticmethod
    def __get_strings_to_check(length):
        if length == 0:
            return []
        return [('0'*length + str(bin(i))[2:])[-length:]
                for i in range(2**length)
                if '00' not in ('0'*length + str(bin(i))[2:])[-length:]]

    def test_negative(self):
        self.assertRaisesRegex(ArgumentException,
                               'The parameter must be integer equal or greater '
                               'than zero',
                               generate_strings, -1)

    def test_none(self):
        self.assertRaisesRegex(ArgumentException,
                               'The parameter must be integer equal or greater '
                               'than zero',
                               generate_strings, None)

    def test_not_int(self):
        self.assertRaisesRegex(ArgumentException,
                               'The parameter must be integer equal or greater '
                               'than zero',
                               generate_strings, 1.1)

    def test_zero_one(self):
        for i in range(20):
            self.assertCountEqual(generate_strings(i),
                                  TestZeroOne.__get_strings_to_check(i))


if __name__ == '__main__':
    unittest.main()
