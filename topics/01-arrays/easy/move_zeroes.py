def move_zeroes(numbers):
    
    """
    Move zeroes to one side.
    """
    
    write = 0
    read = 0
    
    while read < len(numbers):
        
        if numbers[read] != 0:
            
            numbers[write] = numbers[read]
            write = write + 1
            
        read = read + 1
        
    for i in range(write, len(numbers)):
        numbers[i] = 0
        
    return numbers
        
print(move_zeroes([0, 1, 0, 3, 12]))
print(move_zeroes([0, 0, 1, 2, 0, 3]))
print(move_zeroes([1, 2, 3]))
print(move_zeroes([0, 0, 0]))
print(move_zeroes([]))
print(move_zeroes([1, 0, 2, 0, 3, 0]))
        
    
    