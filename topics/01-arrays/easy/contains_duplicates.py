def contains_duplicate(numbers):
    
    """
    Check if there is any duplicates occurs.
    """
    
    if not numbers:
        
        return False
    
    seen = set()
    
    for i in numbers:
        
        if i in seen:
            
            return True
        
        seen.add(i)
        
    return False

# Test 1: Duplicate at the end
print(contains_duplicate([1, 2, 3, 1]))

# Test 2: No duplicates
print(contains_duplicate([1, 2, 3, 4]))

# Test 3: Duplicate appears consecutively
print(contains_duplicate([1, 2, 2, 3]))

# Test 4: All elements are duplicates
print(contains_duplicate([5, 5, 5, 5]))

# Test 5: Single element
print(contains_duplicate([7]))

# Test 6: Empty array
print(contains_duplicate([]))

# Test 7: Negative numbers with duplicate
print(contains_duplicate([-1, -2, -3, -1]))

# Test 8: Duplicate at the beginning
print(contains_duplicate([4, 4, 2, 7, 9]))

# Test 9: Larger array with no duplicates
print(contains_duplicate([1, 3, 5, 7, 9, 11, 13, 15]))

# Test 10: Zero as a duplicate
print(contains_duplicate([0, 1, 2, 0, 4]))
    