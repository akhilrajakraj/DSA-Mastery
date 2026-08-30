# Intersection of Two Arrays

## Problem

Given two arrays, find the **unique elements that appear in both arrays**.

For example:

```text
A = [1, 2, 3, 4]
B = [3, 4, 5, 6]
```

The intersection is:

```text
[3, 4]
```

If a value occurs multiple times, it should appear only once in the result.

---

## My Approach

The main idea is to use a **set** for fast membership checking and another set to prevent duplicate results.

I first convert the second array into a set:

```python
second_set = set(second)
```

Then I traverse the first array one element at a time.

For every `current` value, I check:

```text
1. Is current present in second_set?
2. Is current NOT already in seen?
```

If both are true, the value belongs to the intersection and has not been added before.

Then:

```python
seen.add(current)
result.append(current)
```

Finally, return `result`.

---

## Algorithm

1. Convert `second` into a set called `second_set`.
2. Create an empty `seen` set.
3. Create an empty `result` list.
4. Traverse every value in `first`.
5. Check whether the current value exists in `second_set`.
6. Check whether the current value is not already in `seen`.
7. If both conditions are true, add the value to `seen` and `result`.
8. Return `result`.

Core logic:

```python
second_set = set(second)
seen = set()
result = []

for current in first:
    if current in second_set and current not in seen:
        seen.add(current)
        result.append(current)

return result
```

---

## Why Use a Set for the Second Array?

Without a set, we could compare every element of `first` against every element of `second`.

With:

```python
second_set = set(second)
```

membership checking is average `O(1)`.

So instead of repeatedly scanning `second`, we can ask directly:

```python
current in second_set
```

This makes the lookup much more efficient.

---

## Why Do We Need `seen`?

Consider:

```text
A = [1, 2, 2, 2, 3]
B = [2, 4]
```

The value `2` appears several times in `A`, but the problem asks for unique intersection values.

Without `seen`, we could produce:

```text
[2, 2, 2]
```

With `seen`:

```text
first 2 → found in B → not seen → add
second 2 → found in B → already seen → skip
third 2 → found in B → already seen → skip
```

Final result:

```text
[2]
```

An important refinement from the implementation was realizing that we do **not** need to check both `seen` and `result` for membership. `seen` is sufficient for tracking whether a value has already been added.

---

## Dry Run

Input:

```text
A = [4, 9, 5, 9]
B = [9, 4, 9, 8, 4]
```

First create:

```text
second_set = {9, 4, 8}
seen = {}
result = []
```

### Current = 4

```text
4 in second_set? YES
4 in seen? NO
```

Add it:

```text
seen = {4}
result = [4]
```

### Current = 9

```text
9 in second_set? YES
9 in seen? NO
```

Add it:

```text
seen = {4, 9}
result = [4, 9]
```

### Current = 5

```text
5 in second_set? NO
```

Skip it.

### Current = 9

```text
9 in second_set? YES
9 in seen? YES
```

Skip it because it was already added.

Final:

```text
result = [4, 9]
```

---

## Important Lesson: Membership + Uniqueness

This problem combines two useful set patterns:

### 1. Fast membership checking

```python
current in second_set
```

A set gives average `O(1)` membership checking.

### 2. Uniqueness tracking

```python
current not in seen
```

The `seen` set prevents duplicate values from entering the result.

Together:

```text
set → fast lookup
set → duplicate prevention
list → preserve the result sequence
```

---

## Result Order

Because we traverse `first`, the result follows the order in which unique common values are encountered in the first array.

For example:

```python
intersection([4, 9, 5], [9, 4])
```

produces:

```text
[4, 9]
```

The implementation does not sort the result.

---

## Test Cases

```python
# Test 1: Basic intersection
print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))

# Test 2: Duplicate values
print(intersection([1, 2, 2, 2, 3], [2, 4]))

# Test 3: No common elements
print(intersection([1, 2, 3], [4, 5, 6]))

# Test 4: All elements common
print(intersection([1, 2, 3], [1, 2, 3]))

# Test 5: Duplicates in both arrays
print(intersection([4, 9, 5, 9], [9, 4, 9, 8, 4]))

# Test 6: First array empty
print(intersection([], [1, 2, 3]))

# Test 7: Second array empty
print(intersection([1, 2, 3], []))

# Test 8: Both arrays empty
print(intersection([], []))

# Test 9: Single common element
print(intersection([1], [1]))

# Test 10: Negative numbers
print(intersection([-5, -3, 0, 2], [-3, 0, 4]))
```

Expected output:

```text
[3, 4]
[2]
[]
[1, 2, 3]
[4, 9]
[]
[]
[]
[1]
[-3, 0]
```

All ten test cases were verified successfully.

---

## Complexity Analysis

Let:

```text
n = length of first
m = length of second
k = number of unique intersection values
```

### Time Complexity

Creating `second_set` takes:

```text
O(m)
```

Traversing `first` takes:

```text
O(n)
```

Average set membership operations are `O(1)`.

Therefore:

```text
Time = O(n + m)
```

### Space Complexity

`second_set` requires `O(m)` space.

`seen` and `result` require space proportional to the number of unique values stored. In the worst case this is `O(n)`.

Therefore:

```text
Space = O(n + m)
```

---

## Pattern

**Set-Based Membership + Uniqueness Tracking**

General pattern:

```text
Build a set from one input
          ↓
Traverse the other input
          ↓
Check membership in the set
          ↓
Check whether already seen
          ↓
Add unique matches to result
```

This pattern is useful when a problem asks whether values from one collection exist in another and duplicate results should be avoided.

---

## What I Learned

- I learned to use a set for fast membership checking.
- I learned to use a separate `seen` set to prevent duplicate intersection values.
- I learned that checking `seen` is sufficient; I do not need to check the result list for membership as well.
- I reinforced the idea that sets provide average `O(1)` membership lookup.
- I learned that traversing the first array determines the order of the result in this implementation.
- I practiced handling duplicates in both arrays.
- I tested empty arrays, no intersection, complete intersection, single values, and negative numbers.
- I reinforced the pattern of combining membership checking with uniqueness tracking.

---

## Status

- [x] Problem understood
- [x] Set-based lookup understood
- [x] `seen` uniqueness tracking understood
- [x] Duplicate handling understood
- [x] Result ordering understood
- [x] Empty inputs tested
- [x] No-intersection case tested
- [x] Negative numbers tested
- [x] Complexity analyzed
- [x] Solution verified
