import unittest


from main import Schedule, ScheduleArgumentException
from task import Task


class TestSchedule(unittest.TestCase):
    def test_none_tasks(self):
        self.assertRaisesRegex(ScheduleArgumentException,
                               'Error during initialization of the Schedule '
                               'object! The tasks parameter is not a list',
                               Schedule.__init__, None, None, 1)

    def test_empty_tasks(self):
        self.assertRaisesRegex(ScheduleArgumentException,
                               'Error during initialization of the Schedule '
                               'object! The task list is empty',
                               Schedule.__init__, None, [], 1)

    def test_tasks_contains_non_task(self):
        tasks = [Task('a', 7), Task('b', 3), 'non task object']
        self.assertRaisesRegex(ScheduleArgumentException,
                               'Error during initialization of the Schedule '
                               'object! The task list contains not a Task '
                               'object in the position 2',
                               Schedule.__init__, None, tasks, 1)

    def test_single_task_single_executor(self):
        task_a = Task('a', 1)
        sched = Schedule([task_a], 1)
        executor1_schedule = '1. task: a from 0 to 1'
        self.assertEqual(tuple([task_a]), sched.tasks)
        self.assertEqual(1, sched.task_count)
        self.assertEqual(1, sched.executor_count)
        self.assertEqual(1, sched.duration)
        self.assertEqual(0, sched.downtime)
        self.assertEqual(0, sched.get_downtime_for_executor(0))
        self.assertEqual(executor1_schedule, sched.get_schedule_for_executor(0))

    def test_double_task_single_executor(self):
        task_a = Task('a', 2)
        task_b = Task('b', 1)
        sched = Schedule([task_a, task_b], 1)
        executor1_schedule = '1. task: a from 0 to 2\n' \
                             '2. task: b from 2 to 3'
        self.assertEqual(tuple([task_a, task_b]), sched.tasks)
        self.assertEqual(2, sched.task_count)
        self.assertEqual(1, sched.executor_count)
        self.assertEqual(3, sched.duration)
        self.assertEqual(0, sched.downtime)
        self.assertEqual(0, sched.get_downtime_for_executor(0))
        self.assertEqual(executor1_schedule, sched.get_schedule_for_executor(0))

    def test_triple_task_single_executor(self):
        task_a = Task('a', 1)
        task_b = Task('b', 3)
        task_c = Task('c', 5)
        sched = Schedule([task_a, task_b, task_c], 1)
        executor1_schedule = '1. task: a from 0 to 1\n' \
                             '2. task: b from 1 to 4\n' \
                             '3. task: c from 4 to 9'
        self.assertEqual(tuple([task_a, task_b, task_c]), sched.tasks)
        self.assertEqual(3, sched.task_count)
        self.assertEqual(1, sched.executor_count)
        self.assertEqual(9, sched.duration)
        self.assertEqual(0, sched.downtime)
        self.assertEqual(0, sched.get_downtime_for_executor(0))
        self.assertEqual(executor1_schedule, sched.get_schedule_for_executor(0))

    def test_single_task_double_executor(self):
        task_a = Task('a', 1)
        sched = Schedule([task_a], 2)
        executor1_schedule = '1. task: a from 0 to 1'
        executor2_schedule = '1. task: downtime from 0 to 1'
        self.assertEqual(2, sched.executor_count)
        self.assertEqual(1, sched.duration)
        self.assertEqual(1, sched.downtime)
        self.assertEqual(0, sched.get_downtime_for_executor(0))
        self.assertEqual(1, sched.get_downtime_for_executor(1))
        self.assertEqual(executor1_schedule, sched.get_schedule_for_executor(0))
        self.assertEqual(executor2_schedule, sched.get_schedule_for_executor(1))

    def test_double_task_double_executor(self):
        task_a = Task('a', 2)
        task_b = Task('b', 1)
        sched = Schedule([task_a, task_b], 2)
        executor1_schedule = '1. task: a from 0 to 2'
        executor2_schedule = '1. task: b from 0 to 1\n' \
                             '2. task: downtime from 1 to 2'
        self.assertEqual(2, sched.executor_count)
        self.assertEqual(2, sched.duration)
        self.assertEqual(1, sched.downtime)
        self.assertEqual(0, sched.get_downtime_for_executor(0))
        self.assertEqual(1, sched.get_downtime_for_executor(1))
        self.assertEqual(executor1_schedule, sched.get_schedule_for_executor(0))
        self.assertEqual(executor2_schedule, sched.get_schedule_for_executor(1))

    def test_triple_task_double_executor(self):
        task_a = Task('a', 2)
        task_b = Task('b', 4)
        task_c = Task('c', 6)
        sched = Schedule([task_a, task_b, task_c], 2)
        executor1_schedule = '1. task: a from 0 to 2\n' \
                             '2. task: b from 2 to 6'
        executor2_schedule = '1. task: c from 0 to 6'
        self.assertEqual(2, sched.executor_count)
        self.assertEqual(6, sched.duration)
        self.assertEqual(0, sched.downtime)
        self.assertEqual(0, sched.get_downtime_for_executor(0))
        self.assertEqual(0, sched.get_downtime_for_executor(1))
        self.assertEqual(executor1_schedule, sched.get_schedule_for_executor(0))
        self.assertEqual(executor2_schedule, sched.get_schedule_for_executor(1))

    def test_triple_task_triple_executor(self):
        task_a = Task('a', 2)
        task_b = Task('b', 4)
        task_c = Task('c', 6)
        sched = Schedule([task_a, task_b, task_c], 3)
        executor1_schedule = '1. task: a from 0 to 2\n' \
                             '2. task: b from 2 to 6'
        executor2_schedule = '1. task: c from 0 to 6'
        executor3_schedule = '1. task: downtime from 0 to 6'
        self.assertEqual(3, sched.executor_count)
        self.assertEqual(6, sched.duration)
        self.assertEqual(6, sched.downtime)
        self.assertEqual(0, sched.get_downtime_for_executor(0))
        self.assertEqual(0, sched.get_downtime_for_executor(1))
        self.assertEqual(6, sched.get_downtime_for_executor(2))
        self.assertEqual(executor1_schedule, sched.get_schedule_for_executor(0))
        self.assertEqual(executor2_schedule, sched.get_schedule_for_executor(1))
        self.assertEqual(executor3_schedule, sched.get_schedule_for_executor(2))

    def test_triple_equal_task_triple_executor(self):
        task_a = Task('a', 1)
        task_b = Task('b', 1)
        task_c = Task('c', 1)
        sched = Schedule([task_a, task_b, task_c], 3)
        executor1_schedule = '1. task: a from 0 to 1'
        executor2_schedule = '1. task: b from 0 to 1'
        executor3_schedule = '1. task: c from 0 to 1'
        self.assertEqual(3, sched.executor_count)
        self.assertEqual(1, sched.duration)
        self.assertEqual(0, sched.downtime)
        self.assertEqual(0, sched.get_downtime_for_executor(0))
        self.assertEqual(0, sched.get_downtime_for_executor(1))
        self.assertEqual(0, sched.get_downtime_for_executor(2))
        self.assertEqual(executor1_schedule, sched.get_schedule_for_executor(0))
        self.assertEqual(executor2_schedule, sched.get_schedule_for_executor(1))
        self.assertEqual(executor3_schedule, sched.get_schedule_for_executor(2))

    def test_triple_has_large_task_triple_executor(self):
        task_a = Task('a', 1)
        task_b = Task('b', 1)
        task_c = Task('c', 10)
        sched = Schedule([task_a, task_b, task_c], 3)
        executor1_schedule = '1. task: a from 0 to 1\n' \
                             '2. task: b from 1 to 2\n' \
                             '3. task: c from 2 to 10'
        executor2_schedule = '1. task: c from 0 to 2\n' \
                             '2. task: downtime from 2 to 10'
        executor3_schedule = '1. task: downtime from 0 to 10'
        self.assertEqual(10, sched.duration)
        self.assertEqual(18, sched.downtime)
        self.assertEqual(0, sched.get_downtime_for_executor(0))
        self.assertEqual(8, sched.get_downtime_for_executor(1))
        self.assertEqual(10, sched.get_downtime_for_executor(2))
        self.assertEqual(executor1_schedule, sched.get_schedule_for_executor(0))
        self.assertEqual(executor2_schedule, sched.get_schedule_for_executor(1))
        self.assertEqual(executor3_schedule, sched.get_schedule_for_executor(2))

    def test_complex(self):
        tasks = [Task('a', 3), Task('b', 4), Task('c', 6), Task('d', 7),
                 Task('e', 7), Task('f', 9), Task('g', 10), Task('h', 12),
                 Task('i', 17)]
        sched = Schedule(tasks, 5)
        executor1_schedule = '1. task: a from 0 to 3\n' \
                             '2. task: b from 3 to 7\n' \
                             '3. task: c from 7 to 13\n' \
                             '4. task: d from 13 to 17'
        executor2_schedule = '1. task: d from 0 to 3\n' \
                             '2. task: e from 3 to 10\n' \
                             '3. task: f from 10 to 17'
        executor3_schedule = '1. task: f from 0 to 2\n' \
                             '2. task: g from 2 to 12\n' \
                             '3. task: h from 12 to 17'
        executor4_schedule = '1. task: h from 0 to 7\n' \
                             '2. task: i from 7 to 17'
        executor5_schedule = '1. task: i from 0 to 7\n' \
                             '2. task: downtime from 7 to 17'
        self.assertEqual(tuple(tasks), sched.tasks)
        self.assertEqual(9, sched.task_count)
        self.assertEqual(5, sched.executor_count)
        self.assertEqual(17, sched.duration)
        self.assertEqual(10, sched.downtime)
        self.assertEqual(0, sched.get_downtime_for_executor(0))
        self.assertEqual(0, sched.get_downtime_for_executor(1))
        self.assertEqual(0, sched.get_downtime_for_executor(2))
        self.assertEqual(0, sched.get_downtime_for_executor(3))
        self.assertEqual(10, sched.get_downtime_for_executor(4))
        self.assertEqual(executor1_schedule, sched.get_schedule_for_executor(0))
        self.assertEqual(executor2_schedule, sched.get_schedule_for_executor(1))
        self.assertEqual(executor3_schedule, sched.get_schedule_for_executor(2))
        self.assertEqual(executor4_schedule, sched.get_schedule_for_executor(3))
        self.assertEqual(executor5_schedule, sched.get_schedule_for_executor(4))


if __name__ == '__main__':
    unittest.main()
