import networkx as nx


class ScheduleChecker:
    @staticmethod
    def is_inverted_trees(graph: nx.Graph) -> bool:
        if not nx.is_tree(graph):
            return False
        for node in graph.nodes():
            if graph.degree[node] == 1:
                continue
            neighbors = list(graph.neighbors(node))
            for neighbor in neighbors:
                if graph.degree[neighbor] != 1:
                    return False
        return True

    @staticmethod
    def get_tree_count(graph: nx.Graph) -> int:
        return nx.number_weakly_connected_components(graph)

    @staticmethod
    def get_schedule_errors(graph: nx.Graph,schedule: list[list[str]]) -> list[str]:
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
    graph = nx.DiGraph()

if __name__ == '__main__':
    __usage_example()
