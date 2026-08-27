def merge_sorted_arrays(first, second):
    
    """
    Merge two sorted arrays.
    """
    
    i = 0
    j = 0
    result = []

    while i < len(first) and j < len(second):
        
        if first[i] <= second[j]:
            
            result.append(first[i])
            i = i + 1
            
        elif first[i] >= second[j]:
            
            result.append(second[j])
            j = j + 1
            
    while i < len(first):
        result.append(first[i])
        i += 1

    while j < len(second):
        result.append(second[j])
        j += 1

    return result

print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))
print(merge_sorted_arrays([1, 2, 7], [3, 4, 5, 8]))
print(merge_sorted_arrays([], [1, 2, 3]))
print(merge_sorted_arrays([1, 2, 3], []))
print(merge_sorted_arrays([], []))
print(merge_sorted_arrays([1, 1, 3], [1, 2, 3]))
print(merge_sorted_arrays([-5, -2, 4], [-3, 0, 6]))
    