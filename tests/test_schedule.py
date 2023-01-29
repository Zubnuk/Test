import unittest


from main import Schedule, ScheduleRow
from task import Task


class TestSchedule(unittest.TestCase):

    def test_single(self):
        task_a = Task('a', 1, 2)
        sched = Schedule([task_a])
        stage1_schedule = (ScheduleRow(0, 1, 'a'),
                           ScheduleRow(1, 2, is_downtime=True))
        stage2_schedule = (ScheduleRow(0, 1, is_downtime=True),
                           ScheduleRow(1, 2, 'a'))
        self.assertEqual(tuple([task_a]), sched.tasks)
        self.assertEqual(1, sched.task_count)
        self.assertEqual(3, sched.duration)
        self.assertEqual(stage1_schedule, sched.stage1_schedule)
        self.assertEqual(stage2_schedule, sched.stage2_schedule)

    def test_double(self):
        task_a = Task('a', 2, 1)
        task_b = Task('b', 1, 2)
        sched = Schedule([task_a, task_b])
        stage1_schedule = (ScheduleRow(0, 1, 'b'),
                           ScheduleRow(1, 2, 'a'),
                           ScheduleRow(3, 1, is_downtime=True))
        stage2_schedule = (ScheduleRow(0, 1, is_downtime=True),
                           ScheduleRow(1, 2, 'b'),
                           ScheduleRow(3, 1, 'a'))
        self.assertEqual(tuple([task_b, task_a]), sched.tasks)
        self.assertEqual(2, sched.task_count)
        self.assertEqual(4, sched.duration)
        self.assertEqual(stage1_schedule, sched.stage1_schedule)
        self.assertEqual(stage2_schedule, sched.stage2_schedule)

    def test_triple_stage2_greater_only(self):
        task_a = Task('a', 1, 2)
        task_b = Task('b', 3, 4)
        task_c = Task('c', 5, 6)
        sched = Schedule([task_a, task_b, task_c])
        stage1_schedule = (ScheduleRow(0, 1, 'a'),
                           ScheduleRow(1, 3, 'b'),
                           ScheduleRow(4, 5, 'c'),
                           ScheduleRow(9, 6, is_downtime=True))
        stage2_schedule = (ScheduleRow(0, 1, is_downtime=True),
                           ScheduleRow(1, 2, 'a'),
                           ScheduleRow(3, 1, is_downtime=True),
                           ScheduleRow(4, 4, 'b'),
                           ScheduleRow(8, 1, is_downtime=True),
                           ScheduleRow(9, 6, 'c'))
        self.assertEqual(tuple([task_a, task_b, task_c]), sched.tasks)
        self.assertEqual(3, sched.task_count)
        self.assertEqual(15, sched.duration)
        self.assertEqual(stage1_schedule, sched.stage1_schedule)
        self.assertEqual(stage2_schedule, sched.stage2_schedule)

    def test_triple_stage2_less_only(self):
        task_a = Task('a', 2, 1)
        task_b = Task('b', 4, 3)
        task_c = Task('c', 6, 5)
        sched = Schedule([task_a, task_b, task_c])
        stage1_schedule = (ScheduleRow(0, 6, 'c'),
                           ScheduleRow(6, 4, 'b'),
                           ScheduleRow(10, 2, 'a'),
                           ScheduleRow(12, 3, is_downtime=True))
        stage2_schedule = (ScheduleRow(0, 6, is_downtime=True),
                           ScheduleRow(6, 5, 'c'),
                           ScheduleRow(11, 3, 'b'),
                           ScheduleRow(14, 1, 'a'))
        self.assertEqual(tuple([task_c, task_b, task_a]), sched.tasks)
        self.assertEqual(3, sched.task_count)
        self.assertEqual(15, sched.duration)
        self.assertEqual(stage1_schedule, sched.stage1_schedule)
        self.assertEqual(stage2_schedule, sched.stage2_schedule)

    def test_triple_mix(self):
        task_a = Task('a', 2, 1)
        task_b = Task('b', 3, 4)
        task_c = Task('c', 6, 5)
        sched = Schedule([task_a, task_b, task_c])
        stage1_schedule = (ScheduleRow(0, 3, 'b'),
                           ScheduleRow(3, 6, 'c'),
                           ScheduleRow(9, 2, 'a'),
                           ScheduleRow(11, 4, is_downtime=True))
        stage2_schedule = (ScheduleRow(0, 3, is_downtime=True),
                           ScheduleRow(3, 4, 'b'),
                           ScheduleRow(7, 2, is_downtime=True),
                           ScheduleRow(9, 5, 'c'),
                           ScheduleRow(14, 1, 'a'))
        self.assertEqual(tuple([task_b, task_c, task_a]), sched.tasks)
        self.assertEqual(3, sched.task_count)
        self.assertEqual(15, sched.duration)
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
        stage1_schedule = (ScheduleRow(0, 2, 'd'),
                           ScheduleRow(2, 3, 'c'),
                           ScheduleRow(5, 4, 'e'),
                           ScheduleRow(9, 4, 'a'),
                           ScheduleRow(13, 5, 'b'),
                           ScheduleRow(18, 2, is_downtime=True))
        stage2_schedule = (ScheduleRow(0, 2, is_downtime=True),
                           ScheduleRow(2, 3, 'd'),
                           ScheduleRow(5, 5, 'c'),
                           ScheduleRow(10, 4, 'e'),
                           ScheduleRow(14, 3, 'a'),
                           ScheduleRow(17, 1, is_downtime=True),
                           ScheduleRow(18, 2, 'b'))
        self.assertEqual(ordered_tasks, sched.tasks)
        self.assertEqual(5, sched.task_count)
        self.assertEqual(20, sched.duration)
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
        stage1_schedule = (ScheduleRow(0, 2, 'c'),
                           ScheduleRow(2, 3, 'b'),
                           ScheduleRow(5, 4, 'g'),
                           ScheduleRow(9, 6, 'e'),
                           ScheduleRow(15, 5, 'f'),
                           ScheduleRow(20, 7, 'a'),
                           ScheduleRow(27, 4, 'd'),
                           ScheduleRow(31, 1, is_downtime=True))
        stage2_schedule = (ScheduleRow(0, 2, is_downtime=True),
                           ScheduleRow(2, 5, 'c'),
                           ScheduleRow(7, 4, 'b'),
                           ScheduleRow(11, 5, 'g'),
                           ScheduleRow(16, 6, 'e'),
                           ScheduleRow(22, 3, 'f'),
                           ScheduleRow(25, 2, is_downtime=True),
                           ScheduleRow(27, 2, 'a'),
                           ScheduleRow(29, 2, is_downtime=True),
                           ScheduleRow(31, 1, 'd'))
        self.assertEqual(ordered_tasks, sched.tasks)
        self.assertEqual(7, sched.task_count)
        self.assertEqual(32, sched.duration)
        self.assertEqual(stage1_schedule, sched.stage1_schedule)
        self.assertEqual(stage2_schedule, sched.stage2_schedule)


if __name__ == '__main__':
    unittest.main()
