import unittest

from main import ScheduleRow
from custom_exception import ScheduleArgumentException


class TestScheduleRow(unittest.TestCase):
    def test_init_none_name(self):
        self.assertRaisesRegex(ScheduleArgumentException,
                               'Error during initialization of the Schedule '
                               'object! The task_name parameter is not a '
                               'string',
                               ScheduleRow.__init__, None, 0, 1, None)

    def test_init_not_none_name_downtime(self):
        self.assertRaisesRegex(ScheduleArgumentException,
                               'Error during initialization of the Schedule '
                               'object! The task_name parameter for downtime '
                               'period is not empty',
                               ScheduleRow.__init__, None, 0, 1, 'a', True)

    def test_init_not_str_name(self):
        self.assertRaisesRegex(ScheduleArgumentException,
                               'Error during initialization of the Schedule '
                               'object! The task_name parameter is not a '
                               'string',
                               ScheduleRow.__init__, None, 0, 1, 0)

    def test_init_empty_str_name(self):
        self.assertRaisesRegex(ScheduleArgumentException,
                               'Error during initialization of the Schedule '
                               'object! The task_name parameter is empty',
                               ScheduleRow.__init__, None, 0, 1, '')

    def test_init_not_number_start(self):
        self.assertRaisesRegex(ScheduleArgumentException,
                               'Error during initialization of the Schedule '
                               'object! The start parameter is not a number',
                               ScheduleRow.__init__, None, 'str', 1, 'a')

    def test_init_negative_start(self):
        self.assertRaisesRegex(ScheduleArgumentException,
                               'Error during initialization of the Schedule '
                               'object! The start parameter is less than zero',
                               ScheduleRow.__init__, None, -1, 1, 'a')

    def test_init_not_number_duration(self):
        self.assertRaisesRegex(ScheduleArgumentException,
                               'Error during initialization of the Schedule '
                               'object! The duration parameter is not a number',
                               ScheduleRow.__init__, None, 0, 'str', 'a')

    def test_init_zero_duration(self):
        self.assertRaisesRegex(ScheduleArgumentException,
                               'Error during initialization of the Schedule '
                               'object! The duration parameter is less or '
                               'equal than zero',
                               ScheduleRow.__init__, None, 0, 0, 'a')

    def test_init_negative_duration(self):
        self.assertRaisesRegex(ScheduleArgumentException,
                               'Error during initialization of the Schedule '
                               'object! The duration parameter is less or '
                               'equal than zero',
                               ScheduleRow.__init__, None, 1, -1, 'a')

    def test_init_integers(self):
        task_name = 'task'
        start = 0
        duration = 1
        row = ScheduleRow(start, duration, task_name)
        self.assertEqual(row.task_name, task_name)
        self.assertEqual(start, row.start)
        self.assertEqual(duration, row.duration)
        self.assertEqual(start + duration, row.end)
        self.assertFalse(row.is_downtime)
        self.assertEqual(f'task {task_name} from {start} to {start + duration}',
                         str(row))

    def test_init_floats_downtime(self):
        start = 1.1
        duration = 0.25
        row = ScheduleRow(start, duration, is_downtime=True)
        self.assertEqual('downtime', row.task_name)
        self.assertEqual(start, row.start)
        self.assertEqual(duration, row.duration)
        self.assertEqual(start + duration, row.end)
        self.assertTrue(row.is_downtime)
        self.assertEqual(f'task downtime from {start} to {start + duration}',
                         str(row))

    def test_str(self):
        task_name = 'task'
        start = 0
        duration = 1
        self.assertEqual(f'task {task_name} from {start} to {start + duration}',
                         str(ScheduleRow(start, duration, task_name)))

    def test_str_downtime(self):
        start = 1.1
        duration = 10
        self.assertEqual(f'task downtime from {start} to {start + duration}',
                         str(ScheduleRow(start, duration, is_downtime=True)))


if __name__ == '__main__':
    unittest.main()
