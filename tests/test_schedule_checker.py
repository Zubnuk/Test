import unittest

from schedule_checker import ScheduleChecker


class TestScheduleChecker(unittest.TestCase):
    
     def test_is_inverted_trees(self):
        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D')])
        checker = ScheduleChecker()
        self.assertTrue(checker.is_inverted_trees(graph))

        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')])
        checker = ScheduleChecker()
        self.assertFalse(checker.is_inverted_trees(graph))

    def test_get_tree_count(self):
        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D')])
        checker = ScheduleChecker()
        self.assertEqual(checker.get_tree_count(graph), 1)

        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('E', 'F')])
        checker = ScheduleChecker()
        self.assertEqual(checker.get_tree_count(graph), 2)

    def test_get_schedule_errors(self):
        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D')])
        checker = ScheduleChecker()

        schedule = [["B"], ["A"], ["C"], ["D"]]
        self.assertEqual(checker.get_schedule_errors(graph, schedule), [])

        schedule = [["C"], ["B"], ["D"], ["A"]]
        self.assertEqual(checker.get_schedule_errors(graph, schedule), [])

        schedule = [["B"], ["C"], ["B"], ["D"]]
        self.assertEqual(checker.get_schedule_errors(graph, schedule),
                         ["Task 'B' starts at time 2 but already started at time 0"])

    def test_empty_schedule(self):
        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D')])
        schedule_checker = ScheduleChecker()
        self.assertEqual(schedule_checker.get_schedule_errors(graph, []), [])

    def test_schedule_with_task_not_in_graph(self):
        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D')])
        schedule_checker = ScheduleChecker()
        schedule = [["A"], ["E"], ["B"], ["C"], ["D"]]
        self.assertEqual(schedule_checker.get_schedule_errors(graph, schedule),
                         ["Task 'E' in schedule not found in graph"])

    def test_schedule_with_multiple_same_tasks_at_same_time(self):
        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D')])
        schedule_checker = ScheduleChecker()
        schedule = [["A"], ["B"], ["B"], ["C"], ["D"]]
        self.assertEqual(schedule_checker.get_schedule_errors(graph, schedule),
                         ["Task 'B' starts at time 2 but already started at time 1"])
        
    def test_get_tree_count_empty(self):
        graph = nx.DiGraph()
        checker = ScheduleChecker()
        self.assertEqual(checker.get_tree_count(graph), 0)
        
    def test_valid_schedule(self):
        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D')])
        schedule_checker = ScheduleChecker()
        schedule = [["A"], ["B"], ["C"], ["D"]]
        self.assertEqual(schedule_checker.get_schedule_errors(graph, schedule), [])
        
     def test_is_inverted_trees_empty(self):
        graph = nx.DiGraph()
        checker = ScheduleChecker()
        self.assertFalse(checker.is_inverted_trees(graph))

    def test_schedule_errors(self):
        graph = nx.DiGraph()
        checker = ScheduleChecker()
        schedule = []
        self.assertEqual(checker.get_schedule_errors(graph, schedule), [])

    def test_some_case(self):
        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B'), ('B', 'C'), ('D', 'L'), ('E', 'D'),
                              ('F', 'A'), ('G', 'A'), ('H', 'A'), ('I', 'L'),
                              ('J', 'E'), ('K', 'E'), ('L', 'C'), ('M', 'B')])

        schedule = [["K", "J", "H"], ["E", "G", "F"], ["I", "D", "M"], ["B"], ["C"]]

        schedule_checker = ScheduleChecker()
        self.assertTrue(schedule_checker.is_inverted_trees(graph))
        self.assertEqual(schedule_checker.get_tree_count(graph), 1)
        self.assertEqual(schedule_checker.get_schedule_errors(graph, schedule), [])


if __name__ == '__main__':
    unittest.main()
