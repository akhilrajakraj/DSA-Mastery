# Rotate Array

## Problem

Rotate an array to the **right by `k` positions**.

For example:

```text
[1, 2, 3, 4, 5], k = 2
```

becomes:

```text
[4, 5, 1, 2, 3]
```

The last `k` elements move to the front, while the remaining elements shift to the right.

---

## My Approach

I solved this using **array slicing**.

The key observation is that for a right rotation by `k` positions, the array can be divided into two parts:

```text
[elements that stay at the back | elements that move to the front]
```

For:

```text
[1, 2, 3, 4, 5], k = 2
```

we split the array as:

```text
[1, 2, 3 | 4, 5]
```

Then move the last part to the front:

```text
[4, 5] + [1, 2, 3]
```

which gives:

```text
[4, 5, 1, 2, 3]
```

The split position is:

```python
split = n - k
```

where `n` is the length of the array.

---

## Important Step: Handle Large `k`

`k` can be larger than the array length.

For example, with five elements:

```text
k = 7
```

Rotating seven times is equivalent to rotating:

```text
7 % 5 = 2
```

positions.

So I normalize `k` using:

```python
k = k % n
```

This is an important general idea: when an operation repeats in a cycle of length `n`, values larger than `n` can often be reduced using modulo.

Examples:

```text
7 % 5  = 2
12 % 5 = 2
5 % 5  = 0
```

---

## Algorithm

1. Check whether the array is empty. If it is, return an empty list.
2. Find the array length `n`.
3. Normalize `k` using `k % n`.
4. Calculate the split position using `n - k`.
5. Take the last `k` elements using `numbers[split:]`.
6. Take the remaining elements using `numbers[:split]`.
7. Concatenate them in the new order.
8. Return the rotated array.

Core logic:

```python
if not numbers:
    return []

n = len(numbers)
k = k % n
split = n - k

numbers = numbers[split:] + numbers[:split]

return numbers
```

---

## Dry Run

Input:

```text
numbers = [1, 2, 3, 4, 5]
k = 2
```

### Step 1: Length

```text
n = 5
```

### Step 2: Normalize `k`

```text
k = 2 % 5 = 2
```

### Step 3: Find split position

```text
split = n - k
      = 5 - 2
      = 3
```

### Step 4: Split the array

```text
numbers[:3] = [1, 2, 3]
numbers[3:] = [4, 5]
```

### Step 5: Move the last part to the front

```text
[4, 5] + [1, 2, 3]
```

Final result:

```text
[4, 5, 1, 2, 3]
```

---

## Understanding the Split

The formula:

```python
split = n - k
```

is the most important part of this solution.

For:

```text
n = 5
k = 2
```

there should be exactly two elements at the front after rotation. Those are the last two original elements, so the split occurs at index `3`.

Visualizing it:

```text
index:   0  1  2 | 3  4
array:  [1, 2, 3 | 4, 5]
                    ↑  ↑
                move to front
```

After rotation:

```text
[4, 5 | 1, 2, 3]
```

---

## Mistakes and Debugging Lessons

During the initial implementation, I made mistakes in understanding how to calculate the split.

### Mistake 1: Reusing `k` incorrectly in a loop

I initially wrote logic similar to:

```python
for k in numbers:
```

This was incorrect because `k` already represents the number of rotation positions. Using it as the loop variable would overwrite the value of `k`.

The important lesson is that variable names should keep one clear meaning throughout the algorithm.

### Mistake 2: Treating an integer like a list

I also tried to build the split using slicing on `k` and subtraction involving slices.

The problem is that:

```text
k → integer
numbers[:k] → list
```

These are different types and have different operations.

The correct reasoning is to calculate a numeric split index first:

```python
split = n - k
```

and then use that integer as a slicing boundary.

### Mistake 3: Confusing rotation with other transformations

I initially had confusion about what a right rotation actually does. The important definition is:

```text
right rotation by k
→ take the last k elements
→ move them to the front
```

It is not reversing the array and it does not introduce or remove values.

---

## Edge Cases Tested

### `k = 1`

```python
[1, 2, 3, 4, 5], 1
```

Result:

```text
[5, 1, 2, 3, 4]
```

### `k = 3`

```python
[1, 2, 3, 4, 5, 6, 7], 3
```

Result:

```text
[5, 6, 7, 1, 2, 3, 4]
```

