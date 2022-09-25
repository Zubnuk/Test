using Algorithms;

namespace Tests;

public class TablePathTest
{
    [Fact]
    public void TestDuplicate()
    {
        Assert.Throws<ArgumentException>(() => Program.GetMinCostPath(new double[1,0]));
    }

    [Fact]
    public void TestSingle()
    {
        double[,] priceTable = new double[1, 1] {{ 1.0 }};
        double expCost = 1.0;
        int[,] expPath = new int[1, 2] {{0, 0}};
        MinCostPath result = Program.GetMinCostPath(priceTable);
        Assert.Equal(expCost, result.Cost);
        Assert.True(ArraysAreEqual(expPath, result.Path));
    }

    [Fact]
    public void TestDouble()
    {
        double[,] priceTable = new double[2, 2] {{ 1.0, 2.0 }, {3.0, 4.0}};
        double expCost = 7.0;
        int[,] expPath = new int[3, 2] {{0, 0}, {0, 1}, {1, 1}};
        MinCostPath result = Program.GetMinCostPath(priceTable);
        Assert.Equal(expCost, result.Cost);
        Assert.True(ArraysAreEqual(expPath, result.Path));
    }

    [Fact]
    public void TestTriple()
    {
        double[,] priceTable = new double[3, 3] {{ 1.0, 2.0, 2.0 }, {3.0, 4.0, 2.0}, {1.0, 1.0, 2.0}};
        double expCost = 8.0;
        int[,] expPath = new int[5, 2] {{0, 0}, {1, 0}, {2, 0}, {2, 1}, {2, 2}};
        MinCostPath result = Program.GetMinCostPath(priceTable);
        Assert.Equal(expCost, result.Cost);
        Assert.True(ArraysAreEqual(expPath, result.Path));
    }

    [Fact]
    public void TestRectangle()
    {
        double[,] priceTable = new double[2, 3] {{ 1.0, 2.0, 2.0 }, {3.0, 4.0, 1.0}};
        double expCost = 6.0;
        int[,] expPath = new int[4, 2] {{0, 0}, {0, 1}, {0, 2}, {1, 2}};
        MinCostPath result = Program.GetMinCostPath(priceTable);
        Assert.Equal(expCost, result.Cost);
        Assert.True(ArraysAreEqual(expPath, result.Path));
    }

    [Fact]
    public void TestSquare()
    {
        double[,] priceTable = new double[6, 6]
        {
            {1.0, 2.0, 2.0, 1.0, 3.0, 4.0},
            {3.0, 1.0, 1.0, 5.0, 7.0, 6.0},
            {3.0, 4.0, 1.0, 2.0, 7.0, 6.0},
            {5.0, 7.0, 1.0, 6.0, 4.0, 4.0},
            {5.0, 9.0, 2.0, 3.0, 5.0, 8.0},
            {2.0, 2.0, 1.0, 3.0, 1.0, 6.0}
        };
        double expCost = 20.0;
        int[,] expPath = new int[11, 2]
        {
            {0, 0}, {0, 1}, {1, 1}, {1, 2}, {2, 2}, {3, 2}, {4, 2}, {5, 2}, {5, 3}, {5, 4}, {5, 5}
        };
        MinCostPath result = Program.GetMinCostPath(priceTable);
        Assert.Equal(expCost, result.Cost);
        Assert.True(ArraysAreEqual(expPath, result.Path));
    }

    [Fact]
    public void TestRectangleLarge()
    {
        double[,] priceTable = new double[12, 6]
        {
            {8.0, 9.0, 2.0, 1.0, 6.0, 9.0},
            {2.0, 3.0, 4.0, 8.0, 5.0, 1.0},
            {4.0, 1.0, 7.0, 7.0, 1.0, 7.0},
            {5.0, 6.0, 2.0, 8.0, 5.0, 6.0},
            {3.0, 5.0, 2.0, 5.0, 8.0, 3.0},
            {6.0, 9.0, 1.0, 3.0, 1.0, 5.0},
            {7.0, 5.0, 4.0, 4.0, 2.0, 9.0},
            {8.0, 7.0, 4.0, 1.0, 3.0, 5.0},
            {6.0, 5.0, 7.0, 7.0, 6.0, 2.0},
            {6.0, 2.0, 4.0, 8.0, 6.0, 3.0},
            {7.0, 7.0, 2.0, 4.0, 5.0, 7.0},
            {3.0, 8.0, 1.0, 6.0, 7.0, 1.0}
        };
        double expCost = 52.0;
        int[,] expPath = new int[17, 2]
        {
            {0, 0}, {1, 0}, {1, 1}, {2, 1}, {3, 1}, {3, 2}, {4, 2}, {5, 2}, {5, 3},
            {5, 4}, {6, 4}, {7, 4}, {7, 5}, {8, 5}, {9, 5}, {10, 5}, {11, 5}
        };
        MinCostPath result = Program.GetMinCostPath(priceTable);
        Assert.Equal(expCost, result.Cost);
        Assert.True(ArraysAreEqual(expPath, result.Path));
    }

    private static bool ArraysAreEqual(int[,] source, int[,] target)
    {
        if (source.GetLength(0) != target.GetLength(0) ||
            source.GetLength(1) != target.GetLength(1))
        {
            return false;
        }
        for (var i = 0; i < source.GetLength(0); i++)
        {
            for (var j = 0; j < source.GetLength(1); j++)
            {
                if (source[i, j] != target[i, j]) return false;
            }
        }
        return true;
    }
}