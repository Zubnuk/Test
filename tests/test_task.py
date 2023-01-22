import unittest
from task import Task
from custom_exception import TaskArgumentException


class TestTask(unittest.TestCase):
    name = 'a'
    duration = 1
    task = Task(name, duration)

    def test_init_none_name(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task '
                               'object! The task name is not a string',
                               Task.__init__, None, None, self.duration)

    def test_init_int_name(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task '
                               'object! The task name is not a string',
                               Task.__init__, None, 0, self.duration)

    def test_init_empty_name(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task '
                               'object! The task name is empty',
                               Task.__init__, None, '', self.duration)

    def test_init_empty_duration(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task object!'
                               ' The duration parameter is not an integer',
                               Task.__init__, None, self.name, None)

    def test_init_not_int_duration(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task object!'
                               ' The duration parameter is not an integer',
                               Task.__init__, None, self.name, '1')

    def test_init_negative_duration(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task object!'
                               ' The duration parameter value is less than 1',
                               Task.__init__, None, self.name, -1)

    def test_init_zero_duration(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task object!'
                               ' The duration parameter value is less than 1',
                               Task.__init__, None, self.name, 0)

    def test_str(self):
        self.assertEqual(str(self.task),
                         f'task: {self.name}, duration: {self.duration}')

    def test_name_property(self):
        self.assertEqual(self.task.name, self.name)

    def test_duration_property(self):
        self.assertEqual(self.task.duration, self.duration)


if __name__ == '__main__':
    unittest.main()
