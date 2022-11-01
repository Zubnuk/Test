import unittest


from tests.test_task import TestTask


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestTask))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
