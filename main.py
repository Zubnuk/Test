import random as rnd
from colorama import Fore, Style




#return: [[ [A,1], [B,1],... ],...]
def main(n, t, tasks):    
    if n<=0:
        raise Exception('количество исполнителей <= 0')
    if t<=0:
        raise Exception('количество работ <= 0')
    if len([i for i in tasks if i[1]<=0])>0:
        raise Exception(f'длительность работ {", ".join([i[0] for i in tasks if i[1]<=0])} <= 0')
    try: 
        int(n)
        int(t)
    except:
        raise Exception('количество задач и количество исполнителе должны быть типа инт')
    tasks_length = [i[1] for i in tasks]
    #tmax
    t_max = max(tasks_length)

    t_avg = sum(tasks_length) / n

    t_opt = max(t_max, t_avg)

    result = [[] for i in range(n)]

    current_actor=0
    for i in tasks:
        cur_sum = sum([j[1] for j in result[current_actor]])
        if cur_sum+i[1]<=t_opt: #i[1]<=t_opt-cur_sum
            result[current_actor].append(i)
        else: #i[1] > t_opt-cur_sum
            result[current_actor].append([i[0], t_opt-cur_sum ])
            current_actor+=1
            result[current_actor].append([i[0], i[1] - (t_opt-cur_sum) ])

    #result to float x.xx
    result = [[[i[0], round(float(i[1]),2)] for i in row] for row in result]
    #clear result
    result = [[i for i in row if i[1]!=0] for row in result if row!=[]]

    print(*result, sep='\n', end='\n\n')
    
    return result

    

if __name__ == '__main__':
    tasks=[]
    n=int(input('количество исполнителей '))
    t=int(input('количество работ '))
    for i in range(t):
        tasks.append([chr(65+i), float(input(f'{chr(65+i)}: '))])
    main(n, t, tasks)
    