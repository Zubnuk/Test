using Algorithms;

namespace Tests;

public class PermutationsTest
{
    [Fact]
    public void TestEmpty()
    {
        Assert.Empty(Program.GeneratePermutations(new char[0]));
    }

    [Fact]
    public void TestDuplicate()
    {
        Assert.Throws<ArgumentException>(() => Program.GeneratePermutations(new char[3] {'a', 'b', 'b'}));
    }

    [Fact]
    public void TestSingle()
    {
        string[] expected = new string[1] {"a"};
        string[] actual = Program.GeneratePermutations(new char[1] {'a'});
        Assert.True(ArraysAreEqual(expected, actual));
    }

    [Fact]
    public void TestDouble()
    {
        string[] expected = new string[2] {"ab", "ba"};
        string[] actual = Program.GeneratePermutations(new char[2] {'a', 'b'});
        Assert.True(ArraysAreEqual(expected, actual));
    }

    [Fact]
    public void TestTriple()
    {
        string[] expected = new string[6] {"abc", "acb", "bac", "bca", "cab", "cba"};
        string[] actual = Program.GeneratePermutations(new char[3] {'a', 'b', 'c'});
        Assert.True(ArraysAreEqual(expected, actual));
    }

    [Fact]
    public void TestQuadruple()
    {
        string[] expected = new string[24]
        {
            "abcd", "dbca", "adcb", "abdc", "cbad", "dbac", "cdab", "cbda", "acbd", "dcba", "adbc", "acdb",
            "bacd", "dacb", "bdca", "badc", "cabd", "dabc", "cdba", "cadb", "bcad", "dcab", "bdac", "bcda"
        };
        string[] actual = Program.GeneratePermutations(new char[4] {'a', 'b', 'c', 'd'});
        Assert.True(ArraysAreEqual(expected, actual));
    }

    private static bool ArraysAreEqual(string[] source, string[] target)
    {
        if (source.Length != target.Length) return false;
        foreach (var srcItem in source)
        {
            bool find = false;
            foreach (var trgItem in target)
            {
                if (srcItem == trgItem) find = true;
            }
            if (!find) return false;
        }
        return true;
    }
}