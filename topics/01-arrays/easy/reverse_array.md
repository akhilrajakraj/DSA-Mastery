# Reverse an Array

## Problem

Reverse an array **in-place**.

For example:

```python
[1, 2, 3, 4, 5]
```

should become:

```python
[5, 4, 3, 2, 1]
```

The solution should not create a second array.

---

## My Approach

I use two pointers:

- `left` starts at the first index (`0`).
- `right` starts at the last index (`len(numbers) - 1`).

While `left < right`, I swap the values at those two positions and then move both pointers toward the middle.

This means:

```text
first   ↔ last
second  ↔ second-last
third   ↔ third-last
...
```

Once the pointers meet or cross, every required pair has been swapped.

---

## Algorithm

1. Set `left = 0`.
2. Set `right = len(numbers) - 1`.
3. While `left < right`:
   - Swap `numbers[left]` and `numbers[right]`.
   - Increment `left`.
   - Decrement `right`.
4. Return the modified array.

The array is modified directly, so no additional array is required.

---

## Implementation

The implementation is available in `reverse_array.py`.

Core logic:

```python
left = 0
right = len(numbers) - 1

while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]
    left += 1
    right -= 1

return numbers
```

Python allows the two values to be swapped directly without manually creating a temporary variable.

---

## Dry Run — Odd-Length Array

For:

```text
[1, 2, 3, 4, 5]
```

Initial state:

```text
left = 0
right = 4
```

First swap:

```text
index 0 ↔ index 4
1 ↔ 5

[5, 2, 3, 4, 1]
```

Move pointers:

```text
left = 1
right = 3
```

Second swap:

```text
index 1 ↔ index 3
2 ↔ 4

[5, 4, 3, 2, 1]
```

Move pointers:

```text
left = 2
right = 2
```

Now `left < right` is false, so the loop stops.

The middle element does not need to be swapped with itself.

---

## Dry Run — Even-Length Array

For:

```text
[10, 20, 30, 40, 50, 60]
```

Initial state:

```text
left = 0
right = 5
```

First swap:

```text
10 ↔ 60
[60, 20, 30, 40, 50, 10]
```

Then:

```text
left = 1
right = 4
```

Second swap:

```text
20 ↔ 50
[60, 50, 30, 40, 20, 10]
```

Then:

```text
left = 2
right = 3
```

Third swap:

```text
30 ↔ 40
[60, 50, 40, 30, 20, 10]
```

Then:

```text
left = 3
right = 2
```

The pointers have crossed, so the loop stops.

---

## Why `left < right`?

The loop condition is:

```python
while left < right:
```

We do not need to continue when the pointers are equal because that means they have reached the middle of an odd-length array.

For an even-length array, the pointers eventually cross.

Therefore the process stops when:

```text
left >= right
```

---

## Edge Cases

### Single element

```python
[10]
```

Output:

```text
[10]
```

No swap is required.

### Empty array

```python
[]
```

Output:

```text
[]
```

`right` becomes `-1`, so `left < right` is immediately false.

### Negative numbers

```python
[-5, -10, -2, -8]
```

Output:

```text
[-8, -2, -10, -5]
```

The algorithm works independently of the sign of the values.

---

## In-Place Verification

The solution modifies the original list instead of creating a new list.

For example:

```python
numbers = [1, 2, 3, 4, 5]
reverse_array(numbers)
print(numbers)
```

Output:

```text
[5, 4, 3, 2, 1]
```

This confirms that the original list itself was changed.

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

We process approximately half of the elements, but `O(n / 2)` simplifies to `O(n)` in Big-O notation.

### Space Complexity

```text
O(1)
```

Only the `left` and `right` pointers and constant swap storage are used. No additional array grows with the input size.

---

## What I Learned

- I learned how to reverse an array using two pointers.
- I learned that the first element swaps with the last, the second with the second-last, and so on.
- I learned why `len(numbers) - 1` gives the final valid index.
- I learned why the loop condition should be `left < right`.
- I learned the difference between pointers meeting and pointers crossing.
- I learned how to modify an array in-place.
- I reinforced that processing half of an array is still `O(n)`.

---

## Mistakes / Clarifications

Initially, I thought about tracking the `0th` and `1st` indexes. The correct approach is to track the two ends of the array:

```text
left  → beginning
right → end
```

The pointers then move inward after every swap.

I also initially described the loop as stopping when `left` and `right` become equal. That is true for odd-length arrays, but for even-length arrays the pointers cross. The more accurate rule is:

```text
Continue while left < right.
Stop when left >= right.
```

---

## Pattern

**Two-Pointer / In-Place Array Manipulation**

```text
left →                ← right
[  1,  2,  3,  4,  5  ]
   ↘                ↙
      swap values
         ↓
[  5,  2,  3,  4,  1  ]
         ↓
      move inward
```

This two-pointer pattern will appear frequently in later DSA problems.

---

## Status

- [x] Problem understood
- [x] Two-pointer approach designed
- [x] In-place implementation completed
- [x] Odd-length array tested
- [x] Even-length array tested
- [x] Single-element array tested
- [x] Empty array tested
- [x] Negative numbers tested
- [x] In-place modification verified
- [x] Complexity analyzed
- [x] Solution verified
