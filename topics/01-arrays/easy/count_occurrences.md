# Count Occurrences

## Problem

Given an array of numbers and a target value, find how many times the target appears in the array.

### Example

Input:

```python
numbers = [2, 4, 2, 7, 2, 9, 4]
target = 2
```

Output:

```text
3
```

---

## My Approach

I create a `count` variable and initialize it to `0`.

Then I traverse through the entire list. Whenever the current element is equal to the target, I increase the count by `1`.

After checking every element, I return the count.

I must traverse the complete array because I need to know the total number of occurrences, even if the target is found early.

---

## Algorithm

1. Initialize `count` to `0`.
2. Traverse every element in the array.
3. Compare the current element with the target.
4. If they are equal, increase `count` by `1`.
5. After the traversal is complete, return `count`.

---

## Implementation

The implementation is available in `count_occurrences.py`.

Core logic:

```python
count = 0

for n in numbers:
    if n == target:
        count += 1

return count
```

---

## Dry Run

For:

```text
numbers = [2, 4, 2, 7, 2, 9, 4]
target = 2
```

Initially:

```text
count = 0
```

Then:

```text
2 == 2 → count = 1
4 == 2 → no change
2 == 2 → count = 2
7 == 2 → no change
2 == 2 → count = 3
9 == 2 → no change
4 == 2 → no change
```

Final answer:

```text
3
```

---

## Edge Cases

### 1. Target appears multiple times

```python
count_occurrences([2, 4, 2, 7, 2, 9, 4], 2)
```

Output:

```text
3
```

### 2. Target does not appear

```python
count_occurrences([2, 4, 2, 7, 2, 9, 4], 5)
```

Output:

```text
0
```

### 3. Empty list

```python
count_occurrences([], 2)
```

Output:

```text
0
```

An empty list contains the target zero times, so no exception is necessary.

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

Every element must potentially be checked, including when the target appears early, because we need the total number of occurrences.

### Space Complexity

```text
O(1)
```

Only a constant amount of extra space is used for the `count` variable and loop variables.

---

## What I Learned

- I learned how to count occurrences using a simple array traversal.
- I learned the importance of initializing a running count to `0`.
- I learned that this problem must examine the complete array, so even the best case is `O(n)`.
- I learned that an empty list naturally produces a count of `0`.
- I reinforced the difference between a problem where we can stop early and one where we must process the entire input.

---

## Mistakes I Made

Initially, I added an exception for an empty list:

```python
if not numbers:
    raise ValueError("The list is empty")
```

I corrected this after considering what the problem actually asks.

For counting occurrences, an empty list is valid input. The target simply occurs zero times, so the correct result is:

```text
0
```

This is different from finding a maximum or minimum, where an empty list has no maximum or minimum value.

---

## Pattern

**Array Traversal with a Running Count**

The general pattern is:

```text
Initialize count = 0
        ↓
Traverse the array
        ↓
Does current element match?
     ┌──┴──┐
    Yes   No
     ↓     ↓
 count++  continue
     \     /
      \   /
       Continue
          ↓
    Return count
```

This pattern is useful for many problems involving counting, filtering, and frequency-related logic.

---

## Comparison With Previous Problems

```text
Find Maximum
→ may inspect every element
→ O(n)

Find Minimum
→ may inspect every element
→ O(n)

Linear Search
→ can stop when target is found
→ Best O(1), Worst O(n)

Count Occurrences
→ must inspect the entire array
→ Best O(n), Worst O(n)
```

The important lesson is that **early termination depends on what information the problem requires**.

---

## Status

- [x] Problem understood
- [x] Algorithm designed
- [x] Implementation completed
- [x] Multiple occurrences tested
- [x] Target-not-found case tested
- [x] Empty input tested
- [x] Complexity analyzed
- [x] Edge-case behavior corrected
- [x] Solution verified
