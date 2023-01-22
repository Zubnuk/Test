from typing import Union


from custom_exception import TaskArgumentException


class Task:
    """Represents a task object that is executed in two stages.

    Properties
    ----------
    name(self) -> str:
        Returns the task name.

    stage1(self) -> int:
        Returns the duration of the first stage of the task.

    stage2(self) -> int:
        Returns the duration of the second stage of the task.
    """
    def __init__(self, name: str, stage1: int, stage2: int):
        """Task class constructor to initialize the object.

        :param name: the task name.
        :param stage1: the duration of the first stage of the task.
        :param stage2: the duration of the second stage of the task.
        :raise TaskArgumentException: when the task name is not a string,
            when the task name is empty, when the duration is not an integer,
            when the duration is less than 1.
        """
        error_msg = Task.__get_param_error(name, stage1, stage2)
        if error_msg is not None:
            raise TaskArgumentException(error_msg)
        self._name: str = name
        self._stage1: int = stage1
        self._stage2: int = stage2

    def __str__(self):
        return f'task: {self._name}, duration: {self._stage1}/{self._stage2}'

    @property
    def name(self) -> str:
        """Returns the task name."""
        return self._name

    @property
    def stage1(self) -> int:
        """Returns the duration of the first stage of the task."""
        return self._stage1

    @property
    def stage2(self) -> int:
        """Returns the duration of the second stage of the task."""
        return self._stage2

    @staticmethod
    def __get_param_error(name: str, stage1: int, stage2: int) -> \
            Union[str, None]:
        if type(name) != str:
            return 'The task name is not a string'
        if len(name) < 1:
            return 'The task name is empty'
        for value, name in zip([stage1, stage2], ['stage1', 'stage2']):
            if type(value) != int:
                return f'The {name} parameter is not an integer'
            if value < 1:
                return f'The {name} parameter value is less than 1'
        return None
