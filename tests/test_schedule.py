import unittest

from main import create_schedule, TASK, PART

class TestSchedule(unittest.TestCase):
    def test_none_tasks(self):
        self.assertRaisesRegex(ValueError, 'Error during initialization of the Schedule object! The tasks parameter is not a list',
                               create_schedule, None, 1)

    def test_empty_tasks(self):
        self.assertRaisesRegex(ValueError, 'Error during initialization of the Schedule object! The task list is empty',
                               create_schedule, [], 1)

    def test_tasks_contains_non_task(self):
        tasks = [['a', 7], ['b', 3], 'non task object']
        self.assertRaisesRegex(ValueError, 'Error during initialization of the Schedule '
                               'object! The task list contains not a list '
                               'object in the position 2',
                               create_schedule, tasks, 1)

    def test_get_schedule_for_executor_not_int(self):
        self.assertRaisesRegex(ValueError, 'Invalid type of executors amount',
                               create_schedule, [['a', 1]], '5')

    def test_get_schedule_for_executor_less_than_one(self):
        self.assertRaisesRegex(ValueError, 'Invalid executors amount number',
                               create_schedule, [['a', 1]], -1)

    def test_private_single__executor_tasks(self):
        task_a = ['a', 2]
        task_b = ['b', 1]
        sched = create_schedule([task_a, task_b], 1)
        executor_schedules = sched['executor_tasks']
        executor1_schedule = [{TASK: task_a, PART: 2}, {TASK: task_b, PART: 1}]
        self.assertEqual(executor1_schedule, executor_schedules[0])

    def test_private_double__executor_tasks(self):
        task_a = ['a', 2]
        task_b = ['b', 1]
        sched = create_schedule([task_a, task_b], 2)
        executor_schedules = sched['executor_tasks']
        executor1_schedule = [{TASK: task_a, PART: 2}]
        executor2_schedule = [{TASK: task_b, PART: 1}]
        self.assertEqual(executor1_schedule, executor_schedules[0])
        self.assertEqual(executor2_schedule, executor_schedules[1])

    def test_single_task_single_executor(self):
        task_a = ['a', 1]
        sched = create_schedule([task_a], 1)
        executor1_schedule = '1. task: a from 0 to 1'
        self.assertEqual(tuple([task_a]), sched['tasks'])
        self.assertEqual(1, sched['tasks amount'])
        self.assertEqual(1, sched['executors'])
        self.assertEqual(1, sched['duration'])
        self.assertEqual(0, sched['downtime'])
        self.assertEqual(0, sched['downtime executor 1'])
        self.assertEqual(executor1_schedule, sched[1])

    def test_double_task_single_executor(self):
        task_a = ['a', 2]
        task_b = ['b', 1]
        sched = create_schedule([task_a, task_b], 1)
        executor1_schedule = '1. task: a from 0 to 2\n' \
                             '2. task: b from 2 to 3'
        self.assertEqual(tuple([task_a, task_b]), sched['tasks'])
        self.assertEqual(2, sched['tasks amount'])
        self.assertEqual(1, sched['executors'])
        self.assertEqual(3, sched['duration'])
        self.assertEqual(0, sched['downtime'])
        self.assertEqual(0, sched['downtime executor 1'])
        self.assertEqual(executor1_schedule, sched[1])

    def test_triple_task_single_executor(self):
        task_a = ['a', 1]
        task_b = ['b', 3]
        task_c = ['c', 5]
        sched = create_schedule([task_a, task_b, task_c], 1)
        executor1_schedule = '1. task: a from 0 to 1\n' \
                             '2. task: b from 1 to 4\n' \
                             '3. task: c from 4 to 9'
        self.assertEqual(tuple([task_a, task_b, task_c]), sched['tasks'])
        self.assertEqual(3, sched['tasks amount'])
        self.assertEqual(1, sched['executors'])
        self.assertEqual(9, sched['duration'])
        self.assertEqual(0, sched['downtime'])
        self.assertEqual(0, sched['downtime executor 1'])
        self.assertEqual(executor1_schedule, sched[1])

    def test_single_task_double_executor(self):
        task_a = ['a', 1]
        sched = create_schedule([task_a], 2)
        executor1_schedule = '1. task: a from 0 to 1'
        executor2_schedule = '1. task: downtime from 0 to 1'
        self.assertEqual(2, sched['executors'])
        self.assertEqual(1, sched['duration'])
        self.assertEqual(1, sched['downtime'])
        self.assertEqual(0, sched['downtime executor 1'])
        self.assertEqual(1, sched['downtime executor 2'])
        self.assertEqual(executor1_schedule, sched[1])
        self.assertEqual(executor2_schedule, sched[2])

    def test_double_task_double_executor(self):
        task_a = ['a', 2]
        task_b = ['b', 1]
        sched = create_schedule([task_a, task_b], 2)
        executor1_schedule = '1. task: a from 0 to 2'
        executor2_schedule = '1. task: b from 0 to 1\n' \
                             '2. task: downtime from 1 to 2'
        self.assertEqual(2, sched['executors'])
        self.assertEqual(2, sched['duration'])
        self.assertEqual(1, sched['downtime'])
        self.assertEqual(0, sched['downtime executor 1'])
        self.assertEqual(1, sched['downtime executor 2'])
        self.assertEqual(executor1_schedule, sched[1])
        self.assertEqual(executor2_schedule, sched[2])

    def test_triple_task_double_executor(self):
        task_a = ['a', 2]
        task_b = ['b', 4]
        task_c = ['c', 6]
        sched = create_schedule([task_a, task_b, task_c], 2)
        executor1_schedule = '1. task: a from 0 to 2\n' \
                             '2. task: b from 2 to 6'
        executor2_schedule = '1. task: c from 0 to 6'
        self.assertEqual(2, sched['executors'])
        self.assertEqual(6, sched['duration'])
        self.assertEqual(0, sched['downtime'])
        self.assertEqual(0, sched['downtime executor 1'])
        self.assertEqual(0, sched['downtime executor 2'])
        self.assertEqual(executor1_schedule, sched[1])
        self.assertEqual(executor2_schedule, sched[2])

    def test_triple_task_triple_executor(self):
        task_a = ['a', 2]
        task_b = ['b', 4]
        task_c = ['c', 6]
        sched = create_schedule([task_a, task_b, task_c], 3)
        executor1_schedule = '1. task: a from 0 to 2\n' \
                             '2. task: b from 2 to 6'
        executor2_schedule = '1. task: c from 0 to 6'
        executor3_schedule = '1. task: downtime from 0 to 6'
        self.assertEqual(3, sched['executors'])
        self.assertEqual(6, sched['duration'])
        self.assertEqual(6, sched['downtime'])
        self.assertEqual(0, sched['downtime executor 1'])
        self.assertEqual(0, sched['downtime executor 2'])
        self.assertEqual(6, sched['downtime executor 3'])
        self.assertEqual(executor1_schedule, sched[1])
        self.assertEqual(executor2_schedule, sched[2])
        self.assertEqual(executor3_schedule, sched[3])

    def test_triple_equal_task_triple_executor(self):
        task_a = ['a', 1]
        task_b = ['b', 1]
        task_c = ['c', 1]
        sched = create_schedule([task_a, task_b, task_c], 3)
        executor1_schedule = '1. task: a from 0 to 1'
        executor2_schedule = '1. task: b from 0 to 1'
        executor3_schedule = '1. task: c from 0 to 1'
        self.assertEqual(3, sched['executors'])
        self.assertEqual(1, sched['duration'])
        self.assertEqual(0, sched['downtime'])
        self.assertEqual(0, sched['downtime executor 1'])
        self.assertEqual(0, sched['downtime executor 2'])
        self.assertEqual(0, sched['downtime executor 3'])
        self.assertEqual(executor1_schedule, sched[1])
        self.assertEqual(executor2_schedule, sched[2])
        self.assertEqual(executor3_schedule, sched[3])

    def test_triple_has_large_task_triple_executor(self):
        task_a = ['a', 1]
        task_b = ['b', 1]
        task_c = ['c', 10]
        sched = create_schedule([task_a, task_b, task_c], 3)
        executor1_schedule = '1. task: a from 0 to 1\n' \
                             '2. task: b from 1 to 2\n' \
                             '3. task: c from 2 to 10'
        executor2_schedule = '1. task: c from 0 to 2\n' \
                             '2. task: downtime from 2 to 10'
        executor3_schedule = '1. task: downtime from 0 to 10'
        self.assertEqual(10, sched['duration'])
        self.assertEqual(18, sched['downtime'])
        self.assertEqual(0, sched['downtime executor 1'])
        self.assertEqual(8, sched['downtime executor 2'])
        self.assertEqual(10, sched['downtime executor 3'])
        self.assertEqual(executor1_schedule, sched[1])
        self.assertEqual(executor2_schedule, sched[2])
        self.assertEqual(executor3_schedule, sched[3])

    def test_complex(self):
        tasks = [['a', 3], ['b', 4], ['c', 6], ['d', 7],
                ['e', 7], ['f', 9], ['g', 10], ['h', 12],
                ['i', 17]]
        sched = create_schedule(tasks, 5)
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
        self.assertEqual(tuple(tasks), sched['tasks'])
        self.assertEqual(9, sched['tasks amount'])
        self.assertEqual(5, sched['executors'])
        self.assertEqual(17, sched['duration'])
        self.assertEqual(10, sched['downtime'])
        self.assertEqual(0, sched['downtime executor 1'])
        self.assertEqual(0, sched['downtime executor 2'])
        self.assertEqual(0, sched['downtime executor 3'])
        self.assertEqual(0, sched['downtime executor 4'])
        self.assertEqual(10, sched['downtime executor 5'])
        self.assertEqual(executor1_schedule, sched[1])
        self.assertEqual(executor2_schedule, sched[2])
        self.assertEqual(executor3_schedule, sched[3])
        self.assertEqual(executor4_schedule, sched[4])
        self.assertEqual(executor5_schedule, sched[5])


if __name__ == '__main__':
    unittest.main()
