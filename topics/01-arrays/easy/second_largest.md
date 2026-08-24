# Second Largest Distinct Element

## Problem

Find the second-largest **distinct** element in an array. If there are not at least two distinct values, raise a `ValueError`.

### Example

```python
[10, 5, 8, 20, 15]  # 15
```

## My Approach

I maintain two values while traversing the array: `largest` and `second_largest`. Both start as `None` so the algorithm works with negative numbers without assuming that `0` is a valid starting value.

For every `current` value:

1. If there is no largest yet, make `current` the largest.
2. If `current > largest`, the old largest becomes the second largest and `current` becomes the new largest.
3. Otherwise, if `current < largest` and `current` is greater than the current second largest, update `second_largest`.
4. If `current == largest`, ignore it because the second-largest value must be distinct.
5. After the traversal, raise an error if no second-largest value exists.

No sorting or set is required.

## Algorithm

```text
largest = None
second_largest = None

Traverse every current value:
    if largest is None:
        largest = current
    elif current > largest:
        second_largest = largest
        largest = current
    elif current < largest and
         (second_largest is None or current > second_largest):
        second_largest = current

After the loop:
    if second_largest is None:
        raise ValueError
    return second_largest
```

## Dry Run

For `[10, 5, 8, 20, 15]`:

```text
10 → largest=10, second=None
5  → largest=10, second=5
8  → largest=10, second=8
20 → largest=20, second=10
15 → largest=20, second=15
```

Answer: `15`.

For `[20, 10, 20, 5]`, the second `20` is ignored because it is equal to `largest`. The answer is `10`.

## Edge Cases

```text
[10, 5, 8, 20, 15]       → 15
[20, 10, 20, 5]          → 10
[-5, -10, -2, -8]        → -5
[20, 15, 10, 5]           → 15
[5, 10, 15, 20]           → 15
[10, 15, 5, 15, 20, 3]   → 15
[10]                      → ValueError
[10, 10, 10, 10]          → ValueError
[]                        → ValueError
```

## Complexity Analysis

### Time

`O(n)` — the array is traversed exactly once.

### Space

`O(1)` — only `largest` and `second_largest` are maintained.

This is better than sorting first, which would require `O(n log n)` time.

## What I Learned

- How to maintain multiple pieces of state during one traversal.
- When a new largest appears, the old largest becomes the second largest.
- Duplicate largest values must be ignored for a distinct-second-largest problem.
- `None` is safer than initializing with `0`, especially for negative numbers.
- A correct single-pass algorithm can avoid sorting and extra data structures.

## Mistakes I Made

- I initially passed `largest` and `second_largest` as function parameters even though they are internal state.
- I initially set `second_largest = current` when a new largest appeared. The correct update is `second_largest = largest` followed by `largest = current`.
- I initially made overlapping `elif` conditions, making a later condition unreachable.
- I initially checked for the missing second-largest value inside the loop. The final validation belongs after the traversal.

## Pattern

**Maintaining Multiple State Variables During Array Traversal**

```text
Initialize state
     ↓
Traverse once
     ↓
Compare current with state
     ↓
Update state
     ↓
Validate final state
     ↓
Return result
```

## Implementation

See [`second_largest.py`](./second_largest.py).

## Status

- [x] Algorithm designed
- [x] Single-pass implementation completed
- [x] Duplicates tested
- [x] Negative numbers tested
- [x] Invalid inputs tested
- [x] Complexity analyzed
- [x] Solution verified
