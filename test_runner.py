import unittest

from tests.test_schedule import TestSchedule

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestSchedule))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
