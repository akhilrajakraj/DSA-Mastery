def reverse_array(numbers):
    
    
    
    left = 0
    right = len(numbers)-1
    
    while left < right:
        
        numbers[left], numbers[right] = numbers[right], numbers[left]
        
        left = left+1
        right= right-1
        
    return numbers

# Test 1: Odd number of elements
numbers = [1, 2, 3, 4, 5]
print(reverse_array(numbers))

numbers = [10, 20, 30, 40, 50, 60]
print(reverse_array(numbers))

numbers = [10]
print(reverse_array(numbers))

numbers = []
print(reverse_array(numbers))

numbers = [-5, -10, -2, -8]
print(reverse_array(numbers))

numbers = [1, 2, 3, 4, 5]

reverse_array(numbers)

print(numbers)