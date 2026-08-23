def linear_search(numbers, target):
    
    """Linear Search. """
    
    for i, n in enumerate(numbers):
        
        if n == target:
            
            return i
        
    return -1

print(linear_search([4, 8, 1, 9, 3, 7], 9))
print(linear_search([4, 8, 1, 9, 3, 7], 10))
    