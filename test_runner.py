import unittest


from tests.test_task import TestTask
from tests.test_main import TestMain


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestTask))
suite.addTest(unittest.makeSuite(TestMain))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
