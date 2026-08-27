# Move Zeroes

## Problem

Move all zeroes in an array to the end **in-place**, while preserving the relative order of all non-zero elements.

Example:

```python
[0, 1, 0, 3, 12]
```

becomes:

```python
[1, 3, 12, 0, 0]
```

---

## My Approach

I used the **read/write two-pointer pattern**.

- `read` scans every element in the array.
- `write` tracks the position where the next non-zero element should be placed.

When `read` encounters a zero, I ignore it and only move `read` forward.

When `read` encounters a non-zero value, I copy that value to `numbers[write]` and then move `write` forward.

After all elements have been scanned, every non-zero value is at the beginning of the array in its original relative order. The remaining positions are then filled with zeroes.

---

## Algorithm

1. Initialize `write = 0`.
2. Initialize `read = 0`.
3. Traverse the entire array with `read`.
4. Check the **value** `numbers[read]`, not the index `read`.
5. If the value is non-zero:
   - Copy it to `numbers[write]`.
   - Increment `write`.
6. Increment `read` after every iteration.
7. After the complete traversal, fill positions from `write` to the end with `0`.
8. Return the modified array.

---

## Important Debugging Lesson

My first implementation contained two mistakes.

### Mistake 1: Checking the index instead of the value

I initially wrote:

```python
if read != 0:
```

But `read` is an index. The problem asks whether the **element** at that index is zero.

The correct condition is:

```python
if numbers[read] != 0:
```

This reinforced an important distinction:

```text
read       → index
numbers[read] → value at that index
```

### Mistake 2: Filling zeroes inside the scanning loop

I initially placed the zero-filling loop inside the `while` loop. That caused values that still needed to be inspected to be overwritten with zeroes.

The correct order is:

```text
Scan the complete array
        ↓
Place all non-zero values
        ↓
Finish scanning
        ↓
Fill remaining positions with zeroes
```

The zero-filling loop must therefore happen **after** the scanning loop.

---

## Dry Run

Input:

```text
[0, 1, 0, 3, 12]
```

Initial state:

```text
write = 0
read = 0
```

### `read = 0`

```text
numbers[0] = 0
```

Zero, so ignore it.

```text
write = 0
read = 1
```

### `read = 1`

```text
numbers[1] = 1
```

Non-zero, so:

```text
numbers[write] = numbers[read]
numbers[0] = numbers[1]
```

The useful portion begins with:

```text
[1, ...]
```

Then:

```text
write = 1
read = 2
```

### `read = 2`

Value is `0`.

Ignore it.

```text
write = 1
read = 3
```

### `read = 3`

Value is `3`.

Copy it to the write position:

```text
numbers[1] = numbers[3]
```

Useful portion:

```text
[1, 3, ...]
```

Then:

```text
write = 2
read = 4
```

### `read = 4`

Value is `12`.

Copy it to:

```text
numbers[2] = numbers[4]
```

Useful portion:

```text
[1, 3, 12, ...]
```

Now:

```text
write = 3
```

The scan is complete.

The remaining positions start at index `3`, so fill them with zeroes:

```text
[1, 3, 12, 0, 0]
```

---

## Why We Need `write`

`write` represents the next available position for a non-zero value.

For:

```text
[0, 1, 0, 3, 12]
```

we can think of the array as two regions while processing:

```text
[non-zero values | unprocessed / remaining values]
```

The `read` pointer searches through the array, while `write` maintains the boundary of the non-zero region.

---

## Relative Order

The non-zero elements must remain in their original order.

Input:

```text
[0, 1, 0, 3, 12]
```

Non-zero values appear as:

```text
1 → 3 → 12
```

The result keeps exactly that order:

```text
[1, 3, 12, 0, 0]
```

---

## Edge Cases Tested

### Zeroes at the beginning

```python
[0, 0, 1, 2, 0, 3]
```

Result:

```text
[1, 2, 3, 0, 0, 0]
```

### No zeroes

```python
[1, 2, 3]
```

Result:

```text
[1, 2, 3]
```

### All zeroes

```python
[0, 0, 0]
```

Result:

```text
[0, 0, 0]
```

### Empty array

```python
[]
```

Result:

```text
[]
```

### Zeroes between non-zero values

```python
[1, 0, 2, 0, 3, 0]
```

Result:

```text
[1, 2, 3, 0, 0, 0]
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

The array is traversed once to move the non-zero values and once more to fill the remaining positions with zeroes.

Because these loops are sequential rather than nested:

```text
O(n) + O(n) = O(n)
```

### Space Complexity

```text
O(1)
```

No additional list or data structure is created. The transformation is performed in-place.

---

## What I Learned

- I learned another application of the **read/write two-pointer pattern**.
- `read` scans the input, while `write` tracks where the next useful value belongs.
- I learned the difference between an index and the value stored at that index.
- Zeroes can be ignored during the first pass instead of being explicitly stored elsewhere.
- The remaining positions can be filled after the scan is complete.
- The relative order of non-zero values is preserved naturally because `read` processes them from left to right.
- Two sequential `O(n)` loops still give `O(n)`, not `O(n²)`.
- I learned that modifying the array during the scan must be done carefully so that values still needed by `read` are not destroyed.

---

## Pattern

**Two Pointers — Read/Write + In-Place Filtering**

General idea:

```text
read → inspect every element
write → maintain the next position for a value we want to keep
```

For this problem:

```text
zero:
    ignore

non-zero:
    numbers[write] = numbers[read]
    write += 1

after scanning:
    fill remaining positions with zero
```

This pattern is useful when an array needs to be transformed in-place while preserving the order of selected elements.

---

## Status

- [x] Problem understood
- [x] Read/write pointers identified
- [x] Non-zero filtering implemented
- [x] In-place modification implemented
- [x] Relative order preserved
- [x] Zero-filling step implemented after traversal
- [x] Index vs value mistake identified and fixed
- [x] Loop-placement mistake identified and fixed
- [x] Zero-heavy input tested
- [x] No-zero input tested
- [x] All-zero input tested
- [x] Empty input tested
- [x] Complexity analyzed
- [x] Solution verified
