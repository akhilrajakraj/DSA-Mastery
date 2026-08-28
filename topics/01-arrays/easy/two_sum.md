# Two Sum

## Problem

Given an array of integers and a target value, find two different elements whose sum equals the target.

Return the indexes of the two elements. If no pair exists, return `[-1, -1]`.

Examples:

```text
[2, 7, 11, 15], target = 9  → [0, 1]
[3, 2, 4], target = 6        → [1, 2]
[3, 3], target = 6            → [0, 1]
[1, 2, 3], target = 10        → [-1, -1]
```

---

## My Approach

I used the straightforward **brute-force pair comparison** approach.

Two indexes are used:

- `i` selects the first element.
- `j` checks the elements after `i`.

For every `i`, `j` starts at `i + 1`. This ensures that the same element is not used twice and avoids checking the same pair in reverse order.

For each pair, I check:

```python
numbers[i] + numbers[j] == target
```

If the condition is true, I immediately return the two indexes.

If every possible pair is checked and no pair reaches the target, the function returns:

```python
[-1, -1]
```

---

## Algorithm

1. Start an outer loop over every valid index `i`.
2. Start an inner loop from `i + 1` through the remaining indexes.
3. Add `numbers[i]` and `numbers[j]`.
4. If their sum equals `target`, return `[i, j]`.
5. Continue checking pairs if the sum does not match.
6. If no pair is found after both loops finish, return `[-1, -1]`.

The core structure is:

```python
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            return [i, j]

return [-1, -1]
```

---

## Important Debugging Lesson: Index vs Value

My first attempt used:

```python
for i in numbers:
```

and:

```python
for j in numbers:
```

This made `i` and `j` contain **values**, not indexes.

For example:

```text
numbers = [2, 7, 11, 15]
```

would make `i` become:

```text
2 → 7 → 11 → 15
```

Then using:

```python
numbers[i]
```

could try to access `numbers[15]`, which is outside the valid index range `0` through `3`.

This caused:

```text
IndexError: list index out of range
```

The correction was to explicitly iterate over indexes:

```python
for i in range(len(numbers)):
```

and:

```python
for j in range(i + 1, len(numbers)):
```

This reinforced the distinction:

```text
i              → index
numbers[i]     → value at that index
```

---

## Why Does `j` Start at `i + 1`?

Suppose:

```text
numbers = [2, 7, 11, 15]
```

When `i = 0`, we use:

```text
j = 1, 2, 3
```

So we check:

```text
numbers[0] + numbers[1]
numbers[0] + numbers[2]
numbers[0] + numbers[3]
```

When `i = 1`, we use:

```text
j = 2, 3
```

This avoids checking:

```text
numbers[0] + numbers[0]
```

and also avoids checking the same pair twice:

```text
numbers[0] + numbers[1]
```

and later:

```text
numbers[1] + numbers[0]
```

Therefore `j = i + 1` is important for this brute-force approach.

---

## Dry Run

Input:

```text
numbers = [2, 7, 11, 15]
target = 9
```

Start:

```text
i = 0
```

Then:

```text
j = i + 1 = 1
```

Compare:

```text
numbers[0] + numbers[1]
= 2 + 7
= 9
```

The target is found, so return:

```text
[0, 1]
```

---

## Another Dry Run

Input:

```text
numbers = [3, 2, 4]
target = 6
```

Start:

```text
i = 0
```

Check:

```text
j = 1
3 + 2 = 5
```

Not the target.

Next:

```text
j = 2
3 + 4 = 7
```

Not the target.

Move to:

```text
i = 1
```

Now:

```text
j = 2
2 + 4 = 6
```

Target found.

Return:

```text
[1, 2]
```

---

## Complement Idea

Another way to think about each comparison is to calculate the value needed to reach the target:

```text
target - current value = required value
```

For example:

```text
target = 9
current = 2

9 - 2 = 7
```

So when the current value is `2`, we are looking for `7`.

For:

```text
target = 6
current = 2
```

we need:

```text
6 - 2 = 4
```

This complement idea becomes important when learning the more efficient hash-table solution later.

---

## Edge Cases Tested

### Normal pair

```python
[2, 7, 11, 15], 9
```

Result:

```text
[0, 1]
```

### Pair is not at the beginning

```python
[3, 2, 4], 6
```

Result:

```text
[1, 2]
```

### Equal values at different indexes

```python
[3, 3], 6
```

Result:

```text
[0, 1]
```

The two `3`s are valid because they occupy different indexes.

### No pair exists

```python
[1, 2, 3], 10
```

Result:

```text
[-1, -1]
```

The explicit final return is important. Without it, the function could reach the end and return `None` or accidentally expose stale loop values depending on the implementation.

---

## Complexity Analysis

### Time Complexity

```text
O(n²)
```

The outer loop can examine every element, and the inner loop can examine many of the remaining elements for each outer-loop iteration.

The number of pairs is approximately:

```text
n × (n - 1) / 2
```

which grows quadratically.

### Space Complexity

```text
O(1)
```

Only the loop indexes and a constant amount of additional information are used. No additional data structure grows with the input size.

---

## Why Not `O(n)`?

It initially seemed that the solution might be `O(n)` because we are looking for a target and can calculate a complement:

```text
target - current
```

However, calculating the complement itself is constant time. The brute-force implementation still has to compare many pairs, resulting in `O(n²)` time.

An `O(n)` Two Sum solution is possible using a hash table/dictionary, which will be studied later as part of the roadmap.

---

## What I Learned

- I learned the brute-force solution to Two Sum.
- I reinforced the difference between an **index** and the **value stored at that index**.
- I learned why nested loops lead to `O(n²)` time here.
- I learned why `j` should start at `i + 1`.
- I learned how to prevent using the same array element twice.
- I learned that two different equal values can form a valid pair if they have different indexes.
- I learned the complement idea: `target - current` gives the value we need.
- I learned the importance of an explicit final return when no valid pair exists.
- I encountered and fixed an `IndexError` caused by treating values as indexes.
- I also learned that a straightforward brute-force solution can be useful as a foundation before optimizing it.

---

## Pattern

**Brute Force — Pair Comparison**

General idea:

```text
choose first element
       ↓
check every later element
       ↓
compare the pair
       ↓
return when condition is satisfied
```

This is the basic version of Two Sum. Later, the problem can be optimized using a dictionary/hash table to achieve average `O(n)` time.

---

## Status

- [x] Problem understood
- [x] Brute-force approach identified
- [x] Index-based loops implemented
- [x] `j = i + 1` understood
- [x] Same-element reuse prevented
- [x] No-solution case handled
- [x] Duplicate-value pair tested
- [x] Index vs value error identified and fixed
- [x] Normal pair tested
- [x] Pair later in the array tested
- [x] Complexity analyzed
- [x] Solution verified
