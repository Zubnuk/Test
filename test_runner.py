import unittest


from tests.test_task import TestTask
from tests.test_schedule_row import TestScheduleRow
from tests.test_schedule import TestSchedule


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestTask))
suite.addTest(unittest.makeSuite(TestScheduleRow))
suite.addTest(unittest.makeSuite(TestSchedule))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
