using System.Linq;
using System.Threading.Tasks;

namespace Algorithm11
{
    public class Schedule
    {
        private List<Task> _tasks;
        private int _executorCount;
        private int _duration;

        public int GetExecutorsCount()
        {
            return _executorCount;
        }

        public int TaskCount()
        {
            if(_tasks == null)
            {
                return 0;
            }
            return _tasks.Count();
        }

        public int GetDuration()
        {
            return _duration;
        }

        private int CalculateDuration(List<Task> tasks, int executorCount)
        {
            int Tmax = tasks.Max(x => x.Duration);
            int Tavg = tasks.Sum(x => x.Duration) / executorCount;
            int duration = Math.Max(Tmax, (int)Math.Round((double)Tavg));
            return duration;
        }

        public Schedule(List<Task> tasks, int executorCount)
        {
            // error checking 
            if (tasks == null || tasks.Count == 0)
                throw new ArgumentException("Tasks list is empty or null");
            if (executorCount < 1)
                throw new ArgumentException("Executor count should be greater than 0");

            //Calculating Duration of the schedule
            _executorCount = executorCount;
            _tasks = tasks;
            _duration = CalculateDuration(tasks, executorCount);
        }

        public void BeautyPrint()
        {
            var elements = DistributeTasks();
            int index = 0;
            Console.WriteLine($"Total duration: {GetDuration()}");
            foreach (List<Task> tape in elements)
            {
                index++;
                Console.WriteLine(index);
                foreach (Task task in tape)
                {
                    Console.WriteLine("Task: " + task.Name + " from "+ task.StartDuration + " to " + task.EndDuration);
                }
            }
        }


        public Queue<List<Task>> DistributeTasks()
        {
            Queue<List<Task>> taskTapes = new Queue<List<Task>>();
            List<Task> remainingTasks = new List<Task>(_tasks);
            while (remainingTasks.Count > 0)
            {
                List<Task> tape = new List<Task>();
                int tapeDuration = 0;
                while (tapeDuration <= _duration && remainingTasks.Count > 0)
                {
                    Task task = remainingTasks[0];
                    if (tapeDuration == this._duration)
                    {
                        break;
                    }
                    if (tapeDuration + task.Duration <= _duration)
                    {
                        task.StartDuration = tapeDuration;
                        task.EndDuration = tapeDuration + task.Duration;
                        tape.Add(task);
                        tapeDuration += task.Duration;
                        remainingTasks.RemoveAt(0);
                    }
                    else
                    {
                        int remainingDuration = task.Duration - (_duration - tapeDuration);
                        Task newTask = new Task(task.Name, remainingDuration);
                        task.Duration = _duration - tapeDuration;
                        task.StartDuration = tapeDuration;
                        task.EndDuration = tapeDuration + task.Duration;
                        tape.Add(task);
                        remainingTasks.RemoveAt(0);
                        remainingTasks.Insert(0, newTask);
                        break;
                    }
                }
                taskTapes.Enqueue(tape);
            }
            return taskTapes;
        }
    }
}

        //public List<List<Task>> DistributeTasks()
        //{
        //    // Create a list to hold the "tapes" of tasks
        //    List<List<Task>> taskTapes = new List<List<Task>>();

        //    foreach (Task task in tasks)
        //    {
        //        bool added = false;
        //        for (int i = 0; i < taskTapes.Count; i++)
        //        {
        //            if (taskTapes[i].Sum(x => x.Duration) == duration)
        //            {
        //                continue;
        //            }

        //            List<Task> tape = taskTapes[i];
        //            int tapeDuration = tape.Sum(x => x.Duration);
        //            if (tapeDuration + task.Duration <= duration)
        //            {
        //                tape.Add(task);
        //                added = true;
        //                break;
        //            }
        //            else if (tapeDuration + task.Duration > duration)
        //            {
        //                int remainingDuration = task.Duration - (duration - tapeDuration);
        //                Task newTask = new Task(task.Name, remainingDuration);
        //                task.Duration = duration - tapeDuration;
        //                tape.Add(task);
        //                taskTapes.Add(new List<Task> { newTask });
        //                added = true;
        //                break;
        //            }
        //        }
        //        if (!added)
        //        {
        //            List<Task> newTape = new List<Task> { task };
        //            taskTapes.Add(newTape);
        //        }
        //    }
        //    return taskTapes;
        //}

