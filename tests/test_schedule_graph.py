import unittest


from schedule_graph import ScheduleGraph
from custom_exception import ArgumentException


class TestScheduleGraph(unittest.TestCase):
    def test_one_vertex(self):
        g = ScheduleGraph.generate_random_forest(1, 1)
        self.assertEqual(1, len(g.nodes()))

    def test_several_vertex(self):
        g = ScheduleGraph.generate_random_forest(1, 3)
        self.assertEqual(3, len(g.nodes()))

    def test_several_trees(self):
        g = ScheduleGraph.generate_random_forest(3, 10)
        self.assertEqual(10, len(g.nodes()))

    def test_zero_vertex_count(self):
        self.assertRaisesRegex(ArgumentException, 'Tree count and vertex count must be an integer more than zero',
                               ScheduleGraph.generate_random_forest, 1, 0)

    def test_zero_tree_count(self):
        self.assertRaisesRegex(ArgumentException, 'Tree count and vertex count must be an integer more than zero',
                               ScheduleGraph.generate_random_forest, 0, 2)

    def test_tree_count_more_than_vertex_count(self):
        self.assertRaisesRegex(ArgumentException, 'Tree count must be not more than vertex count',
                               ScheduleGraph.generate_random_forest, 3, 2)

    def test_type_tree_count_not_int(self):
        self.assertRaisesRegex(ArgumentException, 'Tree count and vertex count must be an integer more than zero',
                               ScheduleGraph.generate_random_forest, 1.1, 2)

    def test_type_vertex_count_not_int(self):
        self.assertRaisesRegex(ArgumentException, 'Tree count and vertex count must be an integer more than zero',
                               ScheduleGraph.generate_random_forest, 1, 2.2)


if __name__ == '__main__':
    unittest.main()