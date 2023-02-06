import networkx as nx


class ScheduleChecker:
    @staticmethod
    def is_inverted_trees(graph: nx.Graph) -> bool:
        if graph is None or len(graph.nodes) < 1:
            return False
        matrix = nx.adjacency_matrix(graph)
        matrix = matrix.toarray()
        zero_line_count = 0
        for i in range(len(matrix)):
            line_sum = sum(matrix[i])
            if line_sum > 1:
                return False
            elif line_sum == 0:
                zero_line_count += 1
        if zero_line_count > 0:
            return True
        return False

    @staticmethod
    def get_tree_count(graph: nx.Graph) -> int:
        if graph is None or len(graph.nodes) < 1:
            return 0
        matrix = nx.adjacency_matrix(graph)
        matrix = matrix.toarray()
        zero_line_count = 0
        for i in range(len(matrix)):
            if sum(matrix[i]) == 0:
                zero_line_count += 1
        if zero_line_count == 0:
            return 1
        return zero_line_count

    @staticmethod
    def get_schedule_errors(graph: nx.Graph, schedule: list[list[str]]) -> list[str]:
        errors = []
        all_tasks_in_schedule = []

        for line in schedule:
            for task in line:
                all_tasks_in_schedule.append(task)
                if not list(graph.nodes).count(task) > 0:
                    errors.append(f'There are no node named {task}')

        for node in list(graph.nodes):
            if not all_tasks_in_schedule.count(node) > 0:
                errors.append(f'There are no task named {node}')

        return errors


def __usage_example():
    graph = nx.DiGraph()
    graph.add_nodes_from(['a', 'b'])
    graph.add_edges_from([('a', 'b')])

    if ScheduleChecker.is_inverted_trees(graph):
        print('The graph is an inverted trees!')
    else:
        print('The graph is NOT an inverted trees!')

    print(f'There are {ScheduleChecker.get_tree_count(graph)} trees in this graph!')
    schedule = [["a"]]
    errors = ScheduleChecker.get_schedule_errors(schedule)
    if len(errors) > 0:
        print('Schedule has errors:\n', '\n'.join(errors))
    else:
        print('Schedule has no errors')


if __name__ == '__main__':
    __usage_example()