import math
stock = [7,1,5,3,6,4]
min_price=math.inf
max_profit=0
for i in stock:
    if i<min_price:
        min_price=i
    if max_profit< i-min_price:
        max_profit= i-min_price
print(max_profit)
