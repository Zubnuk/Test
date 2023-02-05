import networkx as nx


class Schedule:
    def __init__(self, graph: nx.Graph, executor_count: int):
        self.__graph = graph
        self.__executor_count = executor_count
        self.__matrix = (nx.adjacency_matrix(graph)).toarray()
        self.__schedule = [[] for _ in range(executor_count)]
        self.__fill_schedule()
        self.get_schedule_for_executor(1)

    def get_schedule(self) -> list[list[str]]:
        return self.__schedule

    def get_schedule_for_executor(self, executor_idx: int) -> list[str]:
        return self.__schedule[executor_idx]

    def __fill_schedule(self) -> None:
        levels = [[]]
        matr = self.__matrix.tolist()
        for i in range(len(matr)):
            if sum(matr[i]) == 0:
                levels[0].append(i)
        k = 0
        levels.append([])
        while sum(len(row) for row in levels) != len(list(self.__graph.nodes)):
            for i in range(len(matr)):
                for j in range(len(levels[k])):
                    if matr[i][levels[k][j]] == 1:
                        levels[k + 1].append(i)
            k += 1
            levels.append([])
        del levels[-1]
        nodes = list(self.__graph.nodes)
        for row in levels:
            for i in range(len(row)):
                row[i] = nodes[row[i]]
        k = 0
        for i in range(len(levels) - 1, -1, -1):
            for j in range(len(levels[i]) - 1, -1, -1):
                if k == self.__executor_count:
                    k = 0
                    self.__schedule[k].append(levels[i][j])
                    k += 1
                else:
                    self.__schedule[k].append(levels[i][j])
                    k += 1


def __usage_example():
    graph = nx.DiGraph()
    graph.add_nodes_from([('a', {'color': 'red'}), ('b', {'color': 'red'}),
                          ('c', {'color': 'red'}), ('d', {'color': 'red'}),
                          ('e', {'color': 'green'}), ('f', {'color': 'green'}),
                          ('g', {'color': 'green'}), ('h', {'color': 'green'}),
                          ('i', {'color': 'green'}), ('j', {'color': 'green'}),
                          ('k', {'color': 'green'}), ('l', {'color': 'green'}),
                          ('m', {'color': 'green'})])
    graph.add_edges_from([('a', 'b'), ('b', 'c'), ('d', 'l'),
                          ('e', 'd'), ('f', 'a'), ('g', 'a'), ('h', 'a'), ('i', 'l'),
                          ('j', 'e'), ('k', 'e'), ('l', 'c'), ('m', 'b')])
    executor_count = 3
    schedule = Schedule(graph, executor_count)
    print(f'Schedule for {executor_count} executers:')
    for ex_idx in range(executor_count):
        print(f'#{ex_idx + 1} executer:')
        print(*schedule.get_schedule_for_executor(ex_idx))


if __name__ == '__main__':
    __usage_example()
