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

    def test_single(self):
        task_a = Task('a', 1)
        sched = Schedule([task_a], 1)
        executor1_schedule = '1. task: a from: 0 to 1'
        self.assertEqual(tuple([task_a]), sched.tasks)
        self.assertEqual(1, sched.task_count)
        self.assertEqual(1, sched.executor_count)
        self.assertEqual(1, sched.duration)
        self.assertEqual(0, sched.downtime)
        self.assertEqual(1, sched.stage2_downtime)
        self.assertEqual(3, sched.total_downtime)
        self.assertEqual(stage1_schedule, sched.stage1_schedule)
        self.assertEqual(stage2_schedule, sched.stage2_schedule)

    def test_double(self):
        task_a = Task('a', 2, 1)
        task_b = Task('b', 1, 2)
        sched = Schedule([task_a, task_b])
        stage1_schedule = '1. task: b from: 0 to 1\n' \
                          '2. task: a from: 1 to 3\n' \
                          '3. task: downtime from: 3 to 4'
        stage2_schedule = '1. task: downtime from: 0 to 1\n' \
                          '2. task: b from: 1 to 3\n' \
                          '3. task: a from: 3 to 4'
        self.assertEqual(tuple([task_b, task_a]), sched.tasks)
        self.assertEqual(tuple(['b', 'a']), sched.tasks_names)
        self.assertEqual(2, sched.task_count)
        self.assertEqual(4, sched.total_duration)
        self.assertEqual(1, sched.stage1_downtime)
        self.assertEqual(1, sched.stage2_downtime)
        self.assertEqual(2, sched.total_downtime)
        self.assertEqual(stage1_schedule, sched.stage1_schedule)
        self.assertEqual(stage2_schedule, sched.stage2_schedule)

    def test_triple_stage2_greater_only(self):
        task_a = Task('a', 1, 2)
        task_b = Task('b', 3, 4)
        task_c = Task('c', 5, 6)
        sched = Schedule([task_a, task_b, task_c])
        stage1_schedule = '1. task: a from: 0 to 1\n' \
                          '2. task: b from: 1 to 4\n' \
                          '3. task: c from: 4 to 9\n' \
                          '4. task: downtime from: 9 to 15'
        stage2_schedule = '1. task: downtime from: 0 to 1\n' \
                          '2. task: a from: 1 to 3\n' \
                          '3. task: downtime from: 3 to 4\n' \
                          '4. task: b from: 4 to 8\n' \
                          '5. task: downtime from: 8 to 9\n' \
                          '6. task: c from: 9 to 15'
        self.assertEqual(tuple([task_a, task_b, task_c]), sched.tasks)
        self.assertEqual(tuple(['a', 'b', 'c']), sched.tasks_names)
        self.assertEqual(3, sched.task_count)
        self.assertEqual(15, sched.total_duration)
        self.assertEqual(6, sched.stage1_downtime)
        self.assertEqual(3, sched.stage2_downtime)
        self.assertEqual(9, sched.total_downtime)
        self.assertEqual(stage1_schedule, sched.stage1_schedule)
        self.assertEqual(stage2_schedule, sched.stage2_schedule)

    def test_triple_stage2_less_only(self):
        task_a = Task('a', 2, 1)
        task_b = Task('b', 4, 3)
        task_c = Task('c', 6, 5)
        sched = Schedule([task_a, task_b, task_c])
        stage1_schedule = '1. task: c from: 0 to 6\n' \
                          '2. task: b from: 6 to 10\n' \
                          '3. task: a from: 10 to 12\n' \
                          '4. task: downtime from: 12 to 15'
        stage2_schedule = '1. task: downtime from: 0 to 6\n' \
                          '2. task: c from: 6 to 11\n' \
                          '3. task: b from: 11 to 14\n' \
                          '4. task: a from: 14 to 15'
        self.assertEqual(tuple([task_c, task_b, task_a]), sched.tasks)
        self.assertEqual(tuple(['c', 'b', 'a']), sched.tasks_names)
        self.assertEqual(3, sched.task_count)
        self.assertEqual(15, sched.total_duration)
        self.assertEqual(3, sched.stage1_downtime)
        self.assertEqual(6, sched.stage2_downtime)
        self.assertEqual(9, sched.total_downtime)
        self.assertEqual(stage1_schedule, sched.stage1_schedule)
        self.assertEqual(stage2_schedule, sched.stage2_schedule)

    def test_triple_mix(self):
        task_a = Task('a', 2, 1)
        task_b = Task('b', 3, 4)
        task_c = Task('c', 6, 5)
        sched = Schedule([task_a, task_b, task_c])
        stage1_schedule = '1. task: b from: 0 to 3\n' \
                          '2. task: c from: 3 to 9\n' \
                          '3. task: a from: 9 to 11\n' \
                          '4. task: downtime from: 11 to 15'
        stage2_schedule = '1. task: downtime from: 0 to 3\n' \
                          '2. task: b from: 3 to 7\n' \
                          '3. task: downtime from: 7 to 9\n' \
                          '4. task: c from: 9 to 14\n' \
                          '5. task: a from: 14 to 15'
        self.assertEqual(tuple([task_b, task_c, task_a]), sched.tasks)
        self.assertEqual(tuple(['b', 'c', 'a']), sched.tasks_names)
        self.assertEqual(3, sched.task_count)
        self.assertEqual(15, sched.total_duration)
        self.assertEqual(4, sched.stage1_downtime)
        self.assertEqual(5, sched.stage2_downtime)
        self.assertEqual(9, sched.total_downtime)
        self.assertEqual(stage1_schedule, sched.stage1_schedule)
        self.assertEqual(stage2_schedule, sched.stage2_schedule)

    def test_pentad(self):
        task_a = Task('a', 4, 3)
        task_b = Task('b', 5, 2)
        task_c = Task('c', 3, 5)
        task_d = Task('d', 2, 3)
        task_e = Task('e', 4, 4)
        sched = Schedule([task_a, task_b, task_c, task_d, task_e])
        ordered_tasks = tuple([task_d, task_c, task_e, task_a, task_b])
        stage1_schedule = '1. task: d from: 0 to 2\n' \
                          '2. task: c from: 2 to 5\n' \
                          '3. task: e from: 5 to 9\n' \
                          '4. task: a from: 9 to 13\n' \
                          '5. task: b from: 13 to 18\n' \
                          '6. task: downtime from: 18 to 20'
        stage2_schedule = '1. task: downtime from: 0 to 2\n' \
                          '2. task: d from: 2 to 5\n' \
                          '3. task: c from: 5 to 10\n' \
                          '4. task: e from: 10 to 14\n' \
                          '5. task: a from: 14 to 17\n' \
                          '6. task: downtime from: 17 to 18\n' \
                          '7. task: b from: 18 to 20'
        self.assertEqual(ordered_tasks, sched.tasks)
        self.assertEqual(tuple(['d', 'c', 'e', 'a', 'b']), sched.tasks_names)
        self.assertEqual(5, sched.task_count)
        self.assertEqual(20, sched.total_duration)
        self.assertEqual(2, sched.stage1_downtime)
        self.assertEqual(3, sched.stage2_downtime)
        self.assertEqual(5, sched.total_downtime)
        self.assertEqual(stage1_schedule, sched.stage1_schedule)
        self.assertEqual(stage2_schedule, sched.stage2_schedule)

    def test_sevenfold(self):
        task_a = Task('a', 7, 2)
        task_b = Task('b', 3, 4)
        task_c = Task('c', 2, 5)
        task_d = Task('d', 4, 1)
        task_e = Task('e', 6, 6)
        task_f = Task('f', 5, 3)
        task_g = Task('g', 4, 5)
        sched = Schedule([task_a, task_b, task_c, task_d, task_e, task_f,
                          task_g])
        ordered_tasks = tuple([task_c, task_b, task_g, task_e, task_f, task_a,
                               task_d])
        stage1_schedule = '1. task: c from: 0 to 2\n' \
                          '2. task: b from: 2 to 5\n' \
                          '3. task: g from: 5 to 9\n' \
                          '4. task: e from: 9 to 15\n' \
                          '5. task: f from: 15 to 20\n' \
                          '6. task: a from: 20 to 27\n' \
                          '7. task: d from: 27 to 31\n' \
                          '8. task: downtime from: 31 to 32'
        stage2_schedule = '1. task: downtime from: 0 to 2\n' \
                          '2. task: c from: 2 to 7\n' \
                          '3. task: b from: 7 to 11\n' \
                          '4. task: g from: 11 to 16\n' \
                          '5. task: e from: 16 to 22\n' \
                          '6. task: f from: 22 to 25\n' \
                          '7. task: downtime from: 25 to 27\n' \
                          '8. task: a from: 27 to 29\n' \
                          '9. task: downtime from: 29 to 31\n' \
                          '10. task: d from: 31 to 32'
        self.assertEqual(ordered_tasks, sched.tasks)
        self.assertEqual(tuple(['c', 'b', 'g', 'e', 'f', 'a', 'd']),
                         sched.tasks_names)
        self.assertEqual(7, sched.task_count)
        self.assertEqual(32, sched.total_duration)
        self.assertEqual(1, sched.stage1_downtime)
        self.assertEqual(6, sched.stage2_downtime)
        self.assertEqual(7, sched.total_downtime)
        self.assertEqual(stage1_schedule, sched.stage1_schedule)
        self.assertEqual(stage2_schedule, sched.stage2_schedule)


if __name__ == '__main__':
    unittest.main()
