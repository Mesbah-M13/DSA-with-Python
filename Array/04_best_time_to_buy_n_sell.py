prices = [7,1,5,3,6,4]

min_price = float('inf')
max_profit = 0        
        
for price in prices:
    profit = price - min_price
            
    min_price = min(price, min_price)
    max_profit = max(profit, max_profit)
                
print(max_profit)