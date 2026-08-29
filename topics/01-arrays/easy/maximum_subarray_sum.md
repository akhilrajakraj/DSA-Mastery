# Maximum Subarray Sum

## Problem

Given an array of integers, find the maximum sum of a **contiguous subarray**.

A contiguous subarray contains elements that are next to each other in the original array. Elements cannot be skipped.

Example:

```text
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

The maximum-sum contiguous subarray is:

```text
[4, -1, 2, 1]
```

Its sum is:

```text
4 + (-1) + 2 + 1 = 6
```

Therefore the answer is `6`.

---

## Understanding Contiguous

Contiguous means **next to each other without skipping elements**.

For:

```text
[1, 2, 3, 4, 5]
```

these are contiguous:

```text
[1, 2]
[2, 3]
[3, 4]
[1, 2, 3]
[3, 4, 5]
```

but these are not:

```text
[1, 3]  # skips 2
[1, 4]  # skips 2 and 3
[2, 5]  # skips 3 and 4
```

A useful way to think about it is that we choose a starting position and an ending position, but everything between them must remain included.

---

## My Approach

The solution uses **Kadane's Algorithm**.

While traversing from left to right, maintain two values:

```text
current_sum → best sum of a contiguous subarray ending at the current position
max_sum     → largest subarray sum found anywhere so far
```

For each current number, there are two choices:

```text
continue the existing subarray:
current_sum + current number

OR

start a new subarray here:
current number
```

We choose whichever is larger.

Then we compare the resulting `current_sum` with `max_sum` and keep the larger value.

---

## Algorithm

1. Handle an empty array by returning `0`.
2. Initialize `current_sum` to the first element.
3. Initialize `max_sum` to the first element.
4. Traverse the remaining elements.
5. Compare `current_sum + current number` with the current number itself.
6. Keep the larger choice as the new `current_sum`.
7. If `current_sum` is greater than `max_sum`, update `max_sum`.
8. Return `max_sum`.

Core logic:

```python
current_sum = numbers[0]
max_sum = numbers[0]

for i in numbers[1:]:
    if current_sum + i > i:
        current_sum = current_sum + i
    else:
        current_sum = i

    if current_sum > max_sum:
        max_sum = current_sum

return max_sum
```

---

## The Central Decision

At every element `i`, ask:

> Should I continue the subarray I already have, or should I start a new subarray at `i`?

Compare:

```text
current_sum + i
```

with:

```text
i
```

If continuing is better:

```python
current_sum = current_sum + i
```

Otherwise:

```python
current_sum = i
```

This is the key insight behind Kadane's Algorithm.

---

## Dry Run

Input:

```text
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

Initial state:

```text
current_sum = -2
max_sum = -2
```

### Current = 1

Two choices:

```text
continue → -2 + 1 = -1
new      → 1
```

Choose `1` because:

```text
1 > -1
```

So:

```text
current_sum = 1
max_sum = 1
```

### Current = -3

```text
continue → 1 + (-3) = -2
new      → -3
```

Choose `-2` because:

```text
-2 > -3
```

So:

```text
current_sum = -2
max_sum = 1
```

### Current = 4

```text
continue → -2 + 4 = 2
new      → 4
```

Choose `4` because:

```text
4 > 2
```

So:

```text
current_sum = 4
```

Since:

```text
4 > 1
```

update:

```text
max_sum = 4
```

### Current = -1

```text
continue → 4 + (-1) = 3
new      → -1
```

Choose `3`.

```text
current_sum = 3
max_sum = 4
```

### Current = 2

```text
continue → 3 + 2 = 5
new      → 2
```

Choose `5`.

```text
current_sum = 5
max_sum = 5
```

### Current = 1

```text
continue → 5 + 1 = 6
new      → 1
```

Choose `6`.

```text
current_sum = 6
max_sum = 6
```

The current contiguous subarray is:

```text
[4, -1, 2, 1]
```

### Current = -5

```text
continue → 6 + (-5) = 1
new      → -5
```

Choose `1`.

```text
current_sum = 1
```

But:

```text
1 < 6
```

so:

```text
max_sum = 6
```

### Current = 4

```text
continue → 1 + 4 = 5
new      → 4
```

Choose `5`.

