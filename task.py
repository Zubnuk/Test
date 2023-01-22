from typing import Union
from custom_exception import TaskArgumentException

NAME_NOT_STR = 'The task name is not a string'
NAME_EMPTY = 'The task name is empty'
DURATION_PARAM_NOT_INT = 'The duration parameter is not an integer'
DURATION_PARAM_LESS_THAN_ONE = 'The duration parameter value is less than 1'


class Task:
    """Represents a task object with a time duration.
    Properties
    ----------
    name(self) -> str:
        Returns the task name.
    duration(self) -> int:
        Returns the duration of the task.
    """

    def __init__(self, name: str, duration: int):
        """Task class constructor to initialize the object.
        :param name: the task name.
        :param duration: the duration of the task.
        :raise TaskArgumentException: when the task name is not a string,
            when the task name is empty, when the duration is not an integer,
            when the duration is less than 1.
        """
        error_msg = Task.__get_param_error(name, duration)
        if error_msg is not None:
            raise TaskArgumentException(error_msg)
        self._name: str = name
        self._duration: int = duration

    def __str__(self):
        return f'task: {self._name}, duration: {self._duration}'

    @property
    def name(self) -> str:
        """Returns the task name."""
        return self._name

    @property
    def duration(self) -> int:
        """Returns the duration of the task."""
        return self._duration

    def set_name(self, name: str):
        """Set new task name."""
        self._name = name

    def set_duration(self, duration: int):
        """Set new duration of the task."""
        self._duration = duration

    @staticmethod
    def __get_param_error(name: str, duration: int) -> Union[str, None]:
        if type(name) != str:
            return NAME_NOT_STR
        if len(name) < 1:
            return NAME_EMPTY
        if type(duration) != int:
            return DURATION_PARAM_NOT_INT
        if duration < 1:
            return DURATION_PARAM_LESS_THAN_ONE
        return None
