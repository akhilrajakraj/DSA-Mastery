# Linear Search

## Problem

Given an array of numbers and a target value, find whether the target exists in the array. If it exists, return its index. If it does not exist, return `-1`.

### Example 1

Input:

```python
numbers = [4, 8, 1, 9, 3, 7]
target = 9
```

Output:

```text
3
```

### Example 2

Input:

```python
numbers = [4, 8, 1, 9, 3, 7]
target = 10
```

Output:

```text
-1
```

---

## My Approach

I traverse the array from the beginning and compare each element with the target.

Because the problem asks for the index, I keep track of both the index and the current value using `enumerate()`.

If the current value matches the target, I immediately return its index.

If I finish traversing the entire array without finding the target, I return `-1` to indicate that it does not exist in the array.

---

## Algorithm

1. Traverse the array from the first element.
2. Keep track of the current index and value.
3. Compare the current value with the target.
4. If they are equal, return the current index.
5. Continue until the array ends.
6. If the target was not found, return `-1`.

---

## Implementation

The implementation is available in `linear_search.py`.

Core logic:

```python
for i, n in enumerate(numbers):
    if n == target:
        return i

return -1
```

---

## Dry Run

For:

```text
numbers = [4, 8, 1, 9, 3, 7]
target = 9
```

The search proceeds as:

```text
i = 0, n = 4  → 4 == 9? No
i = 1, n = 8  → 8 == 9? No
i = 2, n = 1  → 1 == 9? No
i = 3, n = 9  → 9 == 9? Yes
```

Therefore:

```text
return 3
```

For target `10`:

```text
4 → not found
8 → not found
1 → not found
9 → not found
3 → not found
7 → not found
```

The loop finishes, so:

```text
return -1
```

---

## Edge Cases

### 1. Target is the first element

```python
linear_search([9, 4, 8, 1], 9)
```

Output:

```text
0
```

This is the best case.

### 2. Target is the last element

```python
linear_search([4, 8, 1, 3, 9], 9)
```

Output:

```text
4
```

### 3. Target does not exist

```python
linear_search([4, 8, 1, 3], 9)
```

Output:

```text
-1
```

### 4. Empty list

```python
linear_search([], 5)
```

Output:

```text
-1
```

No exception is required because an empty array simply means the target was not found.

---

## Complexity Analysis

### Best Case

```text
O(1)
```

The target is the first element, so the algorithm returns immediately.

### Average Case

```text
O(n)
```

The target may be somewhere in the middle, so a linear number of elements may need to be checked.

### Worst Case

```text
O(n)
```

The target is the last element or does not exist, so the entire array may need to be traversed.

### Space Complexity

```text
O(1)
```

Only a constant amount of extra space is used for the loop variables and target reference.

---

## What I Learned

- I learned how to implement linear search without using a built-in search function.
- I learned that `enumerate()` gives both the index and value while traversing a list.
- I learned that the best case can be `O(1)` when the target is found immediately.
- I learned that the average and worst cases are `O(n)` for linear search.
- I learned that the algorithm can return early as soon as the target is found.
- I reinforced that the extra space is `O(1)`.

---

## Mistakes I Made

My initial explanation said to return the target when it was found. I corrected this after checking the actual problem requirement.

The problem asks for the **index of the target**, not the target value itself.

For example:

```text
numbers = [4, 8, 1, 9, 3, 7]
target = 9
```

The target is `9`, but the required answer is its index:

```text
3
```

This is why the implementation uses:

```python
return i
```

instead of:

```python
return n
```

---

## Pattern

**Linear Search / Array Traversal**

The general pattern is:

```text
Start from the beginning
        ↓
Check current element
        ↓
Found?
 ┌──────┴──────┐
Yes           No
 ↓              ↓
Return index   Move forward
                  ↓
              Repeat
                  ↓
             End reached?
                  ↓
               Return -1
```

Linear search is useful when the array is not sorted and we need to find a particular value by checking elements sequentially.

---

## Status

- [x] Problem understood
- [x] Algorithm designed
- [x] Implementation completed
- [x] Target found case tested
- [x] Target not found case tested
- [x] Empty input tested
- [x] Best-case complexity understood
- [x] Worst-case complexity understood
- [x] Space complexity analyzed
- [x] Solution verified
