def intersection(first, second):
    
    """
    Find the unique intersection.
    """
    
    second_set = set(second)
    seen = set()
    result = []
    
    for current in first:
        
        if current in second_set and current not in seen:
            
            seen.add(current)
            result.append(current)
            
            
    return result 

# Test 1: Basic intersection
print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))

# Test 2: Duplicate values
print(intersection([1, 2, 2, 2, 3], [2, 4]))

# Test 3: No common elements
print(intersection([1, 2, 3], [4, 5, 6]))

# Test 4: All elements common
print(intersection([1, 2, 3], [1, 2, 3]))

# Test 5: Duplicates in both arrays
print(intersection([4, 9, 5, 9], [9, 4, 9, 8, 4]))

# Test 6: First array empty
print(intersection([], [1, 2, 3]))

# Test 7: Second array empty
print(intersection([1, 2, 3], []))

# Test 8: Both arrays empty
print(intersection([], []))

# Test 9: Single common element
print(intersection([1], [1]))

# Test 10: Negative numbers
print(intersection([-5, -3, 0, 2], [-3, 0, 4]))
            
             
    