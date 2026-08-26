# Check if an Array Is Sorted

## Problem

Determine whether an array is sorted in ascending order.

Equal adjacent values are allowed.

Examples:

```python
[1, 2, 3, 4, 5]     # True
[1, 3, 2, 4, 5]     # False
[1, 2, 2, 3, 4]     # True
```

---

## My Approach

I compare every pair of adjacent elements.

For ascending order, the current element must never be greater than the next element.

Therefore, I look for the condition that proves the array is **not** sorted:

```python
numbers[i] > numbers[i + 1]
```

If this condition occurs, I immediately return `False` because one out-of-order pair is enough to prove that the whole array is not sorted.

If the complete traversal finishes without finding such a pair, I return `True`.

---

## Algorithm

1. Traverse from index `0` to `len(numbers) - 2`.
2. Compare `numbers[i]` with `numbers[i + 1]`.
3. If `numbers[i] > numbers[i + 1]`, return `False` immediately.
4. If no violation is found, return `True`.

The loop uses `len(numbers) - 1` because the final element has no next element to compare with.

---

## Implementation

The implementation is available in `sorted_array.py`.

```python
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        return False

return True
```

---

## Dry Run

For:

```text
[1, 2, 3, 4, 5]
```

The comparisons are:

```text
1 ≤ 2  ✓
2 ≤ 3  ✓
3 ≤ 4  ✓
4 ≤ 5  ✓
```

No violation is found, so the result is:

```text
True
```

For:

```text
[1, 3, 2, 4, 5]
```

The comparisons begin:

```text
1 ≤ 3  ✓
3 > 2  ✗
```

The function immediately returns:

```text
False
```

There is no reason to inspect the remaining elements because the array has already been proven unsorted.

---

## Edge Cases Tested

### Normal sorted array

```python
[1, 2, 3, 4, 5]
```

Result: `True`

### Unsorted array

```python
[1, 3, 2, 4, 5]
```

Result: `False`

### Duplicate values

```python
[1, 2, 2, 3, 4]
```

Result: `True`

Equal adjacent values are allowed because `2 > 2` is false.

### Reverse sorted

```python
[5, 4, 3, 2, 1]
```

Result: `False`

### Single element

```python
[10]
```

Result: `True`

There is no pair that can violate the sorted condition.

### Empty array

```python
[]
```

Result: `True`

There are no adjacent elements that violate the condition.

### Negative numbers

```python
[-10, -5, -3, 0, 4]
```

Result: `True`

### Negative numbers but unsorted

```python
[-10, -3, -5, 0, 4]
```

Result: `False`

because:

```text
-3 > -5
```

---

## Complexity Analysis

### Time Complexity

```text
Worst case: O(n)
```

In the worst case, the entire array must be checked.

### Best Case

```text
O(1)
```

If the first adjacent pair is out of order, the function returns immediately.

Example:

```python
[5, 1, 2, 3, 4]
```

The first comparison is:

```text
5 > 1
```

so the function stops immediately.

### Space Complexity

```text
O(1)
```

Only the loop index is required. No additional data structure grows with the input size.

---

## What I Learned

- I learned to compare adjacent elements when checking whether an array is sorted.
- I learned to search for the condition that proves the answer is false instead of unnecessarily checking for every condition that proves it is true.
- I learned that one out-of-order adjacent pair is enough to prove an array is not sorted.
- I learned about **early termination**: once the answer is known, stop processing.
- I reinforced why `range(len(numbers) - 1)` is necessary when accessing `i + 1`.
- I reinforced that equal adjacent values are valid in ascending order.
- I reinforced the difference between best-case `O(1)` and worst-case `O(n)` time.

---

## Pattern

**Adjacent Comparison + Early Termination**

The general pattern is:

```text
Traverse adjacent elements
        ↓
Check for a violation
        ↓
Violation found?
   ↙          ↘
 Yes           No
  ↓             ↓
return False  continue
                ↓
          finish traversal
                ↓
           return True
```

This is a useful pattern for validation problems where a single counterexample is enough to reject the input.

---

## Status

- [x] Problem understood
- [x] Adjacent comparison identified
- [x] Early termination implemented
- [x] Sorted input tested
- [x] Unsorted input tested
- [x] Duplicate values tested
- [x] Reverse sorted input tested
- [x] Single-element input tested
- [x] Empty input tested
- [x] Negative values tested
- [x] Complexity analyzed
- [x] Solution verified
