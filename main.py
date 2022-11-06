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
        error_msg = _ScheduleTask.__get_param_error(task)
        if error_msg is not None:
            raise ScheduleArgumentException(error_msg)
        self.__task = task
        self.__stage1_start = None
        self.__stage2_start = None

    @property
    def task(self) -> Task:
        """Returns a source Task object."""
        return self.__task

    @property
    def keys_to_sort(self) -> tuple[int, int]:
        """Returns keys that allow to compare this task with another for sorting
        task list."""
        key1 = int(self.__task.stage1 > self.__task.stage2)
        key2 = (-1 * self.__task.stage2
                if self.__task.stage1 > self.__task.stage2
                else self.__task.stage1)
        return tuple((key1, key2))

    @property
    def stage1_start(self) -> int:
        """Returns the first stage start point."""
        return self.__stage1_start

    @stage1_start.setter
    def stage1_start(self, value: int) -> None:
        """Sets the first stage start point.

        :param value: the first stage start point.
        :raise InternalScheduleException: when the stage1 start time is not an
            integer, when the stage1 start time is less than 0.
        :return: None
        """
        if type(value) != int:
            raise InternalScheduleException(
                'The stage1 start time is not an integer', self.task)
        if type(value) != int or value < 0:
            raise InternalScheduleException(
                'The stage1 start time is less than 0', self.task)
        self.__stage1_start = value

    @property
    def stage1_end(self) -> int:
        """Returns the first stage end point."""
        return self.__stage1_start + self.__task.stage1

    @property
    def stage2_start(self) -> int:
        """Returns the second stage start point."""
        return self.__stage2_start

    @stage2_start.setter
    def stage2_start(self, value: int) -> None:
        """Sets the second stage start point.

        :param value: the second stage start point
        :raise InternalScheduleException: when the stage2 start time is not an
            integer, when the stage2 start time is less than the stage1 end
            time.
        :return: None
        """
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
        """Returns the second stage end point."""
        return self.__stage2_start + self.__task.stage2

    @staticmethod
    def __get_param_error(task: Task) -> Union[str, None]:
        if type(task) != Task:
            return 'The task parameter is not a Task'
        return None


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
        error_msg = Schedule.__get_param_error(tasks)
        if error_msg is not None:
            raise ScheduleArgumentException(error_msg)
        self.__tasks = [_ScheduleTask(task) for task in tasks]
        self.__tasks.sort(key=lambda task: task.keys_to_sort)
        self.__set_task_times()

    @property
    def tasks(self) -> tuple[Task]:
        """Returns the source tasks in the optimal order."""
        return tuple([ord_task.task for ord_task in self.__tasks])

    @property
    def tasks_names(self) -> tuple[str]:
        """Returns the source task names in the optimal order."""
        return tuple([ord_task.task.name for ord_task in self.__tasks])

    @property
    def task_count(self) -> int:
        """Returns the source task count."""
        return len(self.__tasks)

    @property
    def total_duration(self) -> int:
        """Returns the duration of all tasks in the schedule."""
        return self.__tasks[-1].stage2_end

    @property
    def stage1_downtime(self) -> int:
        """Returns the duration of downtime for the first stage in the
        schedule."""
        return self.total_duration - self.__tasks[-1].stage1_end

    @property
    def stage2_downtime(self) -> int:
        """Returns the duration of downtime for the second stage in the
        schedule."""
        downtime = self.__tasks[0].task.stage1
        for task_idx in range(1, self.task_count):
            downtime += self.__tasks[task_idx].stage2_start - \
                        self.__tasks[task_idx - 1].stage2_end
        return downtime

    @property
    def total_downtime(self) -> int:
        """Returns the duration of downtime for all stages in the schedule."""
        return self.stage1_downtime + self.stage2_downtime

    @property
    def stage1_schedule(self) -> str:
        """Returns a schedule for the first stage containing time points for
        the start and end of tasks and downtime periods."""
        return Schedule.__get_string_schedule(self.__get_stage1_schedule())

    @property
    def stage2_schedule(self) -> str:
        """Returns a schedule for the second stage containing time points for
        the start and end of tasks and downtime periods."""
        return Schedule.__get_string_schedule(self.__get_stage2_schedule())

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

    def __get_stage1_schedule(self):
        schedule = [{TASK: task.task.name, START: task.stage1_start,
                     END: task.stage1_end} for task in self.__tasks]
        if self.stage1_downtime != 0:
            schedule.append({TASK: DOWNTIME,
                             START: self.total_duration - self.stage1_downtime,
                             END: self.total_duration})
        return schedule

    def __get_stage2_schedule(self):
        first_task = self.__tasks[0]
        schedule = [{TASK: DOWNTIME,
                    START: first_task.stage1_start,
                    END: first_task.stage1_end}]
        for task_idx in range(self.task_count):
            cur_task = self.__tasks[task_idx]
            prev_task = self.__tasks[task_idx - 1]
            if task_idx > 0 and cur_task.stage2_start != prev_task.stage2_end:
                schedule.append({TASK: DOWNTIME, START: prev_task.stage2_end,
                                 END: cur_task.stage2_start})
            schedule.append({TASK: cur_task.task.name,
                             START: cur_task.stage2_start,
                             END: cur_task.stage2_end})
        return schedule

    @staticmethod
    def __get_string_schedule(schedule):
        lines = [f'{idx + 1}. task: {line[TASK]} from: {line[START]} '
                 f'to {line[END]}'
                 for idx, line in enumerate(schedule)]
        return '\n'.join(lines)

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
    print(f'optimal order of execution of tasks: {sched.tasks_names}')
    print(f'minimum task completion time: {sched.total_duration}')
    print(f'downtime of the first stage: {sched.stage1_downtime}')
    print(f'downtime of the second stage: {sched.stage2_downtime}')
    print(f'total downtime:{sched.total_downtime}')
    print(f'\nthe first stage schedule:\n{sched.stage1_schedule}')
    print(f'\nthe second stage schedule:\n{sched.stage2_schedule}')


if __name__ == '__main__':
    main()
