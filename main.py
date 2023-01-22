import matplotlib.pyplot as plt
import random as rnd
from colorama import Fore, Style
from custom_exception import ArgumentException


# проверка ввода длины
def input_length(message):
    flag = True
    while (flag):
        print(message)
        a = input()
        if a.isnumeric() and int(a) > 0:
            flag = False
        else:
            print(Fore.RED + "Введите положительное целое число")
            print(Style.RESET_ALL)
    return int(a)




def check_float(message):
    flag = True
    while (flag):
        print(message, end=": ")
        a = input()
        if is_float(a) and float(a) > 0:
            flag = False
        else:
            print(Fore.RED + "Введите положительное число")
            print(Style.RESET_ALL)
    return float(a)


def is_float(element: any) -> bool:
    if element is None:
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False

    # Выдает чередующийся список цветов заданной длины по буквам


def generate_color(name):
    sum = 0
    p = 1
    for letter in name:
        sum += ord(letter) * p
        p *= 99
    rnd.seed(sum)
    r = rnd.random()

    sum *= r
    rnd.seed(sum)
    g = rnd.random()

    sum *= g
    rnd.seed(sum)
    b = rnd.random()

    color = (r, g, b)
    return color


# Автоматически создает имена задачам: A,B...Z,AA,AB...
def create_name(count):
    name = ""
    while (count > 0):
        if (count == 26):
            name = name + 'Z'
            count = 0
        else:
            name = name + chr(count % 26 + 64)
        count = count // 26
    return name[::-1]


# Создание расписания, возвращает двум. массив
def create_timetable(n, works_length):
    if type(n) is not int or n <= 0:
        raise ArgumentException('The number of employees must be an integer more than zero')
    else:
        for i in works_length:
            if (type(i) is not float and type(i) is not int) or i <= 0:
                raise ArgumentException('The length of work must be a number more than 0')
        work_names = []
        for i in range(1, len(works_length) + 1):
            work_names.append(create_name(i))
        max_time = max(sum(works_length) / n, max(works_length))
        current_time = 0
        i = 0
        row_id = 0
        accuracy = 0.0001  # точность (для работы с дробными числами)
        result = []
        # Пока не выполним все работы:
        while works_length[-1] != 0:
            left_time = max_time - current_time
            # Если текущая задача занимает больше времени, чем осталось у исполнителя, то
            # Всё оставшееся время тек. исполнителя будет занято задачей
            # Считаем остаток задачи и идем к след. исполнителю
            if works_length[i] - (left_time) > accuracy:
                result.append([row_id + 1, work_names[i], round(current_time, 4), round(current_time + left_time, 4)])

                row_id += 1
                works_length[i] -= left_time
                current_time = 0
            # Если текущая задача занимает меньше времени, чем осталось у исполнителя, то
            # Вся задача будет сделана тек. исполнителем
            elif works_length[i] - (left_time) < (-1) * accuracy:
                result.append([row_id + 1, work_names[i], round(current_time, 4), round(current_time + works_length[i], 4)])

                current_time += works_length[i]
                works_length[i] = 0
                i += 1
            # Если текущая задача занимает ровно столько времени, сколько осталось у исполнителя, то
            # Вся задача будет сделана тек. исполнителем, сразу же переходим к следующему исполнителю
            else:
                result.append([row_id + 1, work_names[i], round(current_time, 4), round(current_time + left_time, 4)])

                row_id += 1
                works_length[i] = 0
                current_time = 0
                i += 1
        # заполняет пробелы, когда исполнитель не работает
        return result


# Отображение расписания
def show_timetable(n, timetable, max_time):
    plt.rcParams['toolbar'] = 'None'
    fig, ax = plt.subplots()
    used_names = []
    # Генерируется строка каждого исполнителя
    for i in range(len(timetable)):
        # Чтобы имена задач не дублировались на легенде
        if timetable[i][1] in used_names:
            lbl = "_" + timetable[i][1]
        else:
            lbl = timetable[i][1]
            used_names.append(timetable[i][1])

        ax.broken_barh([(timetable[i][2], timetable[i][3])], (n - timetable[i][0] + 0.6, 0.8),
                       facecolors=generate_color(timetable[i][1]), label=lbl)

    ax.set_ylim(0, n + 1)
    ax.set_xlim(0, max_time)
    ax.set_xlabel('Время')

    ax.set_yticks(list(range(1, n + 1)))
    ax.set_yticklabels(list(range(n, 0, -1)))
    ax.grid(True)
    fig.legend()
    plt.show()


def main():
    # ВВОД
    n = input_length("Введите количество исполнителей")
    m = input_length("Введите количество задач")

    works_length = []
    work_names = []

    print("Введите длительности работ")
    for i in range(1, m + 1):
        # work_names.append(create_name(i))
        #print(create_name(i), end=": ")
        works_length.append(check_float(create_name(i)))

    max_time = max(sum(works_length) / n, max(works_length))
    timetable = create_timetable(n, works_length)
    print(timetable)

    show_timetable(n, timetable, max_time)


if __name__ == '__main__':
    main()
