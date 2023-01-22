import unittest

from main import create_timetable
from custom_exception import ArgumentException

class MyTestCase(unittest.TestCase):
    def test_max_more_avg(self):
        self.assertCountEqual(create_timetable(5, [3, 4, 14, 6, 7]), [[1, 'A', 0, 3.0],
                                                                      [1, 'B', 3.0, 7.0],
                                                                      [1, 'C', 7.0, 14.0],
                                                                      [2, 'C', 0, 7.0],
                                                                      [2, 'D', 7.0, 13.0],
                                                                      [2, 'E', 13.0, 14.0],
                                                                      [3, 'E', 0, 6.0]])

    def test_max_less_avg(self):
        self.assertCountEqual(create_timetable(3, [4, 2, 5, 4, 2]), [
            [1, 'A', 0, 4.0],
            [1, 'B', 4.0, 5.6667],
            [2, 'B', 0, 0.3333],
            [2, 'C', 0.3333, 5.3333],
            [2, 'D', 5.3333, 5.6667],
            [3, 'D', 0, 3.6667],
            [3, 'E', 3.6667, 5.6667]])

    def test_float(self):
        self.assertCountEqual(create_timetable(3, [1, 1, 1, 1]), [
            [1, 'A', 0, 1.0],
            [1, 'B', 1.0, 1.3333],
            [2, 'B', 0, 0.6667],
            [2, 'C', 0.6667, 1.3333],
            [3, 'C', 0, 0.3333],
            [3, 'D', 0.3333, 1.3333]])

    def test_one_employees(self):
        self.assertCountEqual(create_timetable(1, [5, 3, 2]),[
            [1, 'A', 0, 5.0],
            [1, 'B', 5.0, 8.0],
            [1, 'C', 8.0, 10.0]])

    def test_zero_employees(self):
        self.assertRaisesRegex(ArgumentException,
                               'The number of employees must be an integer more than zero',
                               create_timetable, 0, [5, 6, 3])

    def test_float_employees(self):
        self.assertRaisesRegex(ArgumentException, 'The number of employees must be an integer more than zero',
                               create_timetable, 4.5, [5, 6, 3])

    def test_negative_employees(self):
        self.assertRaisesRegex(ArgumentException, 'The number of employees must be an integer more than zero',
                               create_timetable, -1, [5, 6, 3])

    def test_negative_work_length(self):
        self.assertRaisesRegex(ArgumentException, 'The length of work must be a number more than 0',
                               create_timetable, 4, [-5, 6, 3])

    def test_zero_work_length(self):
        self.assertRaisesRegex(ArgumentException, 'The length of work must be a number more than 0',
                               create_timetable, 4, [1, 0, 3])