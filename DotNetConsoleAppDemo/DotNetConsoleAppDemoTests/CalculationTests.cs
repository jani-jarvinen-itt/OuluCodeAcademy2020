using Microsoft.VisualStudio.TestTools.UnitTesting;
using DotNetConsoleAppDemo;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DotNetConsoleAppDemo.Tests
{
    [TestClass()]
    public class CalculationTests
    {
        [TestMethod()]
        public void SumTest()
        {
            int a = 100;
            int b = 200;

            Calculation calc = new Calculation();
            int sum = calc.Sum(a, b);

            int expect = a + b;
            Assert.AreEqual(expect, sum);
        }

        [TestMethod()]
        public void MultiplyTest()
        {
            int a = 5;
            int b = 10;

            Calculation calc = new Calculation();
            int result = calc.Multiply(a, b);

            int expect = a * b;
            Assert.AreEqual(expect, result);
        }
    }
}