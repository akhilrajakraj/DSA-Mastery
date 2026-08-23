# Find Minimum Element

## Problem

Given an array of numbers, find and return the minimum element in the array.

### Example

Input:

```python
[7, 3, 9, 2, 8, 1, 5]
```

Output:

```text
1
```

---

## My Approach

I first check whether the list is empty. If it is empty, there is no minimum element, so I raise a `ValueError`.

For a non-empty list, I assume that the element at index `0` is the minimum.

Then I traverse through the array and compare every element with the current minimum. If I find a smaller element, I update the minimum variable.

After checking all the elements, I return the minimum value.

---

## Algorithm

1. Check whether the list is empty.
2. If the list is empty, raise a `ValueError`.
3. Store the first element as the initial minimum.
4. Traverse through the array.
5. Compare each element with the current minimum.
6. If the current element is smaller, update the minimum.
7. Return the minimum.

---

## Implementation

The implementation is available in `find_minimum.py`.

Core logic:

```python
minimum = numbers[0]

for n in numbers:
    if n < minimum:
        minimum = n
```

---

## Dry Run

For:

```text
[7, 3, 9, 2, 8, 1, 5]
```

Initially:

```text
minimum = 7
```

Then:

```text
3 < 7  → minimum = 3
9 < 3  → no change
2 < 3  → minimum = 2
8 < 2  → no change
1 < 2  → minimum = 1
5 < 1  → no change
```

Final answer:

```text
1
```

---

## Edge Cases

### 1. Normal input

```python
[7, 3, 9, 2, 8, 1, 5]
```

Output:

```text
1
```

### 2. Negative numbers

```python
[-5, -2, -10, -3]
```

Output:

```text
-10
```

### 3. Single element

```python
[7]
```

Output:

```text
7
```

### 4. Empty list

```python
[]
```

The function raises:

```text
ValueError
```

because an empty list has no minimum element.

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

I potentially inspect every element exactly once.

### Space Complexity

```text
O(1)
```

I only use one additional variable, `minimum`, regardless of the input size.

---

## What I Learned

- I learned how to find the minimum without using Python's built-in `min()` function.
- I learned that the first element can be used as the initial minimum.
- I learned that the same array-traversal pattern used for finding a maximum can be reversed to find a minimum.
- I reinforced the importance of handling negative numbers correctly.
- I learned how to handle an empty input explicitly.
- I reinforced that one complete traversal gives `O(n)` time and constant extra space gives `O(1)` space.

---

## Mistakes I Made

I did not make a major algorithmic mistake in this problem. I correctly applied the pattern from the previous problem:

```text
maximum → compare using >
minimum → compare using <
```

I also kept the empty-list check from the previous problem so that the function does not try to access `numbers[0]` when there is no element.

---

## Pattern

**Array Traversal with a Running Result**

The general pattern is:

```text
Initialize a variable
        ↓
Traverse the array
        ↓
Compare current element
        ↓
Update stored result when necessary
        ↓
Return result
```

This is the same pattern used in the maximum-element problem, with the comparison direction changed.

---

## Status

- [x] Problem understood
- [x] Algorithm designed
- [x] Implementation completed
- [x] Negative numbers tested
- [x] Single element tested
- [x] Empty input tested
- [x] Complexity analyzed
- [x] Solution verified
