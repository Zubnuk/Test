from typing import Union


from task import Task
from custom_exception import ScheduleArgumentException

class ScheduleRow:
    """A class for a schedule row.
    Properties
    ----------
    task_name(self) -> str:
        Returns the task name or downtime string, if row represents
        a downtime period.
    is_downtime(self) -> bool:
        Returns True if row represents a downtime period.
    start(self) -> float:
        Returns a start point for the period.
    duration(self) -> float:
        Returns the duration of the row period.
    end(self) -> float:
        Returns an end point for the period.
    """
    def __init__(self, start: float, duration: float,
                 task_name: Union[str, None] = None,
                 is_downtime: bool = False):
        """Schedule row class constructor to initialize the object.
        :param start: a start point for the period.
        :param duration: a duration of the task.
        :param task_name: the task name.
        :param is_downtime: True if row represents a downtime period.
        :raise ScheduleArgumentException: when the task_name parameter for
            downtime period is not empty, when the task_name parameter is not
            a string, when the task_name parameter is empty, when the start
            parameter is not a number, when the start parameter is less than
            zero, when the duration parameter is not a number, when the
            duration parameter is less or equal than zero.
        """
        error_msg = ScheduleRow.__get_param_error(task_name, start, duration,
                                                  is_downtime)
        if error_msg is not None:
            raise ScheduleArgumentException(error_msg)
        self.__task_name = task_name
        self.__start = start
        self.__duration = duration
        self.__is_downtime = is_downtime

    @property
    def task_name(self) -> str:
        """Returns the task name or downtime string, if row represents
        a downtime period."""
        return 'downtime' if self.__is_downtime else self.__task_name

    @property
    def is_downtime(self) -> bool:
        """Returns True if row represents a downtime period."""
        return self.__is_downtime

    @property
    def start(self) -> float:
        """Returns a start point for the period."""
        return self.__start

    @property
    def duration(self) -> float:
        """Returns the duration of the row period."""
        return self.__duration

    @property
    def end(self) -> float:
        """Returns an end point for the period."""
        return self.__start + self.__duration

    def __str__(self):
        return f'task {self.task_name} from {self.start} to {self.end}'

    def __eq__(self, other):
        return (self.task_name == other.task_name and self.start == other.start
                and self.duration == other.duration)

    def __hash__(self):
        return hash((self.task_name, self.start, self.duration))

    @staticmethod
    def __get_param_error(task_name: str, start: float, duration: float,
                          is_downtime: bool) -> Union[str, None]:
        if is_downtime and task_name is not None:
            return 'The task_name parameter for downtime period is not empty'
        if type(task_name) != str and not is_downtime:
            return 'The task_name parameter is not a string'
        if task_name == '':
            return 'The task_name parameter is empty'
        if type(start) not in [float, int]:
            return 'The start parameter is not a number'
        if start < 0:
            return 'The start parameter is less than zero'
        if type(duration) not in [float, int]:
            return 'The duration parameter is not a number'
        if duration <= 0:
            return 'The duration parameter is less or equal than zero'
        return None


class Schedule:
    """A class for calculating the optimal schedule for a conveyor problem with
    two-stage tasks and two executors.

    Properties
    ----------
    tasks(self) -> tuple[Task]:
        Returns the source tasks in the optimal order.

    task_count(self) -> int:
        Returns the source task count.

    duration(self) -> float:
        Returns the duration of all tasks in the schedule.

    stage1_schedule(self) -> tuple[ScheduleRow]:
        Returns a schedule for the first stage containing time points for
        the start and end of tasks and downtime periods.

    stage2_schedule(self) -> tuple[ScheduleRow]:
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
        error_msg = Schedule.__get_param_error(tasks)
        if error_msg is not None:
            raise ScheduleArgumentException(error_msg)
        self.__tasks = self.__sort_tasks(tasks)
        self.__stages_schedule: list[list[ScheduleRow]] = [[], []]
        self.__fill_schedule()

    @property
    def tasks(self) -> tuple[Task]:
        """Returns the source tasks in the optimal order."""
        return tuple(self.__tasks)

    @property
    def task_count(self) -> int:
        """Returns the source task count."""
        return len(self.__tasks)

    @property
    def duration(self) -> float:
        """Returns the duration of all tasks in the schedule."""
        return self.stage2_schedule[-1].end

    @property
    def stage1_schedule(self) -> tuple[ScheduleRow]:
        """Returns a schedule for the first stage containing time points for
        the start and end of tasks and downtime periods."""
        return tuple(self.__stages_schedule[0])

    @property
    def stage2_schedule(self) -> tuple[ScheduleRow]:
        """Returns a schedule for the second stage containing time points for
        the start and end of tasks and downtime periods."""
        return tuple(self.__stages_schedule[1])

    def __sort_tasks(self, tasks: list[Task]) -> list[Task]:
        pass

    def __fill_schedule(self):
        pass

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
    tasks = [Task('a', 7, 2), Task('b', 3, 4), Task('c', 2, 5), Task('d', 4, 1),
             Task('e', 6, 6), Task('f', 5, 3), Task('g', 4, 5)]
    sched = Schedule(tasks)
    print(f'minimum task completion time: {sched.duration}')
    print('\nthe first stage schedule:')
    for row in sched.stage1_schedule:
        print(row)
    print('\nthe second stage schedule:')
    for row in sched.stage2_schedule:
        print(row)


if __name__ == '__main__':
    main()
