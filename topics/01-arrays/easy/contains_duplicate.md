# Contains Duplicate

## Problem

Given an array of values, determine whether **any value appears more than once**.

Return:

```text
True  → a duplicate exists
False → no duplicate exists
```

Examples:

```text
[1, 2, 3, 1] → True
[1, 2, 3, 4] → False
```

---

## My Approach

Use a `set` called `seen` to remember values that have already appeared.

Traverse the array from left to right.

For each number:

```text
Is number already in seen?
```

If yes, a duplicate has been found, so immediately return `True`.

If no, add the number to `seen` and continue.

If the entire array is processed without finding a duplicate, return `False`.

Core logic:

```python
seen = set()

for number in numbers:
    if number in seen:
        return True

    seen.add(number)

return False
```

---

## Algorithm

1. Create an empty `seen` set.
2. Traverse every number in the input array.
3. Check whether the current number already exists in `seen`.
4. If it exists, return `True` immediately.
5. Otherwise add it to `seen`.
6. If the loop finishes, return `False`.

---

## Dry Run

Input:

```text
[4, 7, 2, 9, 7, 3]
```

Initial:

```text
seen = {}
```

### Current = 4

```text
4 in seen? NO
```

Add:

```text
seen = {4}
```

### Current = 7

```text
7 in seen? NO
```

Add:

```text
seen = {4, 7}
```

### Current = 2

```text
2 in seen? NO
```

Add:

```text
seen = {4, 7, 2}
```

### Current = 9

```text
9 in seen? NO
```

Add:

```text
seen = {4, 7, 2, 9}
```

### Current = 7

```text
7 in seen? YES
```

A duplicate has been found.

Return immediately:

```text
True
```

The final `3` does not need to be inspected because the answer is already known.

---

## Important Lesson: Early Termination

Once a duplicate is found, there is no reason to continue traversing the array.

For:

```text
[4, 7, 2, 9, 7, 3]
```

we stop at the second `7`:

```text
4 → add
7 → add
2 → add
9 → add
7 → duplicate → return True
```

This is called **early termination**.

It can make the actual runtime much smaller than the worst-case runtime when a duplicate appears early.

---

## Important Lesson: Set for Membership Checking

A set is useful here because we repeatedly ask:

```python
number in seen
```

Set membership is average `O(1)`.

We therefore avoid scanning all previously encountered values every time.

This is the same set-based membership pattern used in the previous Intersection problem, but the goal is simpler here:

```text
Intersection → find matching values
Contains Duplicate → detect whether a value has appeared before
```

---

## Boolean Return Value

This problem asks a yes/no question, so the function should return a boolean:

```text
True
False
```

For an empty array:

```text
[]
```

there are no duplicate values, so the correct result is:

```text
False
```

An earlier test produced `0` for the empty array. Although Python treats `0` as false-like in conditions, it is not the intended return type for this problem.

The correct implementation returns:

```python
return False
```

This reinforces an important habit:

> Match the return value to what the problem is asking for.

---

## Test Cases

```python
# Test 1: Duplicate at the end
print(contains_duplicate([1, 2, 3, 1]))

# Test 2: No duplicates
print(contains_duplicate([1, 2, 3, 4]))

# Test 3: Duplicate appears consecutively
print(contains_duplicate([1, 2, 2, 3]))

# Test 4: All elements are duplicates
print(contains_duplicate([5, 5, 5, 5]))

# Test 5: Single element
print(contains_duplicate([7]))

# Test 6: Empty array
print(contains_duplicate([]))

# Test 7: Negative numbers with duplicate
print(contains_duplicate([-1, -2, -3, -1]))

# Test 8: Duplicate at the beginning
print(contains_duplicate([4, 4, 2, 7, 9]))

# Test 9: Larger array with no duplicates
print(contains_duplicate([1, 3, 5, 7, 9, 11, 13, 15]))

# Test 10: Zero as a duplicate
print(contains_duplicate([0, 1, 2, 0, 4]))
```

Expected output:

```text
True
False
True
True
False
False
True
True
False
True
```

All ten test cases were verified successfully after correcting the empty-array return value from `0` to `False`.

---

## Complexity Analysis

Let `n` be the number of elements in the input array.

### Time Complexity

```text
O(n)
```

In the worst case, every element must be inspected. Set membership is average `O(1)`.

The best case can terminate very early if a duplicate appears near the beginning, but the worst-case complexity remains `O(n)`.

### Space Complexity

```text
O(n)
```

In the worst case, every element is unique, so all `n` values are stored in `seen`.

---

## Pattern

**Seen Set / Duplicate Detection**

General pattern:

```text
Create seen set
      ↓
Traverse input
      ↓
Already seen?
   ↙       ↘
 YES       NO
  ↓         ↓
return    add to seen
 True        ↓
          continue
             ↓
        loop finishes
             ↓
        return False
```

This is a fundamental pattern for problems involving:

- duplicate detection
- repeated values
- membership checks
- uniqueness
- detecting whether something has appeared previously

---

## Connection to Previous Problems

### Problem 16 — Intersection

We used a set to answer:

```text
Does this value exist in another collection?
```

### Problem 17 — Contains Duplicate

We use a set to answer:

```text
Have I already encountered this value?
```

The underlying technique is the same:

```text
SET + FAST MEMBERSHIP CHECK
```

Recognizing this repeated pattern is part of the mastery roadmap.

---

## What I Learned

- I learned to use a `seen` set for duplicate detection.
- I learned to check membership before adding a value.
- I learned that encountering an already-seen value means a duplicate exists.
- I learned to return `True` immediately when a duplicate is found.
- I learned the concept of early termination.
- I reinforced average `O(1)` set membership checking.
- I learned that an empty array should return `False` because no duplicate exists.
- I reinforced matching the function's return type to the question being asked.
- I connected this problem to the set-based membership pattern from Intersection of Two Arrays.
- I reinforced `O(n)` time and `O(n)` auxiliary space complexity.

---

## Status

- [x] Problem understood
- [x] `seen` set understood
- [x] Membership checking understood
- [x] Duplicate detection understood
- [x] Early termination understood
- [x] Boolean return value understood
- [x] Empty input handled
- [x] Duplicate at beginning tested
- [x] Duplicate at end tested
- [x] Consecutive duplicates tested
- [x] Negative numbers tested
- [x] Zero tested
- [x] No-duplicate case tested
- [x] Complexity analyzed
- [x] Solution verified
