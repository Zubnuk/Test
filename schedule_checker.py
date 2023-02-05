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
    def get_schedule_errors(schedule: list[list[str]]) -> list[str]:
        errors = []
        task_start_times = {}
        for node, edges in graph.items(): 
            for edge in edges:  
                if node not in task_start_times or edge not in task_start_times: 

                    errors.append(f"Task '{node}' or '{edge}' not found in schedule")  

                elif task_start_times[node] >= task_start_times[edge]:  

                    errors.append(
                        f"Violation of dependency: Task '{node}' should start before '{edge}'")

        return errors

def __usage_example():
    graph = nx.DiGraph()

if __name__ == '__main__':
    __usage_example()
