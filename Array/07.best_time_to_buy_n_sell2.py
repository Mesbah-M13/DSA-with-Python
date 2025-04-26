'''
122. Best Time to Buy and Sell Stock II

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
'''
prices = [7,1,5,3,6,4]

profit = 0

for price in range(1,len(prices)):
    if prices[price] > prices[price-1]:
        profit += prices[price] - prices[price-1]
print(profit)