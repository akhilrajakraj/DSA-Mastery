def best_sum(numbers):
    
    """
    To find best contigious maximum sum.
    """
    
    if not numbers:
        
        return 0
    
    current_sum = numbers[0]
    max_sum = numbers[0]
    
    for i in numbers[1:]:
        
        if current_sum + i > i:
            
            current_sum = current_sum + i
        
        else:
            
            current_sum = i
            
        if current_sum > max_sum:
            
            max_sum = current_sum
            
    return max_sum

# Test 1: Standard case
print(best_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# Test 2: All positive
print(best_sum([5, 4, -1, 7, 8]))

# Test 3: All negative
print(best_sum([-3, -2, -5]))

# Test 4: Single element
print(best_sum([7]))

# Test 5: Two positive elements
print(best_sum([1, 2]))

# Test 6: Positive section surrounded by negatives
print(best_sum([-5, 4, -1, 7, -8]))

# Test 7: Maximum occurs at the beginning
print(best_sum([5, 4, -10, 2]))

# Test 8: Maximum occurs at the end
print(best_sum([-5, -2, 3, 4]))

# Test 9: Contains zeros
print(best_sum([0, -1, 0, 5, -2, 3]))

# Test 10: Mixed values
print(best_sum([2, -1, 2, 3, -9, 4, 5]))