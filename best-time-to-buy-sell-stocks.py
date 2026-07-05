# Best time to buy and sell stocks : Buy stock on a day and should sell on any other day with maximum profit.

# BRUTE FORCE APPROACH : Try buying on every day.
                       # For each buying day, try selling on every later day.
                       # Calculate the profit.
                       # Keep track of the maximum profit.
# TIME COMPLEXITY : O(n²) Outer loop runs n times. Inner loop runs n times.
# SPACE COMPLEXITY : O(1) No extra data structures created.

def maximum_profit():
    prices = [7,1,5,3,6,4]
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1,len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit,profit)

    print('Maximum profit : ',max_profit)
maximum_profit()

# OPTIMISED APPROACH : Store price and min_price & profit and max_profit.
                     # Continuosly update if price < min_price.
                     # Continuosly update if profit > max_profit.
# TIME COMPLEXITY : O(n) Only one loop is used.
# SPACE COMPLEXITY : O(1) No extra data structures used.

def maximum_profit():
    prices = [7,1,5,3,6,4]
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        if (price - min_price) > max_profit:
            max_profit = (price - min_price)
    print('Maximum profit : ',max_profit)

maximum_profit()





