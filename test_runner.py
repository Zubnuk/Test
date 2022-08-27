import unittest
from test_dijkstra import TestDijkstra
from test_floyd_warshall import TestFloydWarshall
from test_table_path import TestTablePath


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestDijkstra))
suite.addTest(unittest.makeSuite(TestFloydWarshall))
suite.addTest(unittest.makeSuite(TestTablePath))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
