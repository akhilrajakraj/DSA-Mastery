def max_profit(prices):
    
    """
    Best time to buy or sell stock.
    """
    
    if not prices:
        return 0
    
    minimum_profit = prices[0]
    max_profit = 0
    
    for current in prices:
        
        if current < minimum_profit:
            
            minimum_profit = current
            
        else:
            
            profit = current - minimum_profit
            
            if profit > max_profit:
                
                max_profit = profit 
        
            
    return max_profit

# Test 1: Best profit in the middle
print(max_profit([7, 1, 5, 3, 6, 4]))

# Test 2: Prices continuously decrease
print(max_profit([7, 6, 4, 3, 1]))

# Test 3: Buy at 2, sell at 4
print(max_profit([2, 4, 1]))

# Test 4: Continuously increasing
print(max_profit([1, 2, 3, 4, 5]))

# Test 5: Single day
print(max_profit([5]))

# Test 6: All prices equal
print(max_profit([3, 3, 3, 3]))

# Test 7: Best profit occurs near the end
print(max_profit([10, 1, 2, 8, 4, 9]))

# Test 8: Empty array
print(max_profit([]))

# Test 9: Two days, profitable
print(max_profit([1, 5]))

# Test 10: Two days, no profit
print(max_profit([5, 1]))

            