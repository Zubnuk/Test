import unittest


from main import _ScheduleTask, ScheduleArgumentException,\
    InternalScheduleException
from task import Task


class TestScheduleTask(unittest.TestCase):
    name = 'a'
    stage1 = 1
    stage2 = 2
    task = Task(name, stage1, stage2)
    sched_task = _ScheduleTask(task)

    def test_none_task(self):
        self.assertRaisesRegex(ScheduleArgumentException,
                               'Error during initialization of the Schedule '
                               'object! The task parameter is not a Task',
                               _ScheduleTask.__init__, None, None)

    def test_wrong_type(self):
        self.assertRaisesRegex(ScheduleArgumentException,
                               'Error during initialization of the Schedule '
                               'object! The task parameter is not a Task',
                               _ScheduleTask.__init__, None, 'string')

    def test_task_property(self):
        self.assertEqual(self.sched_task.task, self.task)

    def test_keys_to_sort_zero_first_key(self):
        task = _ScheduleTask(Task('a', 1, 2))
        self.assertEqual(tuple((0, 1)), task.keys_to_sort)

    def test_keys_to_sort_one_first_key(self):
        task = _ScheduleTask(Task('a', 2, 1))
        self.assertEqual(tuple((1, -1)), task.keys_to_sort)

    def test_stage1_start_property_not_init(self):
        task = _ScheduleTask(Task('a', 2, 1))
        self.assertIsNone(task.stage1_start)

    def test_stage1_start_property_none(self):
        with self.assertRaisesRegex(InternalScheduleException,
                                    'Error during processing '
                                    f'task {self.task.name}! The stage1 start '
                                    'time is not an integer'):
            self.sched_task.stage1_start = None

    def test_stage1_start_property_str(self):
        with self.assertRaisesRegex(InternalScheduleException,
                                    'Error during processing '
                                    f'task {self.task.name}! The stage1 start '
                                    'time is not an integer'):
            self.sched_task.stage1_start = 'string'

    def test_stage1_start_property_negative(self):
        with self.assertRaisesRegex(InternalScheduleException,
                                    'Error during processing '
                                    f'task {self.task.name}! The stage1 start '
                                    'time is less than 0'):
            self.sched_task.stage1_start = - 1

    def test_stage1_start_property(self):
        self.sched_task.stage1_start = 1
        self.assertEqual(1, self.sched_task.stage1_start)

    def test_stage1_end_property(self):
        self.sched_task.stage1_start = 1
        self.assertEqual(1 + self.stage1, self.sched_task.stage1_end)

    def test_stage2_start_property_not_init(self):
        task = _ScheduleTask(Task('a', 2, 1))
        self.assertIsNone(task.stage2_start)

    def test_stage2_start_property_none(self):
        with self.assertRaisesRegex(InternalScheduleException,
                                    'Error during processing '
                                    f'task {self.task.name}! The stage2 start '
                                    'time is not an integer'):
            self.sched_task.stage2_start = None

    def test_stage2_start_property_str(self):
        with self.assertRaisesRegex(InternalScheduleException,
                                    'Error during processing '
                                    f'task {self.task.name}! The stage2 start '
                                    'time is not an integer'):
            self.sched_task.stage2_start = 'string'

    def test_stage2_start_property_less_than_stage1(self):
        with self.assertRaisesRegex(InternalScheduleException,
                                    'Error during processing '
                                    f'task {self.task.name}! The stage2 start '
                                    'time is less than the stage1 end time'):
            self.sched_task.stage1_start = 2
            self.sched_task.stage2_start = 2

    def test_stage2_start_property(self):
        self.sched_task.stage1_start = 1
        self.sched_task.stage2_start = 2
        self.assertEqual(2, self.sched_task.stage2_start)

    def test_stage2_end_property(self):
        self.sched_task.stage1_start = 0
        self.sched_task.stage2_start = 1
        self.assertEqual(self.stage1 + self.stage2, self.sched_task.stage2_end)


if __name__ == '__main__':
    unittest.main()
