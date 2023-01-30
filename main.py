import networkx as nx
import matplotlib.pyplot as plt
import scipy

from schedule_graph import ScheduleGraph
from schedule_checker import ScheduleChecker
from schedule import Schedule


def main():
    # networkx example
    graph = nx.DiGraph()
    graph.add_nodes_from([('a', {'color': 'red'}), ('b', {'color': 'red'}),
                          ('c', {'color': 'red'}), ('d', {'color': 'red'}),
                          ('e', {'color': 'green'}), ('f', {'color': 'green'}),
                          ('g', {'color': 'green'})])
    graph.add_edges_from([('d', 'c'), ('c', 'a'), ('b', 'a'),
                          ('g', 'f'), ('f', 'e')])
    print(graph)
    print('\nVertices of the graph:\n', graph.nodes)

    matrix = nx.adjacency_matrix(graph)
    print('\nAn adjacency matrix of the graph:\n', matrix.toarray())
    print(type(matrix.toarray()))

    color_map = [graph.nodes[name]['color'] for name in graph.nodes]
    nx.draw_planar(graph, with_labels=True, node_color=color_map)
    plt.show()

    # ScheduleGraph usage
    tree_count = 3
    vertex_count = 15
    schedule_graph = ScheduleGraph.generate_random_forest(tree_count,
                                                          vertex_count)
    ScheduleGraph.show_plot(schedule_graph)

    # ScheduleChecker usage
    if not ScheduleChecker.is_inverted_trees(graph):
        print('Error! The graph is not a forest with inverted trees!')
        return
    print('The graph is a forest with '
          f'{ScheduleChecker.get_tree_count(graph)} inverted trees!')

    # Schedule usage
    executor_count = 2
    schedule = Schedule(graph, executor_count)
    print(f'Schedule for {executor_count} execotors:')
    for ex_idx in range(executor_count):
        print(f'#{ex_idx + 1} executer:\n'
              f'{schedule.get_schedule_for_executor(ex_idx)}')

    # ScheduleChecker usage
    print('\nSchedule is checked')
    errors = ScheduleChecker.get_schedule_errors(schedule.get_schedule())
    if len(errors) > 0:
        print('Schedule has errors:\n', '\n'.join(errors))
    else:
        print('Schedule has no errors')


if __name__ == '__main__':
    main()
