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