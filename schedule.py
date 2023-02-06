import networkx as nx

GRAPH_MUST_NOT_BE_NONE = 'Graph must not be None!'
EXEC_COUNT_MUST_NOT_BE_NONE = 'Executor count must not be None!'
EXEC_COUNT_MUST_BE_MORE_THAN_ZERO = 'Executor count must be more than 0!'
GRAPH_MUST_BE_DIGRAPH = 'Graph must be type of DiGraph!'
GRAPH_IS_EMPTY = 'Graph is empty!'


class Schedule:
    def __init__(self, graph: nx.DiGraph, executor_count: int):
        self.__graph = graph
        self.__executor_count = executor_count
        self.__error_handler()
        self.__vertices_graph = graph.nodes
        self.__matrix = (nx.adjacency_matrix(graph)).toarray()
        self.__schedule = [[] for _ in range(executor_count)]
        self.__fill_schedule()

    def __error_handler(self):
        """Error-checking method"""

        if self.__graph is None:
            raise ValueError(GRAPH_MUST_NOT_BE_NONE)
        if self.__executor_count is None:
            raise ValueError(EXEC_COUNT_MUST_NOT_BE_NONE)
        if self.__executor_count < 1:
            raise ValueError(EXEC_COUNT_MUST_BE_MORE_THAN_ZERO)
        if type(self.__graph) is not nx.DiGraph:
            raise ValueError(GRAPH_MUST_BE_DIGRAPH)
        if len(self.__graph.nodes) < 1:
            raise ValueError(GRAPH_IS_EMPTY)

    def get_schedule(self) -> list[list[str]]:
        """
        :return: schedule for all executors
        """

        return self.__schedule

    def get_schedule_for_executor(self, executor_idx: int) -> list[str]:
        """
        :param executor_idx: Executor's number (1, 2, 3...)
        :return: Schedule for particular executor
        """

        if executor_idx < 1:
            raise ValueError('Input executor\'s number but not executor\'s index!')
        return self.__schedule[executor_idx - 1]

    def __fill_schedule(self) -> None:
        """Method of filling in the schedule"""
        solved_task_count = 0
        priorities = list(range(len(self.__vertices_graph), 0, -1))  # список приоритетов задач
        priority_index = 0  # текущий индекс приоритета для проверки и смещения по задачам
        executor_index = 0  # текущий индекс работника для заполнения расписания работника
        solved_tasks = list()  # список задач решенных за один момент времени
        while self.__check_finish(priorities, self.__schedule):
            ready_to_solve_any_task_count = 0  # счетчик возможных для решения задач
            ready_to_solve_priority_task_count = 0  # счетчик решенных задач за один момент времени
            for i, name in enumerate(self.__graph.nodes):
                relation_count = 0  # счетчик проверки наличия зависимости задачи
                negative = False
                for j in range(len(self.__vertices_graph)):
                    if self.__matrix[j][i] == -1:
                        negative = True
                        break
                    relation_count += self.__matrix[j][i]
                if negative:
                    continue
                if relation_count == 0:  # если задача - исток
                    ready_to_solve_any_task_count += 1
                    if priorities[priority_index] == self.__graph.nodes[name]['weight']:
                        ready_to_solve_priority_task_count += 1
                        self.__schedule[executor_index].append(name)
                        solved_task_count += 1
                        executor_index += 1
                        solved_tasks.append(i)  # записываем индекс решенной задачи для именения зависимостей
                        self.__set_solved_status(i)
                        priorities.remove(self.__graph.nodes[name]['weight'])
                if executor_index == self.__executor_count:
                    break
            if ready_to_solve_priority_task_count == 0:  # если нет выполненных задач сдвигаем приоритет
                priority_index += 1

            if ready_to_solve_any_task_count == 0:  # если не доступных для решения задач в момент времени
                temp = executor_index
                for i in range(executor_index, self.__executor_count):
                    self.__schedule[i].append("-")
                    temp += 1
                executor_index = temp  # сохраняем значение индекса работника для следующей проверки

            if executor_index == self.__executor_count:
                executor_index = 0
                priority_index = 0
                self.__reset_relation(solved_tasks)
                solved_tasks.clear()

    def __reset_relation(self, solved_tasks: list) -> None:
        """Method for deleting a relation with completed task"""
        for task_index in solved_tasks:
            for i in range(len(self.__vertices_graph)):
                for j in range(len(self.__vertices_graph)):
                    if task_index == j and task_index != i:  # гарантируем что будет хотя бы одно (-1) (task_index != i)
                        self.__matrix[j][i] = 0

    def __set_solved_status(self, solved_task_index: int) -> None:
        """Method for setting the value of -1 for a completed task"""
        for i in range(len(self.__vertices_graph)):
            self.__matrix[i][solved_task_index] = -1

    @staticmethod
    def __check_finish(priorities, schedule) -> bool:
        """
        Method for checking completion of filling of schedule
        :param priorities: Task prioritisation list
        :param schedule: Сurrent filled schedule
        :return: Fully filled (False) or Partially filled (True)
        """

        count_schedule = len(schedule[0])
        count_task = len(priorities)
        if count_task != 0 or count_schedule == 0:
            return True

        for i in schedule:
            if count_schedule != len(i):
                return True

        return False


def __usage_example():
    graph = nx.DiGraph()
    graph.add_nodes_from([('a', {'color': 'red', 'weight': 5}), ('b', {'color': 'red', 'weight': 2}),
                          ('c', {'color': 'red', 'weight': 1}), ('d', {'color': 'red', 'weight': 6}),
                          ('e', {'color': 'red', 'weight': 11}), ('f', {'color': 'red', 'weight': 8}),
                          ('g', {'color': 'red', 'weight': 9}), ('h', {'color': 'red', 'weight': 10}),
                          ('i', {'color': 'red', 'weight': 7}), ('j', {'color': 'red', 'weight': 12}),
                          ('k', {'color': 'red', 'weight': 13}), ('l', {'color': 'red', 'weight': 3}),
                          ('m', {'color': 'red', 'weight': 4})])
    graph.add_edges_from([('j', 'e'), ('k', 'e'), ('e', 'd'),
                          ('h', 'a'), ('g', 'a'), ('f', 'a'),
                          ('i', 'l'), ('d', 'l'), ('a', 'b'),
                          ('m', 'b'), ('l', 'c'), ('b', 'c')])

    s = Schedule(graph, 3)
    print(s.get_schedule())


if __name__ == '__main__':
    __usage_example()
