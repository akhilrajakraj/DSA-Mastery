def majority_element(numbers):
    
    """
    Find the majority element.
    """
    
    counts = {}
    
    for number in numbers:
        
        if number in counts:
            
            counts[number] = counts[number] + 1
            
        else:
    
            counts[number] = 1
            
    for number, count in counts.items():
        
        if count > len(numbers) / 2:
            
            return number
            
    return count
    
print(majority_element([3, 2, 3]))
    
# Test 1: Majority appears twice
print(majority_element([3, 2, 3]))

# Test 2: Majority appears four times
print(majority_element([2, 2, 1, 1, 1, 2, 2]))

# Test 3: Majority appears three times
print(majority_element([5, 5, 5, 2, 2]))

# Test 4: Single element
print(majority_element([1]))

# Test 5: Majority appears four times
print(majority_element([4, 4, 2, 4, 3, 4, 4]))

# Test 6: Negative numbers
print(majority_element([-1, -1, -1, 2, 3]))

# Test 7: Majority at the end
print(majority_element([1, 2, 2, 2, 2]))

# Test 8: Larger array
print(majority_element([7, 7, 3, 3, 7, 2, 7, 7, 4]))