def two_sum(numbers, target):
    
    """
    Find two numbers get targets.
    """
    
    i = 0
    j = i + 1
    
    for i in range(len(numbers)):
        
        for j in range(i + 1, len(numbers)):
            
            if numbers[i] + numbers[j] == target:
                
                return [i,j]
            
    return [1,-1]
        

    
            
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
print(two_sum([1, 2, 3], 10))
    