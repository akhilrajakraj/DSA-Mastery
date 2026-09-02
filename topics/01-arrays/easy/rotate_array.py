def rotate_array(numbers, k):
    
    """
    Rotate the array to the right by k positions.
    """
    
    if not numbers:
        
        return []
    
    n = len(numbers)
    
    k = k % n
    
    split = n - k
    
    numbers = numbers[split:] + numbers[:split]
    
    return numbers 


# Test 1: Basic rotation
print(rotate_array([1, 2, 3, 4, 5], 2))

# Test 2: Rotate by 1
print(rotate_array([1, 2, 3, 4, 5], 1))

# Test 3: Rotate by 3
print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))

# Test 4: k equals array length
print(rotate_array([1, 2, 3, 4, 5], 5))

# Test 5: k greater than array length
print(rotate_array([1, 2, 3, 4, 5], 7))

# Test 6: k much greater than array length
print(rotate_array([1, 2, 3, 4, 5], 12))

# Test 7: Single element
print(rotate_array([1], 5))

# Test 8: Empty array
print(rotate_array([], 3))

# Test 9: k is zero
print(rotate_array([1, 2, 3, 4, 5], 0))

# Test 10: Negative numbers
print(rotate_array([-1, -2, -3, -4, -5], 2))
        
        
        
    
        