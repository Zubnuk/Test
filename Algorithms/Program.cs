using System.Runtime.CompilerServices;

namespace Algorithms
{
    /// <summary>
    /// Class <c>MinCostPath</c> a class with path data in the some table.
    /// </summary>
    public class MinCostPath
    {
        private readonly double _cost;
        private readonly int[,] _path;
        public double Cost { get => _cost; }
        public int[,] Path { get => _path; }

        /// <summary>This constructor initializes the new MinCostPath to
        /// (<paramref name="cost"/>,<paramref name="path"/>).
        /// </summary>
        /// <param name="cost">the new Point's x-coordinate.</param>
        /// <param name="path">the new Point's y-coordinate.</param>
        public MinCostPath(double cost, int[,] path)
        {
            _cost = cost;
            _path = path;
        }

        public override string ToString()
        {
            return $"cost: {Cost.ToString()}\n" + PathToString();
        }

        private string PathToString()
        {
            string[] cells = new string [Path.GetLength(0)];
            for (var i = 0; i < Path.GetLength(0); i++)
            {
                cells[i] = $"({Path[i, 0].ToString()}, {Path[i, 1].ToString()})";
            }
            return "path: " + String.Join(", ", cells);
        }
    }
    public static class Program
    {
        /// <summary>
        /// Searches for the minimum cost path in the table. Each cell in the table has some price per visit.
        /// </summary>
        /// <param name="priceTable">A matrix with float cell price values.</param>
        /// <exception cref="ArgumentException">When the table is empty.</exception>
        /// <returns>A MinCostPath object with the cost value and the path.</returns>
        public static MinCostPath GetMinCostPath(double[,] priceTable)
        {
            throw new NotImplementedException();
        }

        public static void Main(string[] args)
        {
            double[,] priceTable = new double[3, 3]
            {
                {1.0, 2.0, 2.0},
                {3.0, 4.0, 2.0},
                {1.0, 1.0, 2.0}
            };
            Console.WriteLine(GetMinCostPath(priceTable));
        }
    }
}