# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    min_until_now = float('inf')
    max_profit = 0
    for price in A:
        if price < min_until_now:
            min_until_now = price
        max_profit = max(max_profit,price-min_until_now)
        
    return max_profit