### `k` equals array length

```python
[1, 2, 3, 4, 5], 5
```

Result:

```text
[1, 2, 3, 4, 5]
```

because:

```text
5 % 5 = 0
```

### `k` greater than array length

```python
[1, 2, 3, 4, 5], 7
```

Result:

```text
[4, 5, 1, 2, 3]
```

because:

```text
7 % 5 = 2
```

### Much larger `k`

```python
[1, 2, 3, 4, 5], 12
```

Result:

```text
[4, 5, 1, 2, 3]
```

because:

```text
12 % 5 = 2
```

### Single-element array

```python
[1], 5
```

Result:

```text
[1]
```

### Empty array

```python
[], 3
```

Result:

```text
[]
```

The empty-input check also prevents calculating `k % n` when `n = 0`.

### `k = 0`

```python
[1, 2, 3, 4, 5], 0
```

Result:

```text
[1, 2, 3, 4, 5]
```

### Negative values

```python
[-1, -2, -3, -4, -5], 2
```

Result:

```text
[-4, -5, -1, -2, -3]
```

The rotation logic is independent of whether the values are positive or negative.

---

## Test Cases

```python
# Test 1: Basic rotation
print(rotate_array([1, 2, 3, 4, 5], 2))

# Test 2: Rotate by 1
print(rotate_array([1, 2, 3, 4, 5], 1))

# Test 3: Rotate by 3
print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))

# Test 4: k equals array length
print(rotate_array([1, 2, 3, 4, 5], 5))

# Test 5: k greater than array length
print(rotate_array([1, 2, 3, 4, 5], 7))

# Test 6: k much greater than array length
print(rotate_array([1, 2, 3, 4, 5], 12))

# Test 7: Single element
print(rotate_array([1], 5))

# Test 8: Empty array
print(rotate_array([], 3))

# Test 9: k is zero
print(rotate_array([1, 2, 3, 4, 5], 0))

# Test 10: Negative numbers
print(rotate_array([-1, -2, -3, -4, -5], 2))
```

All ten test cases were verified successfully.

---

## Complexity Analysis

Let `n` be the number of elements in the array.

### Time Complexity

```text
O(n)
```

The slicing and concatenation operations create a new list containing the array elements.

### Space Complexity

```text
O(n)
```

The implementation creates new lists through slicing and concatenation, so the additional memory grows with the size of the input.

This is an important trade-off: the solution is simple and readable, but it is **not an in-place `O(1)` extra-space rotation**.

An in-place reversal-based solution can be studied later when array manipulation and two-pointer techniques are revisited.

---

## What I Learned

- A right rotation by `k` means moving the last `k` elements to the front.
- The split index is `n - k` after normalizing `k`.
- `k % n` handles rotations larger than the array length.
- I learned to distinguish an index from the value stored in the array.
- I reinforced that variable names should preserve one clear meaning throughout an algorithm.
- I learned that slicing can give a clean implementation, but it creates additional lists.
- I practiced identifying and correcting type/operation mistakes while implementing the idea.
- I tested normal rotations, zero rotation, full rotation, oversized rotations, empty input, single-element input, and negative values.
- I learned that a correct solution can still have a meaningful optimization opportunity: the current version uses `O(n)` extra space rather than rotating in-place.

---

## Pattern

**Array Slicing + Cyclic Rotation**

General idea:

```text
Normalize k
    ↓
Find split = n - k
    ↓
Take last k elements
    ↓
Place them before the remaining elements
```

A deeper pattern to recognize is **cyclic behavior**: when an operation repeats every `n` positions, modulo can reduce the number of operations without changing the final state.

The problem also introduces an important optimization question:

```text
Simple solution:
O(n) time, O(n) extra space

More advanced solution:
O(n) time, O(1) extra space
```

For the current stage, the priority was understanding rotation correctly and implementing it from scratch. The in-place optimization is a later mastery target.

---

## Status

- [x] Problem understood
- [x] Right rotation definition understood
- [x] Split index derived
- [x] Large `k` handled with modulo
- [x] Array slicing implemented
- [x] Empty input handled
- [x] Single-element input tested
- [x] `k = 0` tested
- [x] `k = n` tested
- [x] `k > n` tested
- [x] Negative values tested
- [x] Mistakes identified and corrected
- [x] Complexity analyzed
- [x] Space trade-off understood
- [x] Solution verified
