def count_occurrences(numbers, target):
    
    """
    To find numbers of time target occured.
    """
    
    
    count = 0
    
    for n in numbers:
        
        if n == target:
            
            count = count +1
            
    
    return count 

print(count_occurrences([2, 4, 2, 7, 2, 9, 4], 2))
print(count_occurrences([2, 4, 2, 7, 2, 9, 4], 5))
print(count_occurrences([], 2))
    