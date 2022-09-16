namespace Algorithms
{
    public static class Program
    {
        /// <summary>
        /// Generates all permutations by a set of chars
        /// </summary>
        /// <param name="items">A set of chars</param>
        /// <exception cref="ArgumentException">Thrown when the chars in items have duplicates</exception>
        /// <returns>An array of permutation strings</returns>
        public static string[] GeneratePermutations(char[] items)
        {
            throw new NotImplementedException();
        }

        public static void Main(string[] args)
        {
            string[] permutations = GeneratePermutations(new char[4] {'a', 'b', 'c', 'd'});
            foreach (var pmt in permutations)
            {
                Console.WriteLine(pmt);
            }
        }
    }
}