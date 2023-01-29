import networkx as nx


class Schedule:
    def __init__(self, graph: nx.Graph, executor_count: int):
        self.__graph = graph
        self.__executor_count = executor_count
        self.__matrix = (nx.adjacency_matrix(graph)).toarray()
        self.__schedule = [[] for _ in range(executor_count)]
        self.__fill_schedule()

    def get_schedule(self) -> list[list[str]]:
        pass

    def get_schedule_for_executor(self, executor_idx: int) -> list[str]:
        pass

    def __fill_schedule(self) -> None:
        pass
