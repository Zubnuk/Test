import unittest
from custom_exception import ScheduleArgumentException
from task import Task
from main import schedule, schedule_duration


class TestMain(unittest.TestCase):
    def test_none_tasks(self):
        self.assertRaisesRegex(ScheduleArgumentException,
                               'Error during Schedule calculation! The tasks parameter is not a list',
                               schedule, None, 1)

    def test_empty_tasks(self):
        self.assertRaisesRegex(ScheduleArgumentException,
                               'Error during Schedule calculation! The task list is empty',
                               schedule, [], 1)

    def test_tasks_contains_non_task(self):
        tasks = [Task('a', 7), Task('b', 3), 'non task object']
        self.assertRaisesRegex(ScheduleArgumentException,
                               'Error during Schedule calculation! The task list contains not a Task object in the '
                               'position 2',
                               schedule, tasks, 1)

    def test_duration(self):
        tasks = [Task('A', 3), Task('B', 4), Task('C', 6), Task('D', 7),
                 Task('E', 7), Task('F', 9), Task('G', 10), Task('H', 12),
                 Task('I', 17)]
        workers_count = 5
        actual = schedule_duration(tasks, workers_count)
        expected = 17
        self.assertEqual(actual, expected)

    def test_complex(self):
        tasks = [Task('A', 3), Task('B', 4), Task('C', 6), Task('D', 7),
                 Task('E', 7), Task('F', 9), Task('G', 10), Task('H', 12),
                 Task('I', 17)]
        workers_count = 5
        actual = schedule(tasks, workers_count)
        expected = "Worker 1: {'A': 3, 'B': 4, 'C': 6, 'D': 4}\nWorker 2: {'D': 3, 'E': 7, 'F': 7}\nWorker 3: {'F': " \
                   "2, 'G': 10, 'H': 5}\nWorker 4: {'H': 7, 'I': 10}\nWorker 5: {'I': 7}\nSchedule duration: 17"
        self.assertEqual(actual, expected)
