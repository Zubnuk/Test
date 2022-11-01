import unittest


from task import Task, TaskArgumentException


class TestTask(unittest.TestCase):
    name = 'a'
    stage1 = 1
    stage2 = 2
    task = Task(name, stage1, stage2)

    def test_init_none_name(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task '
                               'object! The task name is not a string',
                               Task.__init__, None, None, 0, 1)

    def test_init_int_name(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task '
                               'object! The task name is not a string',
                               Task.__init__, None, 0, 0, 1)

    def test_init_empty_name(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task '
                               'object! The task name is empty',
                               Task.__init__, None, '', 0, 1)

    def test_init_empty_stage1(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task '
                               'object! The stage1 parameter is not an integer',
                               Task.__init__, None, 'a', None, 1)

    def test_init_not_int_stage1(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task '
                               'object! The stage1 parameter is not an integer',
                               Task.__init__, None, 'a', '1', 1)

    def test_init_negative_stage1(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task object!'
                               ' The stage1 parameter value is less than 1',
                               Task.__init__, None, 'a', -1, 1)

    def test_init_zero_stage1(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task object!'
                               ' The stage1 parameter value is less than 1',
                               Task.__init__, None, 'a', 0, 1)

    def test_init_empty_stage2(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task '
                               'object! The stage2 parameter is not an integer',
                               Task.__init__, None, 'a', 1, None)

    def test_init_not_int_stage2(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task '
                               'object! The stage2 parameter is not an integer',
                               Task.__init__, None, 'a', 1, '1')

    def test_init_negative_stage2(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task object!'
                               ' The stage2 parameter value is less than 1',
                               Task.__init__, None, 'a', 1, -1)

    def test_init_zero_stage2(self):
        self.assertRaisesRegex(TaskArgumentException,
                               'Error during initialization of the Task object!'
                               ' The stage2 parameter value is less than 1',
                               Task.__init__, None, 'a', 1, 0)

    def test_str(self):
        self.assertEqual(str(self.task), 'task: a, duration: 1/2')

    def test_name_property(self):
        self.assertEqual(self.task.name, self.name)

    def test_stage1_property(self):
        self.assertEqual(self.task.stage1, self.stage1)

    def test_stage2_property(self):
        self.assertEqual(self.task.stage2, self.stage2)


if __name__ == '__main__':
    unittest.main()
