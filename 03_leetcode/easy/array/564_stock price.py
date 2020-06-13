# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

def max_profit(prices: list) -> int:
    profit = 0
    for i in range(0, len(prices)-1):
        profit += max(0, prices[i+1] - prices[i])
    return profit

max_profit([7,6,4,3,1])