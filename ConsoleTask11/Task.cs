using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleTask11
{
    public class Task
    {
        public string Name { get; set; }
        public int Duration { get; set; }
        public int StartDuration { get; set; }
        public int EndDuration { get; set; }

        public Task(string name, int duration)
        {
            this.Name = name;
            this.Duration = duration;
        }
    }
}
