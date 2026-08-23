def find_minimum(numbers):
    
    """Finding minimum number from a given list."""
    
    if not numbers:
        
        raise ValueError("This list is empty.")
    
    minimum = numbers[0]
    
    for n in numbers:
        
        if n < minimum:
            
            minimum = n
            
    return minimum

numbers = [7, 3, 9, 2, 8, 1, 5]

print(find_minimum(numbers))
print(find_minimum([-5, -2, -10, -3]))
print(find_minimum([7]))

try:
    print(find_minimum([]))
except ValueError as error:
    print(error)
            
            