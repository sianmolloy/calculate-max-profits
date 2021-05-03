import unittest
from calc_max_profits import calculate_max_profit, calculate_max_profit_with_short_sell

class TestCalcMaxProfits(unittest.TestCase):
    """
    Test Calc Max Profits
    """

    def test_calc_max_profit(self):
        self.assertEqual(calculate_max_profit([7, 5, 6, 10, 7, 4, 5, 8]), 5)
        self.assertEqual(calculate_max_profit([12, 9, 8, 224, 72, 1006, 78]), 998)
        self.assertEqual(calculate_max_profit([10087, 2004, 756]), -1248)
        #decending prices
        self.assertEqual(calculate_max_profit([10, 8, 5, 4, 3, 1]), -1)
        #ascending prices
        self.assertEqual(calculate_max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 9)        
        #uniform prices
        self.assertEqual(calculate_max_profit([7, 7, 7, 7, 7]), 0)
        #min number of prices
        self.assertEqual(calculate_max_profit([100, 9]), -91)
        self.assertEqual(calculate_max_profit([1, 895]), 894)

    def test_calc_max_profit_with_short_sell(self):
        self.assertEqual(calculate_max_profit_with_short_sell([4, 7, 5, 9, 6, 2]), 7)
        self.assertEqual(calculate_max_profit_with_short_sell([2, 6, 3, 8, 5, 3]), 6)


if __name__ == '__main__':
    unittest.main()