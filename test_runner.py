import unittest


from tests.test_task import TestTask
from tests.test_schedule_task import TestScheduleTask


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestTask))
suite.addTest(unittest.makeSuite(TestScheduleTask))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
