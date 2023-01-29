from task import Task


class ScheduleRow:
    def __init__(self, start, duration, task_name):
        self.__task_name = task_name
        self.__start = start
        self.__duration = duration

    @property
    def task_name(self):
        return self.__task_name

    @property
    def start(self):
        return self.__start

    @property
    def duration(self):
        return self.__duration

    @property
    def end(self):
        return self.__start + self.__duration

    def __str__(self):
        return f'{self.task_name} начал в {self.start} закончил {self.end}'


def Sort(tasks: list[Task]) -> list:
    group1 = []
    group2 = []
    for i in tasks:
        if i.stage1 <= i.stage2:
            group1.append(i)
        else:
            group2.append(i)
    group1.sort(key=lambda task: task.stage1)
    group2.sort(key=lambda task: task.stage2, reverse=True)

    return group1 + group2


def Schedule(sort_tasks: list[Task]):
    worker1 = []
    worker2 = []
    for i in range(len(sort_tasks)):
        if i == 0:
            worker1.append(ScheduleRow(0, sort_tasks[i].stage1, sort_tasks[i].name))
        else:
            worker1.append(ScheduleRow(worker1[i - 1].end, sort_tasks[i].stage1, sort_tasks[i].name))

    for i in range(len(sort_tasks)):
        if i == 0:
            worker2.append(ScheduleRow(worker1[i].end, sort_tasks[i].stage2, sort_tasks[i].name))
        else:
            if worker2[i - 1].end < worker1[i].end:
                worker2.append(ScheduleRow(worker1[i].end, sort_tasks[i].stage2, sort_tasks[i].name))
            else:
                worker2.append(ScheduleRow(worker2[i - 1].end, sort_tasks[i].stage2, sort_tasks[i].name))
    print("Первый рабочий")
    for i in worker1:
        print(i)
    print("Второй рабочий")
    for i in worker2:
        print(i)
    print(f'Минимальная длительность: {worker2[len(sort_tasks) - 1].end}')
    return worker2[len(sort_tasks) - 1].end


def main():
    tasks1 = [Task('a', 7, 2), Task('b', 3, 4), Task('c', 2, 5), Task('d', 4, 1),
              Task('e', 6, 6), Task('f', 5, 3), Task('g', 4, 5)]
    Schedule(Sort(tasks1))


'''    tasks2 = [Task('a', 4, 3), Task('b', 5, 2), Task('c', 3, 5), Task('d', 2, 3), Task('e', 4, 4)]
    Schedule(Sort(tasks2))

    tasks3 = [Task('a', 2, 1), Task('b', 3, 4), Task('c', 6, 5)]
    Schedule(Sort(tasks3))'''

if __name__ == '__main__':
    main()
