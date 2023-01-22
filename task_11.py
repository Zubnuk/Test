from typing import Union
import math


from task import Task
from custom_exception import ScheduleArgumentException,\
    InternalScheduleException


TASK = 'task'
PART = 'part'
DOWNTIME = 'downtime'


class Schedule:
    """A class for calculating the optimal schedule for a list of tasks and the
    number of executors.
    Properties
    ----------
    tasks(self) -> tuple[Task]:
        Returns the source task tuple.
    task_count(self) -> int:
        Returns the source task count.
    executor_count(self) -> int:
        Returns the executor count.
    duration(self) -> int:
        Returns the schedule duration.
    downtime(self) -> int:
        Returns the downtime duration for all executors.
    Methods
    -------
    get_downtime_for_executor(self, executor_idx: int) -> int:
        Returns the downtime duration for the executor.
    get_schedule_for_executor(self, executor_idx: int) -> str:
        Returns the schedule for the executor.
    """
    def __init__(self, tasks: list[Task], executor_count: int):
        """Schedule class constructor to initialize the object.
        :param tasks: a source task list.
        :param executor_count: a number of executors for tasks.
        :raise ScheduleArgumentException: when the tasks parameter is not a
            list, when the task list is empty, when the task list contains
            not a Task object.
        """
        error_msg = Schedule.__get_param_error(tasks)
        if error_msg is not None:
            raise ScheduleArgumentException(error_msg)
        self.__tasks: list[Task] = tasks
        self.__executor_count: int = executor_count
        self.__executor_tasks: list[list[dict[str:Task, str: int]]] =\
            [[] for i in range(executor_count)]
        self.__duration: int = self.__calculate_duration()
        self.__distribute_tasks()

    @property
    def tasks(self) -> tuple[Task]:
        return tuple(self.__tasks)
    @property
    def task_count(self) -> int:
        return len(self.__tasks)

    @property
    def executor_count(self) -> int:
        return self.__executor_count

    @property
    def duration(self) -> int:
        return max(max(task.duration for task in self.__tasks), round(sum(task.duration for task in self.__tasks)/self.executor_count))

    @property
    def downtime(self) -> int:
       return  self.duration * self.executor_count - sum(task.duration for task in self.__tasks)

    def get_downtime_for_executor(self, executor_idx: int) -> int:
        """Returns the downtime duration for the executor.
        :param executor_idx: the index for executor.
        :raise InternalScheduleException: when the executor_idx parameter is
            not int, when the executor_idx parameter value is greater ot equal
            than the number of the executors.
        :return: the downtime duration for the executor.
        """
        self.__get_executor_idx_error(executor_idx)
        if (executor_idx +1 )*self.duration - sum(task.duration for task in self.__tasks) < 0:
            return 0
        elif (executor_idx +1 )*self.duration - sum(task.duration for task in self.__tasks) < self.duration:
            return (executor_idx +1 )*self.duration - sum(task.duration for task in self.__tasks)
        else:
            return self.duration 
            

    def get_schedule_for_executor(self, executor_idx: int) -> str:
        """Returns the schedule for the executor.
        :param executor_idx: the index for executor.
        :raise InternalScheduleException: when the executor_idx parameter is
            not int, when the executor_idx parameter value is greater ot equal
            than the number of the executors.
        :return: the schedule for the executor.
        """
        self.__get_executor_idx_error(executor_idx)
        answer = ''
        time = 0
        val = 0
        cter = 0
        if len(self.__executor_tasks[executor_idx]) == 0:
            answer += f"1. task: downtime from 0 to {self.duration}"
        for t in range(len(self.__executor_tasks[executor_idx])):
            if time == self.duration:
                time = 0
            check = self.__executor_tasks[executor_idx][t]._name
            val = self.__executor_tasks[executor_idx][t]._duration
            
            if self.__executor_tasks[executor_idx][t]._name == self.__tasks[-1].name and executor_idx == self.executor_count-1 and self.executor_count != 1:
                if val != self.duration:
                    answer += f"{t+1}. task: {self.__executor_tasks[executor_idx][t]._name} from {time} to {val}\n"
                    answer += f"{t+2}. task: downtime from {val} to {self.duration}"
                else:
                    answer += f"{t+1}. task: {self.__executor_tasks[executor_idx][t]._name} from {time} to {val}"
            elif t == (len(self.__executor_tasks[executor_idx]) - 1):
                if self.__executor_tasks[executor_idx][t]._name == self.__tasks[-1].name and executor_idx != self.executor_count - 1 and time + self.__tasks[t].duration < self.duration and len(self.__executor_tasks[executor_idx + 1]) == 0 and val != self.duration:
                    answer += f"{t+1}. task: {self.__executor_tasks[executor_idx][t]._name} from {time} to {val}\n"
                    answer +=  f"{t+2}. task: downtime from {val} to {self.duration}"
                else:
                    answer += f"{t+1}. task: {self.__executor_tasks[executor_idx][t]._name} from {time} to {self.duration}"
                    time += val
            else:
                if time != 0:
                    answer += f"{t+1}. task: {self.__executor_tasks[executor_idx][t]._name} from {time} to {time + val}\n"
                else:
                    answer += f"{t+1}. task: {self.__executor_tasks[executor_idx][t]._name} from {time} to {time + val}\n"
                time += val
            
        return answer
      

    def __calculate_duration(self) -> int:
        return max(max(task.duration for task in self.__tasks), round(sum(task.duration for task in self.__tasks)/self.executor_count))

    def __distribute_tasks(self) -> None:
        self._tasks = self.__tasks.copy()
        task_names = []
        task_dur = []
        flagg = False
        ex_downtime = -1
        for i in range(len(self.tasks)):
            task_names.append(self.tasks[i].name)
            task_dur.append(self.tasks[i].duration)
        for ex in range(self.executor_count):
            ex_downtime = self.duration
            if task_names[-1] != self.tasks[-1].name: break
            for t in range (self.task_count):
                if task_names[t] != self.tasks[t].name: continue
                if ex_downtime > 0 :
                    if ex_downtime >= task_dur[t]:
                        self.__executor_tasks[ex].append(Task(task_names[t], task_dur[t]))
                        task_names[t] = " " 
                        ex_downtime -= task_dur[t]   
                    else:
                        flagg = True
                        task_dur[t] = task_dur[t]-ex_downtime
                        self.__executor_tasks[ex].append(Task(task_names[t], task_dur[t]))
                        
                        break

    @staticmethod
    def __get_param_error(tasks: list[Task]) -> Union[str, None]:
        if type(tasks) is not list:
            raise ScheduleArgumentException('Error during initialization of the Schedule object! The tasks parameter is not a list')
        elif len(tasks) == 0:
            raise ScheduleArgumentException('Error during initialization of the Schedule object! The task list is empty')
        else:
            for task in range(len(tasks)):
                if type(tasks[task]) is not Task:
                    raise ScheduleArgumentException(f'Error during initialization of the Schedule object! The task list contains not a Task object in the position {task}')

    def __get_executor_idx_error(self, executor_idx: int) -> Union[str, None]:
        if executor_idx is None:
            raise InternalScheduleException('Schedule error! The executor_idx parameter is not int.')
        elif type(executor_idx) is not int:
            raise InternalScheduleException('Schedule error! The executor_idx parameter is not int.')
        elif executor_idx > self.executor_count:
            raise InternalScheduleException('Schedule error! The executor_idx parameter is out of range.')


def main():
    #tasks = [Task('a', 3), Task('b', 4), Task('c', 6), Task('d', 7),
    #         Task('e', 7), Task('f', 9), Task('g', 10), Task('h', 12),
    #         Task('i', 17)]
    #schedule = Schedule(tasks, 5)
    task_a = Task('a',2)
    task_b = Task('b',4)
    task_c = Task('c',6)
    schedule = Schedule([task_a,task_b,task_c],3)
    #task_a = Task('a', 1)
    #task_b = Task('b', 1)
    #task_c = Task('c', 10)
    #schedule = Schedule([task_a, task_b, task_c], 3)
    print(f'Total duration: {schedule.duration}')
    print(f'Total downtime: {schedule.downtime}')
    for i in range(schedule.executor_count):
        print(f'\nExecutor # {i + 1}:')
        print(f'Downtime:  {schedule.get_downtime_for_executor(i)}')
        print(schedule.get_schedule_for_executor(i))
        
if __name__ == '__main__':
    main()