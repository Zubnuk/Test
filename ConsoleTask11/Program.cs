using ConsoleTask11;
using Task = ConsoleTask11.Task;

Task task1 = new Task("a", 3);
Task task2 = new Task("b", 4);
Task task3 = new Task("c", 6);
Task task4 = new Task("d", 7);
Task task5 = new Task("e", 7);
Task task6 = new Task("f", 9);
Task task7 = new Task("g", 10);
Task task8 = new Task("h", 12);
Task task9 = new Task("i", 17);


List<Task> tasks = new List<Task>()
{
    task1, task2, task3, task4, task5, task6, task7, task8, task9
};


Schedule schedule = new Schedule(tasks, 5);
schedule.BeautyPrint();
Console.ReadLine();