from typing import Union
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
        self.__tasks: list[Task] = tasks
        self.__executor_count: int = executor_count
        self.__executor_tasks: list[list[dict[str:Task, str: int]]] = \
            [[] for i in range(executor_count)]
        self.__duration: int = self.__calculate_duration()
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
        t_max = max(task.duration for task in self.tasks)
        t_avg = sum(task.duration for task in self.tasks) / self.executor_count
        return max(t_max, t_avg)

    @property
    def downtime(self) -> int:
        """Returns the downtime duration for all executors."""
        buf = 0
        for task in self.tasks:
            buf += task.duration
        return self.duration * self.executor_count - buf

    def get_downtime_for_executor(self, executor_idx: int) -> int:
        """Returns the downtime duration for the executor.

        :param executor_idx: the index for executor.
        :raise InternalScheduleException: when the executor_idx parameter is
            not int, when the executor_idx parameter value is greater ot equal
            than the number of the executors.
        :return: the downtime duration for the executor.
        """
        self.__get_executor_idx_error(executor_idx)
        buf_dur = (executor_idx + 1) * self.duration - sum(task.duration for task in self.tasks)
        if buf_dur < 0:
            return 0
        elif buf_dur > self.duration:
            return self.duration
        else:
            return buf_dur

    def get_schedule_for_executor(self, executor_idx: int) -> str:
        """Returns the schedule for the executor.

        :param executor_idx: the index for executor.
        :raise InternalScheduleException: when the executor_idx parameter is
            not int, when the executor_idx parameter value is greater ot equal
            than the number of the executors.
        :return: the schedule for the executor.
        """
        self.__get_executor_idx_error(executor_idx)
        itog = ''
        counter = 0
        for info in self.__distribute_tasks()[executor_idx]:
            if counter > 0 and counter - 1 < len(self.__distribute_tasks()[executor_idx]):
                itog += '\n'
            itog += info
            counter += 1
        return itog

    def __calculate_duration(self) -> int:
        return self.duration

    def __get_private_executor_tasks(self) -> None:
        task_idx = 0
        part_after_gap = 0
        for executor_idx in range(self.__executor_count):
            executor_duration = self.duration
            while executor_duration > 0 and task_idx < len(self.tasks):
                current_task = self.tasks[task_idx]
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

    def __distribute_tasks(self) -> list[[str]]:
        used_time = 0
        tasks_info = []
        task_num = 0
        executions = []
        for i in range(len(self.tasks)):
            if used_time + self.tasks[i].duration < self.duration:
                task_num += 1
                tasks_info.append(
                    f'{task_num}. task: {self.tasks[i].name} from {used_time} to {used_time + self.tasks[i].duration}')
                used_time += self.tasks[i].duration
            elif used_time + self.tasks[i].duration == self.duration:
                task_num += 1
                tasks_info.append(
                    f'{task_num}. task: {self.tasks[i].name} from {used_time} to {used_time + self.tasks[i].duration}')
                used_time = 0
                task_num = 0
                executions.append(tasks_info)
                tasks_info = []
            else:
                task_num += 1
                tasks_info.append(f'{task_num}. task: {self.tasks[i].name} from {used_time} to {self.duration}')
                executions.append(tasks_info)
                used_time = used_time + self.tasks[i].duration - self.duration
                task_num = 1
                tasks_info = []
                tasks_info.append(f'{task_num}. task: {self.tasks[i].name} from 0 to {used_time}')
        if used_time < self.duration:
            task_num += 1
            tasks_info.append(f'{task_num}. task: downtime from {used_time} to {self.duration}')
            executions.append(tasks_info)
        for i in range(self.executor_count - len(executions)):
            executions.append([f'1. task: downtime from 0 to {self.duration}'])
        self.__get_private_executor_tasks()
        return executions

    @staticmethod
    def __get_param_error(tasks: list[Task]) -> Union[str, None]:
        if tasks is None:
            raise ScheduleArgumentException('The tasks parameter is not a list')
        if len(tasks) < 1:
            raise ScheduleArgumentException('The task list is empty')
        for i in range(len(tasks)):
            if type(tasks[i]) is not Task:
                raise ScheduleArgumentException(f'The task list contains not a Task object in the position {i}')

    def __get_executor_idx_error(self, executor_idx: int) -> Union[str, None]:
        if type(executor_idx) is not int:
            raise InternalScheduleException('The executor_idx parameter is not int.')
        if executor_idx >= self.executor_count:
            raise InternalScheduleException('The executor_idx parameter is out of range.')


def main():
    task_a = Task('a', 1)
    task_b = Task('b', 1)
    task_c = Task('c', 1)
    schedule = Schedule([task_a, task_b, task_c], 3)
    print(f'Total duration: {schedule.duration}')
    print(f'Total downtime: {schedule.downtime}')
    for i in range(schedule.executor_count):
        print(f'\nExecutor # {i + 1}:')
        print(f'Downtime:  {schedule.get_downtime_for_executor(i)}')
        print(f'Schedule: {schedule.get_schedule_for_executor(i)}')


if __name__ == '__main__':
    main()
