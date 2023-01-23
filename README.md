
# Задание №12
## Оптимальное расписание. Конвейерная задача.

1. В файле main.py реализовать методы *__sort_tasks* и *__sort_tasks* класса 
*Schedule*.
2. В файле main.py реализовать класс *Schedule*, предоставляющий оптимальное 
расписание для выполнения заданий.
## Примечания
- Обратить внимание, что некоторые тесты ожидают вызов определенного вида   
исключения с заданным сообщением об ошибке.  
- Разработку вести в отдельной ветке, созданной на основе данной. В названии   
ветки префикс main заменить на название команды.  
- Изменения в ветке должны быть только в файле main.py, различные   
конфигурационные файлы и кэш IDE фиксировать не нужно.
- Корректность работы класса *Schedule* проверить запустив файл 
test_schedule.py с модульными тестами.
- Все реализованные классы можно проверить запустив файл test_runner.py с 
модульными тестами.   
## Постановка конвейерной задачи:
1. Количество заданий произвольно;
2. Каждое задание состоит из двух последовательных этапов, длительность которых
произвольна;
3. Задания независимы;
4. Запрещены прерывания при выполнении заданий;
5. Количество работников строго 2;
6. Первый работник выполняет только первый этап каждого задания, второй
работник — только второй этап каждого задания;
7. Производительность работников, размеры оплаты из труда и т.д. не учитываются;
8. Требуется построить расписание выполнения всех заданий в кратчайшие сроки.
## Алгоритм Джонсона
Пусть а<sub>i</sub> и b<sub>i</sub>, — это длительности первого и второго 
этапов i-го задания. Разобьём список всех заданий на две группы. В первую 
группу попадают задания, у которых а<sub>i</sub> <= b<sub>i</sub>. Во вторую 
группу - все остальные задания. Задания из первой группы отсортируем в порядке 
возрастания величин а<sub>i</sub>. Задания из второй группы отсортируем в 
порядке убывания величин b<sub>i</sub>. Согласно алгоритму Джонсона, 
расписание получается кратчайшим, если сначала выполнить все задания из первой 
группы в отсортированном порядке, а затем — все задания из второй группы также 
в отсортированном порядке.
