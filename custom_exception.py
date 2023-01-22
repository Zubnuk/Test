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
    """Exception raised by errors in input parameters during Schedule calculation.
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.__prefix = 'Error during Schedule calculation! '
        self.message = self.__prefix + message
        super().__init__(self.message)
