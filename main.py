from typing import Union, List, Tuple
import math

from task import Task
from custom_exception import ScheduleArgumentException, \
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

    def __init__(self, tasks: List[Task], executor_count: int):
        """Schedule class constructor to initialize the object.
        :param tasks: a source task list.
        :param executor_count: a number of executors for tasks.
        :raise ScheduleArgumentException: when the tasks parameter is not a
            list, when the task list is empty, when the task list contains
            not a Task object.
        """
        error_msg = Schedule.__get_param_error(self, tasks)
        if error_msg is not None:
            raise ScheduleArgumentException(error_msg)
        self.__executor_count: int = executor_count
        self.__tasks: List[Task] = tasks
        self.__executor_tasks: List[List[dict[str:Task, str: int]]] = \
            [[] for i in range(executor_count)]
        self.__duration: int = self.__calculate_duration()
        self.__distribute_tasks()
        self.__executors = self.__distribute_tasks()

    @property
    def tasks(self) -> Tuple[Task]:
        """Returns the source task tuple."""
        return tuple(self.__tasks)

    @property
    def task_count(self) -> int:
        """Returns the source task count."""
        return len(self.tasks)

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
        return self.duration * self.executor_count - sum(self.task_durations)

    @property
    def task_durations(self) -> List[int]:
        """Returns durations for all tasks."""
        return [x.duration for x in self.tasks]

    def get_downtime_for_executor(self, executor_idx: int) -> int:
        """Returns the downtime duration for the executor.
        :param executor_idx: the index for executor.
        :raise InternalScheduleException: when the executor_idx parameter is
            not int, when the executor_idx parameter value is greater ot equal
            than the number of the executors.
        :return: the downtime duration for the executor.
        """
        if (executor_idx + 1) * self.duration <= sum(self.task_durations):
            return 0
        elif (executor_idx + 1) * self.duration - sum(self.task_durations) < self.duration:
            return (executor_idx + 1) * self.duration - sum(self.task_durations)
        else:
            return self.duration

    def get_schedule_for_executor(self, executor_idx: int) -> str:
        """Returns the schedule for the executor.
        :param executor_idx: the index for executor.
        :raise InternalScheduleException: when the executor_idx parameter is
            not int, when the executor_idx parameter value is greater ot equal
            than the number of the executors.
        :return: the schedule for the executor.
        """
        if self.__get_executor_idx_error(executor_idx) is not None:
            raise InternalScheduleException(self.__get_executor_idx_error(executor_idx))
        return self.__executors[executor_idx]

    def __calculate_duration(self) -> int:
        Tmax = max(self.task_durations)
        Tavg = sum(self.task_durations) / self.executor_count
        return max(Tmax, round(Tavg))

    def __distribute_tasks(self) -> List[str]:
        sum = 0
        str = ''
        counter = 1
        executors = []
        for i in range(len(self.tasks)):
            if self.tasks[i].duration + sum < self.duration:
                str += f"{counter}. task: {self.tasks[i].name} from {sum} to {sum + self.tasks[i].duration}\n"
                counter += 1
                sum += self.tasks[i].duration
            elif self.tasks[i].duration + sum == self.duration:
                str += f"{counter}. task: {self.tasks[i].name} from {sum} to {sum + self.tasks[i].duration}\n"
                counter = 1
                sum = 0
                executors.append(str[:-1:])
                str = ''
            else:
                str += f"{counter}. task: {self.tasks[i].name} from {sum} to {self.duration}\n"
                counter += 1
                executors.append(str[:-1:])
                str = ''
                sum += self.tasks[i].duration
                temp = sum - self.duration
                counter = 1
                str += f"{counter}. task: {self.tasks[i].name} from 0 to {temp}\n"
                counter += 1
                sum = temp
        if sum < self.duration:
            str += f"{counter}. task: downtime from {sum} to {self.duration}\n"
        executors.append(str[:-1:])
        for i in range(self.executor_count - len(executors)):
            str = f"1. task: downtime from 0 to {self.duration}\n"
            executors.append(str[:-1:])
        return executors

    def __get_param_error(self, tasks: List[Task]) -> Union[str, None]:
        if tasks is None:
            return 'Error during initialization of the Schedule object! The tasks parameter is not a list'
        if tasks == []:
            return 'Error during initialization of the Schedule object! The task list is empty'
        for i in range(len(tasks)):
            if type(tasks[i]) is not Task:
                return f'Error during initialization of the Schedule object! The task list contains not a Task object in the position {i}'

    def __get_executor_idx_error(self, executor_idx: int) -> Union[str, None]:
        if type(executor_idx) is not int:
            return 'The executor_idx parameter is not int'
        if executor_idx >= self.executor_count:
            return 'The executor_idx parameter value is greater ot equal than the number of the executors'


def main():
    tasks = [Task('a', 1), Task('b', 1), Task('c', 1)]
    schedule = Schedule(tasks, 5)
    print(f'Total duration: {schedule.duration}')
    print(f'Total downtime: {schedule.downtime}')
    schedule.get_schedule_for_executor(0)
    for i in range(schedule.executor_count):
        print(f'\nExecutor # {i + 1}:')
        print(f'Downtime:  {schedule.get_downtime_for_executor(i)}')
        print(schedule.get_schedule_for_executor(i))


if __name__ == '__main__':
    main()