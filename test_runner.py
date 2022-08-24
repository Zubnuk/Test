import unittest
from test_dijkstra import TestDijkstra
from test_floyd_warshall import TestFloydWarshall


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestDijkstra))
suite.addTest(unittest.makeSuite(TestFloydWarshall))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
