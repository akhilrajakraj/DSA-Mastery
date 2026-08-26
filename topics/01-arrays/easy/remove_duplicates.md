# Remove Duplicates from a Sorted Array

## Problem

Given a sorted array, remove duplicate values **in-place** so that each distinct value appears once in the beginning of the same array.

The function returns the number `k` of unique values. The first `k` positions of the array contain the unique values.

Example:

```python
[1, 1, 2, 2, 3, 3, 4]
```

becomes effectively:

```text
[1, 2, 3, 4, ...]
```

and the function returns:

```text
4
```

The values after the first `k` positions are irrelevant.

---

## My Approach

I used the **two-pointer read/write pattern**.

- `read` scans through the array and looks for the next value.
- `write` marks the position where the next unique value should be placed.

Because the array is sorted, duplicate values are next to each other. Therefore, I do not need another set or list to remember duplicates.

If the value at `read` is equal to the current unique value at `write`, it is a duplicate, so I leave `write` where it is and continue scanning.

If the value is different, it is a new unique value. I move `write` forward and copy the value at `read` into that position.

---

## Algorithm

1. If the array is empty, return `0`.
2. Start `write` at index `0`.
3. Start `read` at index `1`.
4. Scan the array using `read`.
5. If `numbers[read]` is different from `numbers[write]`:
   - Increment `write`.
   - Copy `numbers[read]` to `numbers[write]`.
6. Continue until every element has been examined.
7. Return `write + 1`.

The `+1` is necessary because `write` is an index, while the function must return the number of unique elements.

For example, if the final unique value is at index `3`, there are four elements at indexes `0, 1, 2, 3`.

---

## Implementation

The implementation is available in `remove_duplicates.py`.

Core logic:

```python
if not numbers:
    return 0

write = 0

for read in range(1, len(numbers)):
    if numbers[read] != numbers[write]:
        write += 1
        numbers[write] = numbers[read]

return write + 1
```

---

## Dry Run

Input:

```text
[1, 1, 2, 2, 3, 3, 4]
```

Initial state:

```text
write = 0
read = 1
```

### `read = 1`

```text
1 == 1
```

Duplicate.

```text
write stays at 0
```

### `read = 2`

```text
2 != 1
```

Unique.

Move `write`:

```text
write = 1
```

Copy:

```text
numbers[1] = numbers[2]
```

The useful portion is now:

```text
[1, 2, ...]
```

### `read = 3`

```text
2 == 2
```

Duplicate. `write` stays at `1`.

### `read = 4`

```text
3 != 2
```

Unique.

Move `write` to `2` and copy `3` there.

Useful portion:

```text
[1, 2, 3, ...]
```

### `read = 5`

```text
3 == 3
```

Duplicate. `write` stays at `2`.

### `read = 6`

```text
4 != 3
```

Unique.

Move `write` to `3` and copy `4` there.

Final useful portion:

```text
[1, 2, 3, 4]
```

The final `write` index is `3`, so:

```text
write + 1 = 4
```

Therefore the function returns `4`.

---

## Why the Sorted Property Matters

The sorted input is what makes this approach simple.

For:

```text
[1, 1, 2, 2, 3, 3, 4]
```

equal values appear consecutively.

Therefore, when `numbers[read] == numbers[write]`, we know the value has already been kept in the unique portion.

If the array were unsorted, equal values could be far apart and this simple adjacent/read-write approach would not be sufficient by itself.

---

## In-Place Modification

No second list is created.

The beginning of the original array becomes the storage area for the unique values:

```text
[1, 1, 2, 2, 3, 3, 4]
 ↓
[1, 2, 3, 4, ...]
```

Only the first `k` positions matter after the function returns.

For example:

```python
numbers = [1, 1, 2, 2, 3, 3, 4]
k = remove_duplicates(numbers)

print(k)
print(numbers[:k])
```

Expected:

```text
4
[1, 2, 3, 4]
```

---

## Edge Cases Tested

### Multiple duplicates

```python
[1, 1, 2, 2, 3, 3, 4]
```

Result:

```text
4
```

### All values are duplicates

```python
[1, 1, 1, 1]
```

Result:

```text
1
```

### No duplicates

```python
[1, 2, 3, 4, 5]
```

Result:

```text
5
```

### Single element

```python
[1]
```

Result:

```text
1
```

### Empty array

```python
[]
```

Result:

```text
0
```

The empty-array check is necessary because otherwise `write + 1` would incorrectly return `1` when there are actually zero elements.

### Values containing zero

```python
[0, 0, 1, 1, 2, 2, 3]
```

Result:

```text
4
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

The `read` pointer traverses the array once.

### Space Complexity

```text
O(1)
```

Only the `read` and `write` pointers are used. No additional data structure grows with the input size.

---

## What I Learned

- I learned the **read/write two-pointer pattern**.
- I learned that the two pointers can have different responsibilities rather than simply moving toward each other.
- `read` scans the input while `write` maintains the position for the next useful value.
- Because the array is sorted, duplicates appear next to each other and can simply be ignored.
- I learned that the unique values can be written into the beginning of the original array instead of creating another list.
- I learned that `write` is an index, so the number of unique elements is `write + 1` for a non-empty array.
- I found an empty-array boundary case during testing: returning `write + 1` without checking for an empty array gives `1` instead of `0`.
- I reinforced that testing boundary cases is part of solving the problem, not an afterthought.

---

## Pattern

**Two Pointers — Read/Write**

General pattern:

```text
read → scans every element
write → tracks where the next useful element belongs
```

If the current value is a duplicate:

```text
read moves
write stays
```

If the current value is new:

```text
write moves
copy read value to write position
read moves
```

This pattern is useful for in-place array transformations where some elements are kept and others are ignored or replaced.

---

## Status

- [x] Problem understood
- [x] Read/write pointers identified
- [x] Sorted-array property understood
- [x] Duplicate handling implemented
- [x] In-place modification implemented
- [x] Return count understood
- [x] Empty-array edge case found and fixed
- [x] Duplicate-heavy input tested
- [x] No-duplicate input tested
- [x] Single-element input tested
- [x] Empty input tested
- [x] Zero values tested
- [x] Complexity analyzed
- [x] Solution verified
