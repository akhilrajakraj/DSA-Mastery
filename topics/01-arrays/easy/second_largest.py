def second_largest(numbers):
    
    largest = None
    second_largest=None
    
    for current in numbers:
        
        if largest is None:
            largest=current
            
        elif current > largest:
            second_largest=largest
            largest=current
            
        elif current < largest and (second_largest is None or second_largest < current):
            second_largest=current
            
        
    if second_largest is None:
        raise ValueError("There is no second largest.")

    return second_largest

print(second_largest([10, 5, 8, 20, 15]))
print(second_largest([20, 10, 20, 5]))
print(second_largest([-5, -10, -2, -8]))
print(second_largest([20, 15, 10, 5]))
print(second_largest([5, 10, 15, 20]))
print(second_largest([10, 15, 5, 15, 20, 3]))

try:
    print(second_largest([10]))
except ValueError as error:
    print(error)

try:
    print(second_largest([10, 10, 10, 10]))
except ValueError as error:
    print(error)

try:
    print(second_largest([]))
except ValueError as error:
    print(error)