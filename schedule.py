import networkx as nx
import scipy

class Schedule:
    def __init__(self, graph: nx.Graph, executor_count: int):
        self.__graph = graph
        self.__executor_count = executor_count
        self.__error()
        self.__matrix = (nx.adjacency_matrix(graph)).toarray()
        self.__schedule = [[] for _ in range(executor_count)]
        self.__fill_schedule()

    def get_schedule(self) -> list[list[str]]:
        return self.__schedule

    def get_schedule_for_executor(self, executor_idx: int) -> list[str]:
        return self.__schedule[executor_idx]

    def __error(self):
        if self.__graph is None:
            raise ValueError("Error during initialization of the Schedule object! The graph parameter is not a graph'")
        if self.__executor_count is None:
            raise ValueError("executor_count None")
        if self.__executor_count < 1:
            raise ValueError("Invalid executors amount number")
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
            if sum(mon[i]) == 0:
                mon[i][0] = 2
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
            for i in level:
                if self.__CheckElement(i, arr):
                    count += 1
                    self.__schedule[count - 1].append(list(self.__graph.nodes)[i])
                    index_row.append(i)
                if count == self.__executor_count or len(level) == 0:
                    break
            for i in range(count):
                arr[index_row[i]] = [0 for i in range(len(arr[0]))]
                level.remove(index_row[i])
            if count != self.__executor_count:
                for i in range(count, self.__executor_count):
                    self.__schedule[i].append('-')

    def __fill_schedule(self) -> None:
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
            if i == 1 and (sum(arr[count]) != 0 or arr[count][0] == 2):
                return False
            count += 1
        return True


def __usage_example():
    graph = nx.DiGraph()
    graph.add_nodes_from([('a', {'color': 'red'}), ('b', {'color': 'red'}), ('c', {'color': 'red'}), ('d', {'color': 'red'})])
    graph.add_edges_from([('a', 'b'), ('b', 'c')])
    executor_count = 3
    schedule = Schedule(graph, executor_count)
    print(f'Schedule for {executor_count} executers:')
    for i in range(executor_count):
        print(i+1, schedule.get_schedule_for_executor(i))


if __name__ == '__main__':
    __usage_example()
