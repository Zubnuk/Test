import unittest
import networkx as nx

from schedule_checker import ScheduleChecker


class TestScheduleChecker(unittest.TestCase):
    def test_empty_graph(self):
        graph = nx.DiGraph()
        self.assertFalse(ScheduleChecker.is_inverted_trees(graph))
        self.assertEqual(ScheduleChecker.get_tree_count(graph), 0)

    def test_none_graph(self):
        graph = None
        self.assertFalse(ScheduleChecker.is_inverted_trees(graph))
        self.assertEqual(ScheduleChecker.get_tree_count(graph), 0)

    def test_one_node(self):
        graph = nx.DiGraph()
        graph.add_nodes_from(['a'])
        self.assertTrue(ScheduleChecker.is_inverted_trees(graph))
        self.assertEqual(ScheduleChecker.get_tree_count(graph), 1)

    def test_two_nodes_without_edge(self):
        graph = nx.DiGraph()
        graph.add_nodes_from(['a', 'b'])
        self.assertTrue(ScheduleChecker.is_inverted_trees(graph))
        self.assertEqual(ScheduleChecker.get_tree_count(graph), 2)

    def test_two_nodes_with_edge(self):
        graph = nx.DiGraph()
        graph.add_nodes_from(['a', 'b'])
        graph.add_edges_from([('a', 'b')])
        self.assertTrue(ScheduleChecker.is_inverted_trees(graph))
        self.assertEqual(ScheduleChecker.get_tree_count(graph), 1)

    def test_two_nodes_looped(self):
        graph = nx.DiGraph()
        graph.add_nodes_from(['a', 'b'])
        graph.add_edges_from([('a', 'b'), ('b', 'a')])
        self.assertFalse(ScheduleChecker.is_inverted_trees(graph))
        self.assertEqual(ScheduleChecker.get_tree_count(graph), 1)

    def test_many_nodes_and_edges(self):
        graph = nx.DiGraph()
        graph.add_nodes_from([('a', {'color': 'red'}), ('b', {'color': 'red'}),
                              ('c', {'color': 'red'}), ('d', {'color': 'red'}),
                              ('e', {'color': 'green'}), ('f', {'color': 'green'}),
                              ('g', {'color': 'green'})])
        graph.add_edges_from([('d', 'c'), ('c', 'a'), ('b', 'a'),
                              ('g', 'f'), ('f', 'e')])
        self.assertTrue(ScheduleChecker.is_inverted_trees(graph))
        self.assertEqual(ScheduleChecker.get_tree_count(graph), 2)

    def test_many_nodes_with_loop(self):
        graph = nx.DiGraph()
        graph.add_nodes_from([('a', {'color': 'red'}), ('b', {'color': 'red'}),
                              ('c', {'color': 'red'}), ('d', {'color': 'red'}),
                              ('e', {'color': 'green'}), ('f', {'color': 'green'}),
                              ('g', {'color': 'green'})])
        graph.add_edges_from([('d', 'c'), ('c', 'a'), ('b', 'a'),
                              ('g', 'f'), ('f', 'e'), ('d', 'b')])
        self.assertFalse(ScheduleChecker.is_inverted_trees(graph))
        self.assertEqual(ScheduleChecker.get_tree_count(graph), 2)

    def test_two_nodes_with_one_error(self):
        graph = nx.DiGraph()
        graph.add_nodes_from(['a', 'b'])
        graph.add_edges_from([('a', 'b')])
        schedule = [["a"]]
        self.assertEqual(ScheduleChecker.get_schedule_errors(graph, schedule), ['There are no task named b'])

    def test_many_nodes_many_errors(self):
        graph = nx.DiGraph()
        graph.add_nodes_from([('a', {'color': 'red'}), ('b', {'color': 'red'}),
                              ('c', {'color': 'red'}), ('d', {'color': 'red'}),
                              ('e', {'color': 'green'}), ('f', {'color': 'green'}),
                              ('g', {'color': 'green'})])
        graph.add_edges_from([('d', 'c'), ('c', 'a'), ('b', 'a'),
                              ('g', 'f'), ('f', 'e')])
        schedule = [['k', 'd'], ['c', 'b'], ['g', 'a'], ['f']]
        self.assertEqual(ScheduleChecker.get_schedule_errors(graph, schedule), ['There are no node named k',
                                                                                'There are no task named e'])

    def test_two_nodes_no_errors(self):
        graph = nx.DiGraph()
        graph.add_nodes_from(['a', 'b'])
        graph.add_edges_from([('a', 'b')])
        schedule = [["a"], ['b']]
        self.assertEqual(ScheduleChecker.get_schedule_errors(graph, schedule), [])


if __name__ == '__main__':
    unittest.main()
