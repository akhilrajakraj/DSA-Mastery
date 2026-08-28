def find_missing_number(numbers):
    
    """
    Find the missing number from the range.
    """
    sum = 0
    n=len(numbers)
    
    expected_sum = n*(n+1) // 2
    
    for i in numbers:
        
        sum = i + sum
        
    diff = expected_sum - sum
    
    return diff

print(find_missing_number([3, 0, 1]))
print(find_missing_number([0, 1]))
print(find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(find_missing_number([0]))
print(find_missing_number([1]))
print(find_missing_number([]))
        
    
    