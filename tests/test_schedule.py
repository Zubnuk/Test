import unittest
import networkx as nx
from schedule import Schedule


class TestSchedule(unittest.TestCase):
    def test_none_executor_count(self):
        self.assertRaisesRegex(ValueError,
                               'Executor count must not be None!',
                               Schedule, nx.DiGraph, None)

    def test_none_graph(self):
        self.assertRaisesRegex(ValueError,
                               'Graph must not be None!',
                               Schedule, None, 1)

    def test_less_one_executor_count(self):
        self.assertRaisesRegex(ValueError,
                               'Executor count must be more than 0!',
                               Schedule, nx.DiGraph, 0)

    def test_empty_graph(self):
        self.assertRaisesRegex(ValueError,
                               'Graph is empty!',
                               Schedule, nx.DiGraph(), 1)

    def test_di_graph(self):
        self.assertRaisesRegex(ValueError,
                               'Graph must be type of DiGraph!',
                               Schedule, nx.Graph, 1)

    def test_di_graph_first(self):
        graph = nx.DiGraph()
        graph.add_nodes_from([('a', {'color': 'red', 'weight': 1})])
        s = Schedule(graph, 3)
        test = [['a'], ['-'], ['-']]
        self.assertEqual(s.get_schedule(), test)

    def test_di_graph_second(self):
        graph = nx.DiGraph()
        graph.add_nodes_from([('a', {'color': 'red', 'weight': 1})])
        s = Schedule(graph, 3)
        test = ['a']
        self.assertEqual(s.get_schedule_for_executor(1), test)

    def test_di_graph_third(self):
        graph = nx.DiGraph()
        graph.add_nodes_from([('a', {'color': 'red', 'weight': 1}), ('b', {'color': 'red', 'weight': 2}),
                              ('c', {'color': 'red', 'weight': 3})])
        s = Schedule(graph, 3)
        test = [['c'], ['b'], ['a']]
        self.assertEqual(s.get_schedule(), test)

    def test_di_graph_fourth(self):
        graph = nx.DiGraph()
        graph.add_nodes_from([('a', {'color': 'red', 'weight': 5}), ('b', {'color': 'red', 'weight': 2}),
                              ('c', {'color': 'red', 'weight': 1}), ('d', {'color': 'red', 'weight': 6}),
                              ('e', {'color': 'red', 'weight': 11}), ('f', {'color': 'red', 'weight': 8}),
                              ('g', {'color': 'red', 'weight': 9}), ('h', {'color': 'red', 'weight': 10}),
                              ('i', {'color': 'red', 'weight': 7}), ('j', {'color': 'red', 'weight': 12}),
                              ('k', {'color': 'red', 'weight': 13}), ('l', {'color': 'red', 'weight': 3}),
                              ('m', {'color': 'red', 'weight': 4})])
        graph.add_edges_from([('j', 'e'), ('k', 'e'), ('e', 'd'),
                              ('h', 'a'), ('g', 'a'), ('f', 'a'),
                              ('i', 'l'), ('d', 'l'), ('a', 'b'),
                              ('m', 'b'), ('l', 'c'), ('b', 'c')])
        s = Schedule(graph, 3)
        test = [['k', 'e', 'i', 'm', 'b', 'c'], ['j', 'g', 'd', 'l', '-', '-'], ['h', 'f', 'a', '-', '-', '-']]
        self.assertEqual(s.get_schedule(), test)


if __name__ == '__main__':
    unittest.main()
