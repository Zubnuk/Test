import networkx as nx


class ScheduleChecker:
    @staticmethod
    def is_inverted_trees(graph: nx.Graph) -> bool:
        """
        checks if the graph is an inverted tree by checking if
        acyclic
        out_degree = 0.
        :param graph:
        :return: returns a boolean value is an inverted tree or not
        """
        # Check if the graph is an inverted tree by checking if it's acyclic and has exactly one node with in-degree 0
        return nx.is_directed_acyclic_graph(graph) and sum(
            1 for node in graph.nodes if graph.out_degree(node) == 0) == 1

    @staticmethod
    def get_tree_count(graph: nx.Graph) -> int:
        """
        number_weakly_connected_components -> tree count
        :param graph:
        :return: Number of inverted trees in the graph.
        """

        # Return the number of inverted trees in the graph
        return nx.number_weakly_connected_components(graph)

    @staticmethod
    def get_schedule_errors(graph: nx.Graph, schedule: list[list[str]]) -> list[str]:
        """
        error handles:
        tasks that are not found in the graph
        tasks that are executed simultaneously
        :param graph:
        :param schedule:
        :return: errors as list
        """
        errors = []
        task_start_times = {}
        for time, tasks in enumerate(schedule):
            for task in tasks:
                if task not in graph:
                    errors.append(f"Task '{task}' in schedule not found in graph")
                if task in task_start_times:
                    errors.append(
                        f"Task '{task}' starts at time {time} but already started at time {task_start_times[task]}")
                else:
                    task_start_times[task] = time

        return errors


def __usage_example():
    # Create an example graph
    graph = nx.DiGraph()

    graph.add_edges_from([('A', 'B'), ('B', 'C'), ('D', 'L'), ('E', 'D'),
                          ('F', 'A'), ('G', 'A'), ('H', 'A'), ('I', 'L'),
                          ('J', 'E'), ('K', 'E'), ('L', 'C'), ('M', 'B')])

    schedule_checker = ScheduleChecker()
    print(schedule_checker.is_inverted_trees(graph))

    print(schedule_checker.get_tree_count(graph))

    # Get errors in the schedule
    schedule = [["K", "J", "H"], ["E", "G", "F"], ["I", "D", "M"], ["B"], ["C"]]

    print(schedule_checker.get_schedule_errors(graph, schedule))  # Output: []


if __name__ == '__main__':
    __usage_example()
