TASK = 'task'
PART = 'part'
DOWNTIME = 'downtime'


def task_checker(task_list: list):
    if task_list is None:
        raise ValueError('Error during initialization of the Schedule object! The tasks parameter is not a list')
    elif len(task_list) == 0:
        raise ValueError('Error during initialization of the Schedule object! The task list is empty')
    for i in range(len(task_list)):
        if type(task_list[i]) is not list:
            raise ValueError(f'Error during initialization of the Schedule object! '
                             f'The task list contains not a list object in the position {i}')
        if type(task_list[i][0]) != str:
            raise ValueError('The task name is not a string')
        if len(task_list[i][0]) < 1:
            raise ValueError('The task name is empty')
        if type(task_list[i][1]) != int:
            raise ValueError('The duration parameter is not an integer')
        if task_list[i][1] < 1:
            raise ValueError('The duration parameter value is less than 1')


def duration(task_list: list, executor_count: int) -> int:
    all_dur = list(map(lambda t: t[1], task_list))
    t_max = max(all_dur)
    t_avg = sum(all_dur)//executor_count
    t_opt = max(t_max, t_avg)
    return t_opt


def downtime(executor_tasks: list, duration: int) -> int:
    downtime_sum = 0
    for executor in executor_tasks:
        # downtime_sum += self.duration - sum(map(lambda d: list(d.values())[0], executor))
        downtime_sum += duration - sum(map(lambda d: d[PART], executor))
    return downtime_sum


def downtime_for_executor(executor_idx: int, executor_tasks: list, duration: int) -> int:
    return duration - sum(map(lambda d: d[PART], executor_tasks[executor_idx]))


def distribute_tasks(task_list: list, executor_count: int, duration: int):
    distr_tasks = list(map(lambda t: [t[0], t[1]], task_list))
    executor_tasks = [[] for i in range(executor_count)]
    for executor in range(executor_count):
        if distr_tasks[-1][1] == 0:
            break
        for task in range(len(task_list)):
            if distr_tasks[task][1] == 0:
                continue
            dt = duration - sum(map(lambda d: d[PART], executor_tasks[executor]))
            current_task_dur = distr_tasks[task][1]
            if dt > 0:
                if dt - current_task_dur >= 0:
                    executor_tasks[executor].append({TASK: task_list[task], PART: distr_tasks[task][1]})
                    distr_tasks[task][1] = 0
                else:
                    executor_tasks[executor].append({TASK: task_list[task], PART: dt})
                    distr_tasks[task][1] = current_task_dur - dt
            else:
                break
    return executor_tasks


def schedule_for_executor(executor_idx: int, executor_tasks: list, duration: int) -> str:
    answer = ""
    hours = 0
    if len(executor_tasks[executor_idx]) == 0:
        answer += f"1. task: downtime from 0 to {duration}"
    for task in range(len(executor_tasks[executor_idx])):
        item = executor_tasks[executor_idx][task]
        key, value = item[TASK], item[PART]
        if task == len(executor_tasks[executor_idx]) - 1:
            if hours + value != duration:
                answer += f"{task + 1}. task: {key[0]} from {hours} to {hours + value}\n"
                answer += f"{task + 2}. task: downtime from {hours+value} to {duration}"
            else:
                answer += f"{task + 1}. task: {key[0]} from {hours} to {hours + value}"
        else:
            answer += f"{task + 1}. task: {key[0]} from {hours} to {hours + value}\n"
        hours += value
    return answer


def create_schedule(task_list: list, executor_count: int):
    task_checker(task_list)
    if executor_count is None or type(executor_count) is not int:
        raise ValueError('Invalid type of executors amount')
    elif executor_count < 1:
        raise ValueError('Invalid executors amount number')
    dur = duration(task_list, executor_count)
    executor_tasks = distribute_tasks(task_list, executor_count, dur)
    dtime = downtime(executor_tasks, dur)
    schedule = {
        'executors': executor_count,
        'tasks': tuple(task_list),
        'tasks amount': len(task_list),
        'duration': dur,
        'downtime': dtime,
        'executor_tasks': executor_tasks,
    }
    for i in range(executor_count):
        d_time = downtime_for_executor(i, executor_tasks, dur)
        schedule[f'downtime executor {i+1}'] = d_time
        schedule[i+1] = f'{schedule_for_executor(i, executor_tasks, dur)}'
    return schedule


def main():
    tasks = [['a', 3], ['b', 4], ['c', 6], ['d', 7],
             ['e', 7], ['f', 9], ['g', 10], ['h', 12],
             ['i', 17]]
    sch = create_schedule(tasks, 1)
    print(sch['duration'])
    print(sch['downtime'])
    print(sch['executor_tasks'])

    for i in range(sch['executors']):
        print(sch[i+1])


if __name__ == '__main__':
    main()
