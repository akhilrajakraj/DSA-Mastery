def is_sorted(numbers):
    
    """
    Check if the array is sorted or not.
    """
    
    for i in range(len(numbers) - 1):
        
        if numbers[i] > numbers[i + 1]:
            
            return False
        
    return True

# Test 1
numbers = [1, 2, 3, 4, 5]
print(is_sorted(numbers))

# Test 2
numbers = [1, 3, 2, 4, 5]
print(is_sorted(numbers))

# Test 3
numbers = [1, 2, 2, 3, 4]
print(is_sorted(numbers))

# Test 4
numbers = [5, 4, 3, 2, 1]
print(is_sorted(numbers))

# Test 5
numbers = [10]
print(is_sorted(numbers))

# Test 6
numbers = []
print(is_sorted(numbers))

# Test 7
numbers = [-10, -5, -3, 0, 4]
print(is_sorted(numbers))

# Test 8
numbers = [-10, -3, -5, 0, 4]
print(is_sorted(numbers))

