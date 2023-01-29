
class Task:
    def __init__(self, name, stage1, stage2):

        self._name = name
        self._stage1 = stage1
        self._stage2 = stage2

    def __str__(self):
        return f'{self._name}: ({self._stage1},{self._stage2})'

    @property
    def name(self) -> str:
        return self._name

    @property
    def stage1(self) -> int:
        return self._stage1

    @property
    def stage2(self) -> int:
        return self._stage2
