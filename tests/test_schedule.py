import unittest
import networkx as nx



from schedule import Schedule


class TestSchedule(unittest.TestCase):
    def test_none_graph(self):
        self.assertRaisesRegex(ValueError,
                                   'Error during initialization of the Schedule object! The graph parameter is not a graph',
                                   Schedule, None, 1)




    def test_schedule_for_executor_less_than_one(self):
        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D')])
        self.assertRaisesRegex(ValueError, 'Invalid executors amount number',
                                   Schedule, graph, 0)

    def test_one_executor(self):
        graph = nx.DiGraph()
        graph.add_nodes_from(
            [('A', {'color': 'red'}), ('B', {'color': 'red'}), ('C', {'color': 'red'})])
        graph.add_edges_from([('A', 'B'), ('B', 'C')])
        schedule = Schedule(graph, 1)
        right_schedule = [['A', 'B', 'C']]
        self.assertEqual(right_schedule, schedule.get_schedule())

    def test_two_executors(self):
        graph = nx.DiGraph()
        graph.add_nodes_from([('A', {'color': 'red'}), ('B', {'color': 'red'}), ('C', {'color': 'red'})])
        graph.add_edges_from([('A', 'B'), ('C', 'B')])
        schedule = Schedule(graph, 2)
        right_schedule = [['A', 'B'], ['C', '-']]
        self.assertEqual(right_schedule, schedule.get_schedule())

    def test_one_line_two_executors(self):
        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B')])
        schedule = Schedule(graph, 2)
        right_schedule = [['A', 'B'], ['-', '-']]
        self.assertEqual(right_schedule, schedule.get_schedule())

    def test_schedule_for_executor1(self):
        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B'), ('B', 'C')])
        schedule = Schedule(graph, 1)
        right_schedule = ['A', 'B', 'C']
        self.assertEqual(right_schedule, schedule.get_schedule_for_executor(0))

    def test_schedule_for_executor2(self):
        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B'), ('C', 'B')])
        schedule = Schedule(graph, 2)
        right_schedule = ['A', 'B']
        self.assertEqual(right_schedule, schedule.get_schedule_for_executor(0))

    def test_schedule_for_executor3(self):
        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B'), ('C', 'B')])
        schedule = Schedule(graph, 2)
        right_schedule = ['C', '-']
        self.assertEqual(right_schedule, schedule.get_schedule_for_executor(1))

    def test_complex(self):
        graph = nx.DiGraph()
        graph.add_edges_from([('A', 'B'), ('B', 'C'), ('D', 'L'), ('E', 'D'),
                                  ('F', 'A'), ('G', 'A'), ('H', 'A'), ('I', 'L'),
                                  ('J', 'E'), ('K', 'E'), ('L', 'C'), ('M', 'B')])
        schedule = Schedule(graph, 3)
        right_schedule = [['J', 'G', 'A', 'I', 'L', 'C'], ['K', 'H', 'M', 'B', '-', '-'], ['F', 'E', 'D', '-', '-', '-']]
        executor1_schedule = ['J', 'G', 'A', 'I', 'L', 'C']
        executor2_schedule = ['K', 'H', 'M', 'B', '-', '-']
        executor3_schedule = ['F', 'E', 'D', '-', '-', '-']
        self.assertEqual(right_schedule, schedule.get_schedule())
        self.assertEqual(executor1_schedule, schedule.get_schedule_for_executor(0))
        self.assertEqual(executor2_schedule, schedule.get_schedule_for_executor(1))
        self.assertEqual(executor3_schedule, schedule.get_schedule_for_executor(2))


if __name__ == '__main__':
    unittest.main()
