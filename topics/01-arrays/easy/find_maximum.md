# Find Maximum Element

## Problem

Given an array of numbers, find and return the maximum element in the array.

### Example

Input:

```python
[4, 6, 7, 8, 4, 3, 2, 1, 0, 9]
```

Output:

```text
9
```

---

## My Approach

I first assume that the element at index `0` is the maximum.

Then I traverse through the array and compare every element with the current maximum.

If I find an element that is larger than the current maximum, I update the maximum variable.

After checking all the elements, I return the maximum value.

---

## Algorithm

1. Check whether the list is empty.
2. If the list is empty, raise a `ValueError` because an empty list has no maximum element.
3. Store the first element as the initial maximum.
4. Traverse through the array.
5. For every element:
   - Compare it with the current maximum.
   - If it is larger, update the maximum.
6. Return the maximum.

---

## Implementation

The implementation is available in `find_maximum.py`.

Core logic:

```python
maximum = numbers[0]

for n in numbers:
    if n > maximum:
        maximum = n
```

---

## Dry Run

For:

```text
[4, 6, 7, 8, 4, 3, 2, 1, 0, 9]
```

Initially:

```text
maximum = 4
```

Then:

```text
6 > 4  → maximum = 6
7 > 6  → maximum = 7
8 > 7  → maximum = 8
4 > 8  → no change
3 > 8  → no change
2 > 8  → no change
1 > 8  → no change
0 > 8  → no change
9 > 8  → maximum = 9
```

Final answer:

```text
9
```

---

## Edge Cases

### 1. Normal input

```python
[4, 8, 1, 9, 3]
```

Output:

```text
9
```

### 2. Negative numbers

```python
[-5, -2, -10, -3]
```

Output:

```text
-2
```

This is why I should not initialize the maximum as `0`.

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

The function raises `ValueError` because an empty list has no maximum element.

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

I only use one additional variable, `maximum`, regardless of the input size.

---

## What I Learned

- I learned how to find the maximum without using Python's built-in `max()` function.
- I learned that I should initialize the maximum using the first element rather than `0`.
- This is important because the array can contain only negative numbers.
- I learned how to handle an empty input explicitly.
- I reinforced the difference between `O(n)` time and `O(1)` extra space.
- I learned that a simple traversal can solve many array problems efficiently.

---

## Mistakes I Made

### Mistake 1 — Initializing maximum to `0`

My first implementation used:

```python
maximum = 0
```

This fails for an array such as:

```python
[-5, -2, -10, -3]
```

because it would incorrectly return `0`.

### Correction

I changed it to:

```python
maximum = numbers[0]
```

This correctly handles both positive and negative numbers.

### Mistake 2 — Using `max` as a variable name

I initially used:

```python
max = 0
```

I learned that `max` is already a Python built-in function, so using `maximum` is clearer and avoids overwriting the built-in name.

---

## Pattern

**Array Traversal**

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

This pattern will appear repeatedly in array and other DSA problems.

---

## Status

- [x] Problem understood
- [x] Algorithm designed
- [x] Implementation completed
- [x] Edge cases tested
- [x] Complexity analyzed
- [x] Solution verified
