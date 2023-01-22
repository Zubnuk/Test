class TaskArgumentException(Exception):
    """Exception raised by errors in input parameters during initialization of
    the Task object.
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.__prefix = 'Error during initialization of the Task object! '
        self.message = self.__prefix + message
        super().__init__(self.message)


class ScheduleArgumentException(Exception):
    """Exception raised by errors in input parameters during initialization of
    the Schedule object.
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.__prefix = 'Error during initialization of the Schedule object! '
        self.message = self.__prefix + message
        super().__init__(self.message)


class InternalScheduleException(Exception):
    """Exception raised by errors during processing tasks of the Schedule
    object.
    Attributes:
        message -- explanation of the error
        task -- a Task object
    """

    def __init__(self, message, task):
        self.task = task
        self.__prefix = f'Error during processing task {self.task.name}! '
        self.message = self.__prefix + message
        super().__init__(self.message)
