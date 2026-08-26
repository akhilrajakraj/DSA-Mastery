def remove_duplicates(numbers):
    
    """
    Remove duplicates in an array.
    """
    
    if not numbers:
        return 0
    
    write = 0
    read = 1
    
    while read < len(numbers):
        
        if numbers[write] == numbers[read]:
            
            read = read + 1
            
        elif numbers[write] != numbers[read]:
            
            write = write + 1
            numbers[write] = numbers [read]
            
    return write+1

print(remove_duplicates([1, 1, 2, 2, 3, 3, 4]))
print(remove_duplicates([1, 1, 1, 1]))
print(remove_duplicates([1, 2, 3, 4, 5]))
print(remove_duplicates([1]))
print(remove_duplicates([]))
print(remove_duplicates([0, 0, 1, 1, 2, 2, 3]))

numbers = [1, 1, 2, 2, 3, 3, 4]

k = remove_duplicates(numbers)

print("k =", k)
print("array =", numbers)
print("unique portion =", numbers[:k])