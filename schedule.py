import networkx as nx


class Schedule:
    def __init__(self, graph: nx.Graph, executor_count: int):
        self.__graph = graph
        self.__executor_count = executor_count
        self.__matrix = (nx.adjacency_matrix(graph)).toarray()
        self.__schedule = [[] for _ in range(executor_count)]
        self.__fill_schedule()

    def get_schedule(self) -> list[list[str]]:
        return self.__schedule

    def get_schedule_for_executor(self, executor_idx: int) -> list[str]:
        return self.__schedule[executor_idx]

    def __error(self):

        if self.__graph is None:
            raise ValueError("Graph None")
        if self.__executor_count is None:
            raise ValueError("executor_count None")
        if self.__executor_count < 1:
            raise ValueError("executor_count must be >0")
        if type(self.__graph) is not nx.DiGraph:
            raise ValueError("Graph not DiGraph")
        if len(self.__graph.nodes) < 1:
            raise ValueError("Empty graph")

    def __input_matrix(self, arr, indexs):
        mon = [[]]
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if indexs[j] == i:
                    mon[i].append(1)
                else:
                    mon[i].append(0)
            mon.append([])
        mon.pop(-1)
        return mon

    def __Prioritization(self, levels, arr):
        while levels[-1]:
            temp = levels[-1]
            levels.append([])
            for i in temp:
                for j in range(len(arr[i])):
                    if arr[i][j] == 1:
                        levels[-1].append(j)

        levels.pop(-1)
        levels.reverse()
        level = []
        for i in levels:
            level += i
        return level

    def __Schedule_Distribution(self, level, arr):
        while len(level) != 0:
            count = 0
            index_row = []
            maxCount = len(level)
            for i in level:
                maxCount -= 1
                if self.__CheckElement(i, arr):
                    count += 1
                    self.__schedule[count - 1].append(list(self.__graph.nodes)[i])
                    index_row.append(i)
                    maxCount -= 1
                if count == self.__executor_count or len(level) == 0 or maxCount == 0:
                    break
            for i in range(count):
                arr[index_row[i]] = [0 for i in range(len(arr[0]))]
                level.remove(index_row[i])
            if count != self.__executor_count:
                for i in range(count, self.__executor_count):
                    self.__schedule[i].append('-')

    def __fill_schedule(self) -> None:
        self.__error()
        levels = [[]]
        indexs = []
        matr = self.__matrix.tolist()
        for i in range(len(matr)):
            if sum(matr[i]) != 0:
                indexs.append(matr[i].index(1))
            else:
                indexs.append(-1)
                levels[0].append(i)
        mon = self.__input_matrix(matr, indexs)
        level = self.__Prioritization(levels, mon)
        self.__Schedule_Distribution(level, mon)

    def __CheckElement(self, index, arr) -> bool:
        count = 0
        for i in arr[index]:
            if i == 1 and sum(arr[count]) != 0:
                return False
            count += 1
        return True


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
    for i in range(executor_count):
        print(i + 1, schedule.get_schedule_for_executor(i))


if __name__ == '__main__':
    __usage_example()

