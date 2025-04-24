''' LeetCode 121: Best Time to Buy and Sell Stock  
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
 '''

prices = [7,1,5,3,6,4]

'''
min_price = float('inf')
max_profit = 0        
        
for price in prices:
    profit = price - min_price
            
    min_price = min(price, min_price)
    max_profit = max(profit, max_profit)
                
print(max_profit)

'''
# Time: O(n)
# Space: O(1)

# min_price = float('inf')
# max_profit = 0        
        
# for price in prices:
#     if price < min_price:
#         min_price = price
            
#     profit = price - min_price
        
#     if profit > max_profit:
#         max_profit = profit

# print(max_profit)

prices = [7,1,5,3,6,4]

min_profit = float('inf')
max_profit = 0

for price in prices:
    if price < min_profit:
        min_profit = price

    profit = price - min_profit

    if profit > max_profit:
        max_profit = profit
print(max_profit)

