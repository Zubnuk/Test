from typing import Union


from task import Task
from custom_exception import ScheduleArgumentException,\
    InternalScheduleException


TASK = 'task'
START = 'start'
END = 'end'
DOWNTIME = 'downtime'


class _ScheduleTask:
    def __init__(self, task: Task):
        self.__task = task
        self.__stage1_start = None
        self.__stage2_start = None

    @property
    def task(self) -> Task:
        return self.__task

    @property
    def keys_to_sort(self) -> tuple[int, int]:
        key1 = int(self.__task.stage1 > self.__task.stage2)
        key2 = (-1 * self.__task.stage2
                if self.__task.stage1 > self.__task.stage2
                else self.__task.stage1)
        return tuple((key1, key2))

    @property
    def stage1_start(self) -> int:
        return self.__stage1_start

    @stage1_start.setter
    def stage1_start(self, value: int) -> None:
        if type(value) != int:
            raise InternalScheduleException(
                'The stage1 start time is not an integer', self.task)
        if type(value) != int or value < 0:
            raise InternalScheduleException(
                'The stage1 start time is less than 0', self.task)
        self.__stage1_start = value

    @property
    def stage1_end(self) -> int:
        return self.__stage1_start + self.__task.stage1

    @property
    def stage2_start(self) -> int:
        return self.__stage2_start

    @stage2_start.setter
    def stage2_start(self, value: int) -> None:
        if type(value) != int:
            raise InternalScheduleException(
                'The stage2 start time is not an integer', self.task)
        if value < self.stage1_end:
            raise InternalScheduleException(
                'The stage2 start time is less than the stage1 end time',
                self.task)
        self.__stage2_start = value

    @property
    def stage2_end(self) -> int:
        return self.__stage2_start + self.__task.stage2


class Schedule:
    def __init__(self, tasks: list[Task]):
        error_msg = Schedule.__get_param_error(tasks)
        if error_msg is not None:
            raise ScheduleArgumentException(error_msg)
        self.__tasks = [_ScheduleTask(task) for task in tasks]
        self.__tasks.sort(key=lambda task: task.keys_to_sort)
        self.__set_task_times()

    @property
    def task_count(self) -> int:
        return len(self.__tasks)

    @property
    def tasks(self) -> tuple[Task]:
        return tuple([ord_task.task for ord_task in self.__tasks])

    @property
    def tasks_names(self) -> tuple[str]:
        return tuple([ord_task.task.name for ord_task in self.__tasks])

    @property
    def total_duration(self) -> int:
        return self.__tasks[-1].stage2_end

    @property
    def stage1_downtime(self) -> int:
        return self.total_duration - self.__tasks[-1].stage1_end

    @property
    def stage2_downtime(self) -> int:
        downtime = self.__tasks[0].task.stage1
        for task_idx in range(1, self.task_count):
            downtime += self.__tasks[task_idx].stage2_start - \
                        self.__tasks[task_idx - 1].stage2_end
        return downtime

    @property
    def total_downtime(self) -> int:
        return self.stage1_downtime + self.stage2_downtime

    @property
    def conveyor1_schedule(self) -> str:
        return Schedule.__get_string_schedule(self.__get_conveyor1_schedule())

    @property
    def conveyor2_schedule(self) -> str:
        return Schedule.__get_string_schedule(self.__get_conveyor2_schedule())

    def __set_task_times(self):
        first_task = self.__tasks[0]
        first_task.stage1_start = 0
        first_task.stage2_start = first_task.stage1_end
        for task_idx in range(1, self.task_count):
            cur_task = self.__tasks[task_idx]
            prev_task = self.__tasks[task_idx - 1]
            cur_task.stage1_start = prev_task.stage1_end
            cur_task.stage2_start = max(cur_task.stage1_end,
                                        prev_task.stage2_end)

    def __get_conveyor1_schedule(self):
        schedule = [{TASK: task.task.name, START: task.stage1_start,
                     END: task.stage1_end} for task in self.__tasks]
        if self.stage1_downtime != 0:
            schedule.append({TASK: DOWNTIME,
                             START: self.total_duration - self.stage1_downtime,
                             END: self.total_duration})
        return schedule

    def __get_conveyor2_schedule(self):
        first_task = self.__tasks[0]
        schedule = [{TASK: DOWNTIME,
                    START: first_task.stage1_start,
                    END: first_task.stage1_end}]
        for task_idx in range(1, self.task_count):
            cur_task = self.__tasks[task_idx]
            prev_task = self.__tasks[task_idx - 1]
            if cur_task.stage2_start != prev_task.stage2_end:
                schedule.append({TASK: DOWNTIME, START: prev_task.stage2_end,
                                 END: cur_task.stage2_start})
            schedule.append({TASK: cur_task.task.name,
                             START: cur_task.stage2_start,
                             END: cur_task.stage2_end})
        return schedule

    @staticmethod
    def __get_string_schedule(schedule):
        lines = [f'{idx}. task: {line[TASK]} from: {line[START]} to {line[END]}'
                 for idx, line in enumerate(schedule)]
        return '\n'.join(lines)

    @staticmethod
    def __get_param_error(tasks: list[Task]) -> Union[str, None]:
        if type(tasks) != list:
            return 'The task parameter is not a list'
        if len(tasks) < 1:
            return 'The task list is empty'
        for idx, value in enumerate(tasks):
            if type(value) != Task:
                return 'The task list contains not a Task object ' \
                       f'in the position {idx}'
        return None


def main():
    tasks = [Task('a', 7, 2), Task('b', 3, 4), Task('c', 2, 5), Task('d', 4, 1),
             Task('e', 6, 6), Task('f', 5, 3), Task('g', 4, 5)]
    sched = Schedule(tasks)
    print(f'optimal order of execution of tasks: {sched.tasks_names}')
    print(f'minimum task completion time: {sched.total_duration}')
    print(f'downtime of the first conveyor: {sched.stage1_downtime}')
    print(f'downtime of the second conveyor: {sched.stage2_downtime}')
    print(f'total downtime of conveyors:{sched.total_downtime}')
    print(f'\nthe first conveyor schedule:\n{sched.conveyor1_schedule}')
    print(f'\nthe second conveyor schedule:\n{sched.conveyor2_schedule}')


main()


if __name__ == '__main__':
    main()
