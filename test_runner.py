import unittest


from tests.test_schedule import TestSchedule
from tests.test_schedule_graph import TestScheduleGraph
from tests.test_schedule_checker import TestScheduleChecker


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestSchedule))
suite.addTest(unittest.makeSuite(TestScheduleGraph))
suite.addTest(unittest.makeSuite(TestScheduleChecker))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
