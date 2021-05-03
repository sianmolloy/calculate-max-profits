from typing import List
import sys


def calculate_max_profit(prices: List[int]) -> int:
    """ Calculate Max Profit

    Args:
        prices: time series of a stock price

    Returns:
        max_profit: maximum profit possible
    """
    min_price = prices[0]
    max_profit = prices[1] - prices[0]
    for curr_price in prices[1:]:
        if curr_price - min_price > max_profit:
            max_profit = curr_price - min_price

        if curr_price < min_price:
            min_price = curr_price

    return max_profit

def calculate_max_profit_with_short_sell(prices: List[int]) -> int:
    """ Calculate Max Profit with Short Selling

    Args:
        prices: time series of a stock price

    Returns:
        max_profit: maximum profit possible with short selling
    """
    min_price = prices[0]
    max_price = prices[0]
    for curr_price in prices[1:]:
        min_price = min(min_price, curr_price)
        max_price = max(max_price, curr_price)
    
    return max_price - min_price

    
if __name__ == "__main__":
    prices = [int(x) for x in sys.argv[1].split(',')]
    print(f"Max profit: {calculate_max_profit(prices)}") 
    print(f"Max profit with short sell: {calculate_max_profit_with_short_sell(prices)}")