```text
current_sum = 5
max_sum = 6
```

Final answer:

```text
6
```

---

## Important Lesson: `current_sum` vs `max_sum`

These variables have different jobs.

### `current_sum`

The best sum for a contiguous subarray that ends at the current position.

### `max_sum`

The best sum found anywhere in the array so far.

For example, after reaching the `1` in:

```text
[4, -1, 2, 1]
```

we have:

```text
current_sum = 6
max_sum = 6
```

After `-5`:

```text
current_sum = 1
max_sum = 6
```

The current subarray became worse, but we must not forget the best result we already found.

---

## Important Lesson: Do Not Initialize `max_sum` to `0`

An initial implementation used:

```python
max_sum = 0
```

This fails for arrays containing only negative numbers.

For:

```text
[-3, -2, -5]
```

the correct answer is:

```text
-2
```

but if `max_sum` starts at `0`, no negative value can replace it because:

```text
-2 > 0  # False
```

That would incorrectly produce `0`, even though `0` is not in the array.

The correct initialization is:

```python
current_sum = numbers[0]
max_sum = numbers[0]
```

This also correctly handles a single-element input such as:

```text
[7] → 7
```

---

## Empty Array Edge Case

Before accessing:

```python
numbers[0]
```

we check:

```python
if not numbers:
    return 0
```

Otherwise an empty array would cause:

```text
IndexError: list index out of range
```

For this implementation, an empty input returns `0`.

---

## Test Cases

```python
# Test 1: Standard case
print(best_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# Test 2: All positive / mostly positive
print(best_sum([5, 4, -1, 7, 8]))

# Test 3: All negative
print(best_sum([-3, -2, -5]))

# Test 4: Single element
print(best_sum([7]))

# Test 5: Two positive elements
print(best_sum([1, 2]))

# Test 6: Positive section surrounded by negatives
print(best_sum([-5, 4, -1, 7, -8]))

# Test 7: Maximum occurs at the beginning
print(best_sum([5, 4, -10, 2]))

# Test 8: Maximum occurs at the end
print(best_sum([-5, -2, 3, 4]))

# Test 9: Contains zeros
print(best_sum([0, -1, 0, 5, -2, 3]))

# Test 10: Mixed values
print(best_sum([2, -1, 2, 3, -9, 4, 5]))

# Test 11: Empty array
print(best_sum([]))
```

Expected output:

```text
6
23
-2
7
3
10
9
7
6
9
0
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

The array is traversed once. Each element requires only a constant number of comparisons and arithmetic operations.

### Space Complexity

```text
O(1)
```

Only a constant number of variables are maintained. No additional structure grows with the input size.

---

## Pattern

**Kadane's Algorithm — Running Best Sum**

General idea:

```text
current element
      ↓
continue previous subarray OR start here
      ↓
choose the larger sum
      ↓
compare against global best
      ↓
keep the best result
```

The deeper pattern is **local decision + global best**:

```text
current_sum → best choice ending here
max_sum     → best choice found overall
```

This allows us to solve a problem that appears to require considering many subarrays in just one pass.

---

## What I Learned

- I learned what a contiguous subarray means: elements must be adjacent and cannot be skipped.
- I learned to distinguish a contiguous subarray from an arbitrary selection of elements.
- I learned the central decision in Kadane's Algorithm: continue the current subarray or start a new one.
- I learned the difference between `current_sum` and `max_sum`.
- I learned why `max_sum` must not start at `0` when negative answers are possible.
- I learned to initialize the maximum using an actual element from the input.
- I handled empty arrays before accessing `numbers[0]`.
- I reinforced the single-pass `O(n)` and constant-space `O(1)` pattern.
- I learned the reusable pattern of making a local best decision while maintaining a global best result.

---

## Status

- [x] Contiguous subarray understood
- [x] Valid and invalid contiguous examples understood
- [x] Continue-vs-restart decision understood
- [x] `current_sum` understood
- [x] `max_sum` understood
- [x] All-negative case handled
- [x] Single-element case handled
- [x] Empty input handled
- [x] Mixed values tested
- [x] Increasing values tested
- [x] Decreasing values tested
- [x] Zero values tested
- [x] Complexity analyzed
- [x] Solution verified
