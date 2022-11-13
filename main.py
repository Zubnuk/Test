from typing import Union
import math


from task import Task
from custom_exception import ScheduleArgumentException,\
    InternalScheduleException


TASK = 'task'
PART = 'part'
DOWNTIME = 'downtime'


class Schedule:
    """A class for calculating the optimal schedule for a list of tasks and the
    number of executors.

    Properties
    ----------
    tasks(self) -> tuple[Task]:
        Returns the source task tuple.

    task_count(self) -> int:
        Returns the source task count.

    executor_count(self) -> int:
        Returns the executor count.

    duration(self) -> int:
        Returns the schedule duration.

    downtime(self) -> int:
        Returns the downtime duration for all executors.

    Methods
    -------
    get_downtime_for_executor(self, executor_idx: int) -> int:
        Returns the downtime duration for the executor.

    get_schedule_for_executor(self, executor_idx: int) -> str:
        Returns the schedule for the executor.
    """
    def __init__(self, tasks: list[Task], executor_count: int):
        """Schedule class constructor to initialize the object.

        :param tasks: a source task list.
        :param executor_count: a number of executors for tasks.
        :raise ScheduleArgumentException: when the tasks parameter is not a
            list, when the task list is empty, when the task list contains
            not a Task object.
        """
        error_msg = Schedule.__get_param_error(tasks)
        if error_msg is not None:
            raise ScheduleArgumentException(error_msg)
        self.__tasks = tasks
        self.__executor_count = executor_count
        self.__executor_tasks = [[] for i in range(executor_count)]
        self.__duration = self.__calculate_duration()
        self.__distribute_tasks()

    @property
    def tasks(self) -> tuple[Task]:
        """Returns the source task tuple."""
        return tuple(self.__tasks)

    @property
    def task_count(self) -> int:
        """Returns the source task count."""
        return len(self.__tasks)

    @property
    def executor_count(self) -> int:
        """Returns the executor count."""
        return self.__executor_count

    @property
    def duration(self) -> int:
        """Returns the schedule duration."""
        return self.__duration

    @property
    def downtime(self) -> int:
        """Returns the downtime duration for all executors."""
        return sum([self.get_downtime_for_executor(i)
                    for i in range(self.__executor_count)])

    def get_downtime_for_executor(self, executor_idx: int) -> int:
        """Returns the downtime duration for the executor.

        :param executor_idx: the index for executor.
        :raise InternalScheduleException: when the executor_idx parameter is
            not int, when the executor_idx parameter value is greater ot equal
            than the number of the executors.
        :return: the downtime duration for the executor.
        """
        error_msg = self.__get_executor_idx_error(executor_idx)
        if error_msg is not None:
            raise InternalScheduleException(error_msg)
        sch_tasks = self.__executor_tasks[executor_idx]
        tasks_duration = sum([task[PART] for task in sch_tasks])
        return self.__duration - tasks_duration

    def get_schedule_for_executor(self, executor_idx: int) -> str:
        """Returns the schedule for the executor.

        :param executor_idx: the index for executor.
        :raise InternalScheduleException: when the executor_idx parameter is
            not int, when the executor_idx parameter value is greater ot equal
            than the number of the executors.
        :return: the schedule for the executor.
        """
        error_msg = self.__get_executor_idx_error(executor_idx)
        if error_msg is not None:
            raise InternalScheduleException(error_msg)
        schedule = []
        sch_tasks = self.__executor_tasks[executor_idx]
        time = 0
        num = 1
        stop = 0
        for idx, sch_task in enumerate(sch_tasks):
            num = idx+1
            name = sch_task[TASK].name
            start = time
            stop = time + sch_task[PART]
            time += sch_task[PART]
            schedule.append(f'{num}. task: {name} from {start} to {stop}')
        if self.get_downtime_for_executor(executor_idx) > 0:
            schedule.append(f'{num + 1}. task: {DOWNTIME} from {stop} to '
                            f'{self.__duration}')
        return '\n'.join(schedule)

    def __calculate_duration(self) -> int:
        avg_duration = math.ceil(sum([task.duration for task in self.__tasks])
                                 / self.executor_count)
        max_duration = max([task.duration for task in self.__tasks])
        return max(max_duration, avg_duration)

    def __distribute_tasks(self) -> None:
        task_idx = 0
        part_after_gap = 0
        for executor_idx in range(self.executor_count):
            executor_duration = self.__duration
            while executor_duration > 0 and task_idx < self.task_count:
                current_task = self.__tasks[task_idx]
                if part_after_gap > 0:
                    part = part_after_gap
                    part_after_gap = 0
                    task_idx += 1
                elif current_task.duration <= executor_duration:
                    part = current_task.duration
                    task_idx += 1
                else:
                    part = executor_duration
                    part_after_gap = current_task.duration - executor_duration
                executor_duration -= part
                self.__executor_tasks[executor_idx].append({TASK: current_task,
                                                            PART: part})

    @staticmethod
    def __get_param_error(tasks: list[Task]) -> Union[str, None]:
        if type(tasks) != list:
            return 'The tasks parameter is not a list'
        if len(tasks) < 1:
            return 'The task list is empty'
        for idx, value in enumerate(tasks):
            if type(value) != Task:
                return 'The task list contains not a Task object ' \
                       f'in the position {idx}'
        return None

    def __get_executor_idx_error(self, executor_idx: int) -> Union[str, None]:
        if type(executor_idx) != int:
            return 'The executor_idx parameter is not int.'
        if executor_idx >= self.__executor_count:
            return 'The executor_idx parameter is out of range.'
        return None


def main():
    tasks = [Task('a', 3), Task('b', 4), Task('c', 6), Task('d', 7),
             Task('e', 7), Task('f', 9), Task('g', 10), Task('h', 12),
             Task('i', 17)]
    schedule = Schedule(tasks, 5)
    print(f'Total duration: {schedule.duration}')
    print(f'Total downtime: {schedule.downtime}')
    for i in range(schedule.executor_count):
        print(f'Executor # {i + 1}:')
        print(f'Downtime:  {schedule.get_downtime_for_executor(i)}')
        print(schedule.get_schedule_for_executor(i))


if __name__ == '__main__':
    main()
