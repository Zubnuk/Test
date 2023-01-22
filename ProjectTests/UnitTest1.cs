using Algorithm11;
using Task = Algorithm11.Task;

namespace ProjectTests
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void AllTasksInTape()
        {
            // Arrange
            List<Task> tasks = new List<Task>
            {
                new Task("Task 1", 2),
                new Task("Task 2", 3),
                new Task("Task 3", 2),
                new Task("Task 4", 4)
            };
            int executorCount = 2;
            Schedule schedule = new Schedule(tasks, executorCount);

            // Act
            var taskTapes = schedule.DistributeTasks();

            // Assert
            int Tmax = tasks.Max(x => x.Duration);
            int Tavg = tasks.Sum(x => x.Duration) / executorCount;
            int Topt = Math.Max(Tmax, (int)Math.Round((double)Tavg));

            Assert.AreEqual(Topt, schedule.GetDuration());
            Assert.IsTrue(taskTapes.All(x => x.Sum(y => y.Duration) <= schedule.GetDuration()));
        }

        [TestMethod]
        public void ReturnsExpectedTaskTapes()
        {
            // Arrange
            List<Task> tasks = new List<Task>
            {
                new Task("Task 1", 2),
                new Task("Task 2", 3),
                new Task("Task 3", 2),
                new Task("Task 4", 4)
            };
            int executorCount = 2;
            Schedule schedule = new Schedule(tasks, executorCount);

            int Tmax = tasks.Max(x => x.Duration);
            int Tavg = tasks.Sum(x => x.Duration) / executorCount;
            int Topt = Math.Max(Tmax, (int)Math.Round((double)Tavg));

            var taskTapes = schedule.DistributeTasks();

            //Assert
            var allTasks = tasks.Select(x => x.Name);
            var tasksInTapes = taskTapes.SelectMany(x => x.Select(y => y.Name));
            Assert.AreEqual(Topt, schedule.GetDuration());
            Assert.IsTrue(tasksInTapes.All(x => allTasks.Contains(x)));
        }

        [TestMethod]
        public void NullTasksThrowsArgumentException()
        {
            //Arrange
            List<Task> tasks = null;
            List<Task> tasks1 = new List<Task>();
            int executorCount = 2;

            //Assert
            Assert.ThrowsException<ArgumentException>(() => new Schedule(tasks, executorCount));
            Assert.ThrowsException<ArgumentException>(() => new Schedule(tasks1, executorCount));
        }

        [TestMethod]
        public void ZeroExecutorCountThrowsArgumentException()
        {
            // Arrange
            List<Task> tasks = new List<Task>
            {
                new Task("Task 1", 2),
                new Task("Task 2", 3),
                new Task("Task 3", 2),
                new Task("Task 4", 4)
            };
            int executorCount = 0;

            //Assert
            Assert.ThrowsException<ArgumentException>(() => new Schedule(tasks, executorCount));
        }
    }
}