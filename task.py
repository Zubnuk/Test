from typing import Union


from custom_exception import TaskArgumentException


class Task:
    def __init__(self, name: str, stage1: int, stage2: int):
        error_msg = Task.__get_param_error(name, stage1, stage2)
        if error_msg is not None:
            raise TaskArgumentException(error_msg)
        self._name = name
        self._stage1 = stage1
        self._stage2 = stage2

    def __str__(self):
        return f'task: {self._name}, duration: {self._stage1}/{self._stage2}'

    @property
    def name(self) -> str:
        return self._name

    @property
    def stage1(self) -> int:
        return self._stage1

    @property
    def stage2(self) -> int:
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
