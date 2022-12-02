from typing import Union

from custom_exception import InternalScheduleException, ScheduleArgumentException

from task import Task

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
        self.__executor_tasks: list[list[dict[str:Task, str: int]]] =\
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
        return self.__duration

    @property
    def downtime(self) -> int:
        """Returns the downtime duration for all executors."""
        downtime_sum = 0
        for executor in self.__executor_tasks:
            # downtime_sum += self.duration - sum(map(lambda d: list(d.values())[0], executor))
            downtime_sum += self.duration - sum(map(lambda d: d[PART], executor))
        return downtime_sum

    def get_downtime_for_executor(self, executor_idx: int) -> int:
        """Returns the downtime duration for the executor.

        :param executor_idx: the index for executor.
        :raise InternalScheduleException: when the executor_idx parameter is
            not int, when the executor_idx parameter value is greater ot equal
            than the number of the executors.
        :return: the downtime duration for the executor.
        """
        self.__get_executor_idx_error(executor_idx)
        # return self.duration - sum(map(lambda d: list(d.values())[0], self.__executor_tasks[executor_idx]))
        return self.duration - sum(map(lambda d: d[PART], self.__executor_tasks[executor_idx]))

    def get_schedule_for_executor(self, executor_idx: int) -> str:
        """Returns the schedule for the executor.

        :param executor_idx: the index for executor.
        :raise InternalScheduleException: when the executor_idx parameter is
            not int, when the executor_idx parameter value is greater ot equal
            than the number of the executors.
        :return: the schedule for the executor.
        """
        self.__get_executor_idx_error(executor_idx)
        answer = ""
        hours = 0
        if len(self.__executor_tasks[executor_idx]) == 0:
            answer += f"1. task: downtime from 0 to {self.duration}"
        for task in range(len(self.__executor_tasks[executor_idx])):
            item = self.__executor_tasks[executor_idx][task]
            key, value = item[TASK], item[PART]
            if task == len(self.__executor_tasks[executor_idx]) - 1:
                if hours + value != self.duration:
                    answer += f"{task + 1}. task: {key.name} from {hours} to {hours + value}\n"
                    answer += f"{task + 2}. task: downtime from {hours+value} to {self.duration}"
                else:
                    answer += f"{task + 1}. task: {key.name} from {hours} to {hours + value}"
            else:
                answer += f"{task + 1}. task: {key.name} from {hours} to {hours + value}\n"
            hours += value
        return answer

    def __calculate_duration(self) -> int:
        t_max = max(map(lambda t: t.duration, self.tasks))
        t_avg = sum(map(lambda Task: Task.duration, self.tasks))//self.executor_count
        t_opt = max(t_max, t_avg)
        return t_opt

    def __distribute_tasks(self) -> None:
        distr_tasks = list(map(lambda Task: [Task.name, Task.duration], self.tasks))
        for executor in range(self.executor_count):
            if distr_tasks[-1][1] == 0:
                break
            for task in range(self.task_count):
                if distr_tasks[task][1] == 0:
                    continue
                downtime = self.duration - sum(map(lambda d: d[PART], self.__executor_tasks[executor]))
                current_task_dur = distr_tasks[task][1]
                if downtime > 0:
                    if downtime - current_task_dur >= 0:
                        self.__executor_tasks[executor].append({TASK: self.tasks[task], PART: distr_tasks[task][1]})
                        distr_tasks[task][1] = 0
                    else:
                        self.__executor_tasks[executor].append({TASK: self.tasks[task], PART: downtime})
                        distr_tasks[task][1] = current_task_dur - downtime
                else:
                    break

    @staticmethod
    def __get_param_error(tasks: list[Task]) -> Union[str, None]:
        if type(tasks) is not list:
            raise ScheduleArgumentException('Error during initialization of the Schedule object! The tasks parameter is not a list')
        elif len(tasks) == 0:
            raise ScheduleArgumentException('Error during initialization of the Schedule object! The task list is empty')
        else:
            for task in range(len(tasks)):
                if type(tasks[task]) is not Task:
                    raise ScheduleArgumentException(f'Error during initialization of the Schedule object! The task list contains not a Task object in the position {task}')

    def __get_executor_idx_error(self, executor_idx: int) -> Union[str, None]:
        if executor_idx is None:
            raise InternalScheduleException('Schedule error! The executor_idx parameter is not int.')
        elif type(executor_idx) is not int:
            raise InternalScheduleException('Schedule error! The executor_idx parameter is not int.')
        elif executor_idx > self.executor_count:
            raise InternalScheduleException('Schedule error! The executor_idx parameter is out of range.')


def main():
    tasks = [Task('a', 3), Task('b', 4), Task('c', 6), Task('d', 7),
             Task('e', 7), Task('f', 9), Task('g', 10), Task('h', 12),
             Task('i', 17)]
    schedule = Schedule(tasks, 5)
    print(f'Total duration: {schedule.duration}')
    print(f'Total downtime: {schedule.downtime}')
    for i in range(schedule.executor_count):
        print(f'\nExecutor # {i + 1}:')
        print(f'Downtime:  {schedule.get_downtime_for_executor(i)}')
        print(schedule.get_schedule_for_executor(i))


if __name__ == '__main__':
    main()
