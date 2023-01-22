from typing import List
from task import Task
from custom_exception import ScheduleArgumentException

TASKS_PARAM_NOT_LIST = 'The tasks parameter is not a list'
TASKS_LIST_EMPTY = 'The task list is empty'
NOT_TASK_OBJ_IN_TASK_LIST = 'The task list contains not a Task object in the position'


def error_handler(tasks: List[Task]) -> str:
    if type(tasks) is not list:
        return TASKS_PARAM_NOT_LIST
    elif len(tasks) == 0:
        return TASKS_LIST_EMPTY
    else:
        for idx in range(len(tasks)):
            if type(tasks[idx]) is not Task:
                return f'{NOT_TASK_OBJ_IN_TASK_LIST} {idx}'


def schedule(tasks: List[Task], workers_count: int) -> str:
    error_msg = error_handler(tasks)
    if error_msg is not None:
        raise ScheduleArgumentException(error_msg)

    s_duration = schedule_duration(tasks, workers_count)
    optimal_schedule = workers_schedule(tasks, workers_count, s_duration)

    schedule_to_str = ''
    for idx in range(len(optimal_schedule)):
        worker = optimal_schedule[idx]
        schedule_to_str += f'Worker {idx + 1}: {str(worker)}\n'

    schedule_to_str += f'Schedule duration: {s_duration}'

    return schedule_to_str


def schedule_duration(tasks_duration_list: List[Task], workers_count: int):
    durations_list = []
    for task in tasks_duration_list:
        durations_list.append(task.duration)

    average_duration = sum(durations_list) / workers_count
    max_duration = max(durations_list)
    if average_duration >= float(max_duration):
        return average_duration
    else:
        return max_duration


def workers_schedule(tasks_duration_list: List[Task], workers_count: int, time: int):
    optimal_schedule = list()

    tasks_duration_dict = dict()
    for task in tasks_duration_list:
        tasks_duration_dict[task.name] = task.duration

    for i in range(workers_count):
        optimal_schedule.append(dict())

    for item in optimal_schedule:
        curr_worker_duration = 0
        for key in list(tasks_duration_dict):
            if curr_worker_duration < time:
                if time - curr_worker_duration >= tasks_duration_dict[key]:
                    item[key] = tasks_duration_dict[key]
                    curr_worker_duration += tasks_duration_dict[key]
                    del tasks_duration_dict[key]
                else:
                    item[key] = time - curr_worker_duration
                    tasks_duration_dict[key] -= (time - curr_worker_duration)
                    curr_worker_duration += (time - curr_worker_duration)
            else:
                break

    return optimal_schedule


def main():
    tasks_duration_list = [Task('A', 3), Task('B', 4), Task('C', 6), Task('D', 7),
                           Task('E', 7), Task('F', 9), Task('G', 10), Task('H', 12),
                           Task('I', 17)]
    workers_count = 5

    print(schedule(tasks_duration_list, workers_count))


if __name__ == '__main__':
    main()
