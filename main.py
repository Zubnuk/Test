from typing import Union


from task import Task
from custom_exception import ScheduleArgumentException,\
    InternalScheduleException


TASK = 'task'
START = 'start'
END = 'end'
DOWNTIME = 'downtime'


class _ScheduleTask:
    """An internal class for the schedule, a wrapper for the Task object,
    represents information about the time points for the start and end of the
    task stages.

    Properties
    ----------
    task(self) -> Task:
        Returns a source Task object.

    keys_to_sort(self) -> tuple[int, int]:
        Returns keys that allow to compare this task with another for sorting
        task list.

    stage1_start(self) -> int:
        Returns the first stage start point.

    stage1_start(self, value: int) -> None:
        Sets the first stage start point.

    stage1_end(self) -> int:
        Returns the first stage end point.

    stage2_start(self) -> int:
        Returns the second stage start point.

    stage2_start(self, value: int) -> None:
        Sets the second stage start point.

    stage2_end(self) -> int:
        Returns the second stage end point.

    """
    def __init__(self, task: Task):
        """_ScheduleTask class constructor to initialize the object.

        :param task: a source task object.
        :raise ScheduleArgumentException: when the task parameter is not a Task.
        """
        pass

    @property
    def task(self) -> Task:
        """Returns a source Task object."""
        pass

    @property
    def keys_to_sort(self) -> tuple[int, int]:
        """Returns keys that allow to compare this task with another for sorting
        task list."""
        pass

    @property
    def stage1_start(self) -> int:
        """Returns the first stage start point."""
        pass

    @stage1_start.setter
    def stage1_start(self, value: int) -> None:
        """Sets the first stage start point.

        :param value: the first stage start point.
        :raise InternalScheduleException: when the stage1 start time is not an
            integer, when the stage1 start time is less than 0.
        :return: None
        """
        pass

    @property
    def stage1_end(self) -> int:
        """Returns the first stage end point."""
        pass

    @property
    def stage2_start(self) -> int:
        """Returns the second stage start point."""
        pass

    @stage2_start.setter
    def stage2_start(self, value: int) -> None:
        """Sets the second stage start point.

        :param value: the second stage start point
        :raise InternalScheduleException: when the stage2 start time is not an
            integer, when the stage2 start time is less than the stage1 end
            time.
        :return: None
        """
        pass

    @property
    def stage2_end(self) -> int:
        """Returns the second stage end point."""
        pass


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
    def __init__(self, tasks: list[Task]):
        """Schedule class constructor to initialize the object.

        :param tasks: a source task list.
        :raise ScheduleArgumentException: when the tasks parameter is not a
            list, when the task list is empty, when the task list contains
            not a Task object.
        """
        pass

    @property
    def tasks(self) -> tuple[Task]:
        """Returns the source tasks in the optimal order."""
        pass

    @property
    def tasks_names(self) -> tuple[str]:
        """Returns the source task names in the optimal order."""
        pass

    @property
    def task_count(self) -> int:
        """Returns the source task count."""
        pass

    @property
    def total_duration(self) -> int:
        """Returns the duration of all tasks in the schedule."""
        pass

    @property
    def stage1_downtime(self) -> int:
        """Returns the duration of downtime for the first stage in the
        schedule."""
        pass

    @property
    def stage2_downtime(self) -> int:
        """Returns the duration of downtime for the second stage in the
        schedule."""
        pass

    @property
    def total_downtime(self) -> int:
        """Returns the duration of downtime for all stages in the schedule."""
        pass

    @property
    def stage1_schedule(self) -> str:
        """Returns a schedule for the first stage containing time points for
        the start and end of tasks and downtime periods."""
        pass

    @property
    def stage2_schedule(self) -> str:
        """Returns a schedule for the second stage containing time points for
        the start and end of tasks and downtime periods."""
        pass


def main():
    tasks = [Task('a', 7, 2), Task('b', 3, 4), Task('c', 2, 5), Task('d', 4, 1),
             Task('e', 6, 6), Task('f', 5, 3), Task('g', 4, 5)]
    sched = Schedule(tasks)
    print(f'optimal order of execution of tasks: {sched.tasks_names}')
    print(f'minimum task completion time: {sched.total_duration}')
    print(f'downtime of the first stage: {sched.stage1_downtime}')
    print(f'downtime of the second stage: {sched.stage2_downtime}')
    print(f'total downtime:{sched.total_downtime}')
    print(f'\nthe first stage schedule:\n{sched.stage1_schedule}')
    print(f'\nthe second stage schedule:\n{sched.stage2_schedule}')


if __name__ == '__main__':
    main()
