from typing import Union


from task import Task
from custom_exception import ScheduleArgumentException,\
    InternalScheduleException


TASK = 'task'
PART = 'part'
DOWNTIME = 'downtime'


class Schedule:
    """A class for calculating the optimal schedule for a conveyor problem with
    two-stage tasks and two executors.

    Properties
    ----------
    tasks(self) -> tuple[Task]:
        Returns the source tasks in the optimal order.

    tasks_names(self) -> tuple[str]:
        Returns the source task names in the optimal order.

    task_count(self) -> int:
        Returns the source task count.

    total_duration(self) -> int:
        Returns the duration of all tasks in the schedule.

    stage1_downtime(self) -> int:
        Returns the duration of downtime for the first stage in the
        schedule.

    stage2_downtime(self) -> int:
        Returns the duration of downtime for the second stage in the
        schedule.

    total_downtime(self) -> int:
        Returns the duration of downtime for all stages in the schedule.

    stage1_schedule(self) -> str:
        Returns a schedule for the first stage containing time points for
        the start and end of tasks and downtime periods.

    stage2_schedule(self) -> str:
        Returns a schedule for the second stage containing time points for
        the start and end of tasks and downtime periods.
    """
    def __init__(self, tasks: list[Task], executor_count: int):
        """Schedule class constructor to initialize the object.

        :param tasks: a source task list.
        :raise ScheduleArgumentException: when the tasks parameter is not a
            list, when the task list is empty, when the task list contains
            not a Task object.
        """
        error_msg = Schedule.__get_param_error(tasks)
        if error_msg is not None:
            raise ScheduleArgumentException(error_msg)
        self.__tasks = tasks
        self.__executor_count = executor_count
        self.__executer_tasks = [[] for i in range(executor_count)]
        self.__distribute_tasks()

    @property
    def task_count(self) -> int:
        """Returns the source task count."""
        return len(self.__tasks)

    @property
    def executor_count(self) -> int:
        """Returns the executor count."""
        return self.__executor_count

    @property
    def executor_tasks(self):
        """Returns the executor count."""
        return self.__executer_tasks

    def __distribute_tasks(self):
        avg_duration = int(sum([task.duration for task in self.__tasks])
                           / self.executor_count)
        max_duration = max([task.duration for task in self.__tasks])
        duration = max(max_duration, avg_duration)
        task_idx = 0
        part_after_gap = 0
        for executor_idx in range(self.executor_count):
            executor_duration = duration
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
                self.__executer_tasks[executor_idx].append({TASK: current_task,
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


def main():
    tasks = [Task('a', 3), Task('b', 4), Task('c', 6), Task('d', 7),
             Task('e', 7), Task('f', 9), Task('g', 10), Task('h', 12),
             Task('i', 17)]
    sched = Schedule(tasks, 5)
    for idx, exec in enumerate(sched.executor_tasks):
        print(idx)
        for task in exec:
            print(f'{task[TASK]}, part {task[PART]}')


if __name__ == '__main__':
    main()
