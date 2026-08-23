def find_maximum(numbers):
    
    "Finding maximum from given list. "
    
    if not numbers:
        raise ValueError("The list is empty.")
    
    maximum = numbers[0]
    
    for n in numbers:
        
        if n > maximum:
            maximum = n
            
    return maximum
    
print(find_maximum([4, 6, 7, 8, 4, 3, 2, 1, 0, 9]))
print(find_maximum([-5, -2, -10, -3]))
print(find_maximum([7]))

try:
    print(find_maximum([]))
except ValueError as error:
    print(error)    
    