/*
foreach (Task task in tasks)
{
    bool added = false;
    for (int i = 0; i < taskTapes.Count; i++)
    {
        List<Task> tape = taskTapes[i];
        int tapeDuration = tape.Sum(x => x.Duration);
        if (tapeDuration + task.Duration <= duration)
        {
            tape.Add(task);
            added = true;
            break;
        }
        else if (tapeDuration + task.Duration > duration)
        {
            int remainingDuration = duration - tapeDuration;
            Task newTask = new Task("Z", task.Duration - remainingDuration);
            task.Duration = remainingDuration;
            tape.Add(task);
            taskTapes.Add(new List<Task> { newTask });
            added = true;
            break;
        }
    }
    if (!added)
    {
        List<Task> newTape = new List<Task> { task };
        taskTapes.Add(newTape);
    }
}
*/

// Iterate through the tasks and add them to the appropriate "tape"
/*
foreach (Task task in tasks)
{
    bool added = false;
    for (int i = 0; i < taskTapes.Count; i++)
    {
        List<Task> tape = taskTapes[i];
        int tapeDuration = tape.Sum(x => x.Duration);
        if (tapeDuration + task.Duration <= duration)
        {
            tape.Add(task);
            added = true;
            break;
        }
    }
    if (!added)
    {
        List<Task> newTape = new List<Task> { task };
        taskTapes.Add(newTape);
    }
}

// Assign the tapes to the performers
int performerIndex = 0;
foreach (List<Task> tape in taskTapes)
{
    foreach (Task task in tape)
    {
        //task.Performer = performerIndex;
    }
    performerIndex++;
    if (performerIndex >= executorCount)
    {
        performerIndex = 0;
    }
}
*/


/*
class Schedule
{
    private List<Task> tasks;
    private int executorCount;
    private List<List<Dictionary<Task, int>>> executorTasks;
    private int duration;

    public Schedule(List<Task> tasks, int executorCount)
    {
        string errorMsg = GetParamError(tasks);
        if (errorMsg != null)
        {
            throw new ScheduleArgumentException(errorMsg);
        }
        this.executorCount = executorCount;
        this.tasks = tasks;
        this.executorTasks = new List<List<Dictionary<Task, int>>>();
        for (int i = 0; i < executorCount; i++)
        {
            this.executorTasks.Add(new List<Dictionary<Task, int>>());
        }

        //Calculating Duration of the schedule
        int Tmax = TaskDurations.Max();
        int Tavg = TaskDurations.Sum() / executorCount;
        this.duration = Math.Max(Tmax, (int)Math.Round((double)Tavg));

        DistributeTasks();
    }

    // rest of the class

    private List<List<Dictionary<Task, int>>> DistributeTasks()
    {
        int sum = 0;
        int counter = 1;
        int startTime = 0;
        for (int i = 0; i < tasks.Count; i++)
        {
            if (tasks[i].Duration + sum < duration)
            {
                executorTasks[counter % executorCount].Add(new Dictionary<Task, int>() { { tasks[i], startTime } });
                sum += tasks[i].Duration;
                startTime += tasks[i].Duration;
                counter++;
            }
            else
            {
                int remainingTime = duration - sum;
                sum = tasks[i].Duration - remainingTime;
                startTime = remainingTime;
                executorTasks[counter % executorCount].Add(new Dictionary<Task, int>() { { tasks[i], startTime } });
                counter++;
            }
        }
        return executorTasks;
    }
}
*/
