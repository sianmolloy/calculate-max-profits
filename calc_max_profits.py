from typing import List
import sys


def calculate_max_profit(prices: List[int]) -> int:
    """ Calculate Max Profit

    Args:
        prices: time series of a stock price

    Returns:
        max_profit: maximum profit possible
    """
    raise NotImplementedError()

def calculate_max_profit_with_short_sell(prices: List[int]) -> int:
    """ Calculate Max Profit with Short Selling

    Args:
        prices: time series of a stock price

    Returns:
        max_profit: maximum profit possible with short selling
    """
    raise NotImplementedError()

    
if __name__ == "__main__":
    print(calculate_max_profit(sys.argv))