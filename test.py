import unittest

from main import main


class MyTestCase(unittest.TestCase):
    def more_tasks(self):
        self.assertCountEqual(main(3, 6, [['A', 1], ['B', 2], ['C', 3], ['D', 4], ['E', 5], ['F', 6]]), 
        [
            [['A', 1.0], ['B', 2.0], ['C', 3.0], ['D', 1.0]], 
            [['D', 3.0], ['E', 4.0]], 
            [['E', 1.0], ['F', 6.0]]])

    def more_executors(self):
        self.assertCountEqual(main(6, 3, [['A', 1], ['B', 2], ['C', 3]]), 
        [
            [['A', 1.0], ['B', 2.0]], 
            [['C', 3.0]]
            ])

    def float_tasks(self):
        self.assertCountEqual(main(10, 10, [['A', 1.1], ['B', 1.2], ['C', 1.3], ['D', 1.4], ['E', 1.5], ['F', 1.6], ['G', 1.7], ['H', 1.8], ['I', 1.9], ['J', 2.0]]), 
        [
            [['A', 1.1], ['B', 0.9]], 
            [['B', 0.3], ['C', 1.3], ['D', 0.4]], 
            [['D', 1.0], ['E', 1.0]], 
            [['E', 0.5], ['F', 1.5]], 
            [['F', 0.1], ['G', 1.7], ['H', 0.2]], 
            [['H', 1.6], ['I', 0.4]], 
            [['I', 1.5], ['J', 0.5]], 
            [['J', 1.5]]])

    def one_executor(self):
        self.assertCountEqual(main(1, 10, [['A', 1.0], ['B', 2.0], ['C', 3.0], ['D', 4.0], ['E', 5.0], ['F', 6.0], ['G', 7.0], ['H', 8.0], ['I', 9.0], ['J', 10.0]]), 
        [
            [['A', 1.0], ['B', 2.0], ['C', 3.0], ['D', 4.0], ['E', 5.0], ['F', 6.0], ['G', 7.0], ['H', 8.0], ['I', 9.0], ['J', 10.0]]
            ])

    def test_less_zero_employees(self):
        self.assertRaisesRegex(Exception,
                               'количество исполнителей <= 0',
                               main, -1, 1,  [['A', 1]])

    def test_less_zero_tasks(self):
        self.assertRaisesRegex(Exception,
                               'количество работ <= 0',
                               main, 1, -1,  [['A', 1]])

    def test_less_zero_tasks_len(self):
        self.assertRaisesRegex(Exception,
                               'длительность работ A <= 0',
                               main, 1, 1,  [['A', -1]])