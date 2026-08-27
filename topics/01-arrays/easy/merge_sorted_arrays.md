# Merge Two Sorted Arrays

## Problem

Given two sorted arrays, merge them into one sorted array.

Example:

```python
first = [1, 3, 5]
second = [2, 4, 6]
```

Result:

```text
[1, 2, 3, 4, 5, 6]
```

For this problem, the merged result is stored in a new list.

---

## My Approach

I use two pointers:

- `i` points to the current element in the first array.
- `j` points to the current element in the second array.
- `result` stores the merged sorted array.

Both pointers start at index `0`.

At each step, I compare `first[i]` and `second[j]`. The smaller value is appended to `result`, and the pointer belonging to the array whose value was selected is moved forward.

When one array reaches its end, the remaining elements of the other array are already sorted, so they can be appended directly.

---

## Algorithm

1. Initialize `i = 0` and `j = 0`.
2. Create an empty `result` list.
3. While both arrays still contain unprocessed elements:
   - Compare `first[i]` and `second[j]`.
   - Append the smaller value to `result`.
   - Move the corresponding pointer.
4. Append any remaining elements from `first`.
5. Append any remaining elements from `second`.
6. Return `result`.

---

## Equality Case

If the current values are equal, the implementation uses:

```python
if first[i] <= second[j]:
```

This allows the first array's value to be selected when both values are equal. The other equal value remains in the second array and is processed on a later iteration.

For example:

```text
first[i] = 1
second[j] = 1
```

One `1` is appended, `i` moves, and the other `1` is then processed normally.

---

## Important Debugging Lesson

My first implementation used:

```python
result = first[i]
```

and:

```python
result = second[j]
```

This replaced the entire `result` list with an integer.

Later, when the program tried:

```python
result.append(second[j])
```

Python raised:

```text
AttributeError: 'int' object has no attribute 'append'
```

The correct operation is:

```python
result.append(first[i])
```

or:

```python
result.append(second[j])
```

The distinction is:

```text
result = value          → replaces the list
result.append(value)    → adds the value to the existing list
```

I also needed to handle the equality case. Without `<=` or an equivalent equality branch, if `first[i] == second[j]`, neither pointer would move and the loop could continue indefinitely.

---

## Dry Run

Input:

```text
first  = [1, 3, 5]
second = [2, 4, 6]
```

Initial state:

```text
i = 0
j = 0
result = []
```

Compare:

```text
1 vs 2
```

`1` is smaller:

```text
result = [1]
i = 1
```

Compare:

```text
3 vs 2
```

`2` is smaller:

```text
result = [1, 2]
j = 1
```

Compare:

```text
3 vs 4
```

`3` is smaller:

```text
result = [1, 2, 3]
i = 2
```

Compare:

```text
5 vs 4
```

`4` is smaller:

```text
result = [1, 2, 3, 4]
j = 2
```

Compare:

```text
5 vs 6
```

`5` is smaller:

```text
result = [1, 2, 3, 4, 5]
i = 3
```

The first array is exhausted.

The remaining value in the second array is `6`, so append it:

```text
result = [1, 2, 3, 4, 5, 6]
```

---

## Why Sorted Input Matters

Because both arrays are already sorted, the elements at `i` and `j` are the smallest currently available elements from their respective arrays.

Therefore, comparing only:

```text
first[i] vs second[j]
```

is sufficient. We do not need to compare one element against every element of the other array.

This is what allows the merge to run in linear time.

---

## Edge Cases Tested

### Two normal sorted arrays

```python
[1, 3, 5]
[2, 4, 6]
```

Result:

```text
[1, 2, 3, 4, 5, 6]
```

### Different lengths

```python
[1, 2, 7]
[3, 4, 5, 8]
```

Result:

```text
[1, 2, 3, 4, 5, 7, 8]
```

### First array empty

```python
[]
[1, 2, 3]
```

Result:

```text
[1, 2, 3]
```

### Second array empty

```python
[1, 2, 3]
[]
```

Result:

```text
[1, 2, 3]
```

### Both arrays empty

```python
[]
[]
```

Result:

```text
[]
```

### Duplicate values

```python
[1, 1, 3]
[1, 2, 3]
```

Result:

```text
[1, 1, 1, 2, 3, 3]
```

### Negative values

```python
[-5, -2, 4]
[-3, 0, 6]
```

Result:

```text
[-5, -3, -2, 0, 4, 6]
```

---

## Complexity Analysis

Let `n` be the length of the first array and `m` the length of the second array.

### Time Complexity

```text
O(n + m)
```

Every element from both arrays is processed once.

### Space Complexity

```text
O(n + m)
```

The `result` list contains all elements from both input arrays.

---

## What I Learned

- I learned the **merge pattern** using two pointers.
- I learned that `i` and `j` are indexes into separate arrays.
- I learned to compare only the current elements because both arrays are sorted.
- The smaller current element is always safe to append next.
- The pointer belonging to the selected array moves forward.
- When one array is exhausted, the remaining elements of the other array can be appended directly.
- I learned the difference between replacing a list with `=` and adding an element with `.append()`.
- I learned that equality must be handled so that the pointers continue to progress.
- I reinforced that two pointers can operate on two different input arrays.

---

## Pattern

**Two Pointers — Merge**

General pattern:

```text
first[i] vs second[j]
        ↓
   choose smaller
      ↙     ↘
   first   second
      ↓       ↓
   append  append
      ↓       ↓
    i += 1  j += 1
        ↓
     repeat
        ↓
one array exhausted
        ↓
append remaining elements
```

This pattern is foundational for merge-based algorithms, including the merge step of Merge Sort.

---

## Status

- [x] Problem understood
- [x] Two pointers identified
- [x] Merge logic implemented
- [x] Equality case handled
- [x] Remaining elements handled
- [x] Empty arrays tested
- [x] Different-length arrays tested
- [x] Duplicate values tested
- [x] Negative values tested
- [x] Debugging error identified and fixed
- [x] Complexity analyzed
- [x] Solution verified
