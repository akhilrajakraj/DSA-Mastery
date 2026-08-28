# Find the Missing Number

## Problem

Given an array containing `n` distinct numbers taken from the range `0` to `n`, find the one missing number.

Examples:

```text
[3, 0, 1] → 2
[0, 1] → 2
[9, 6, 4, 2, 3, 5, 7, 0, 1] → 8
```

---

## My Approach

I used the mathematical property of the sum of consecutive numbers.

First, I find `n` from the length of the array. The complete range is `0` through `n`, so it contains `n + 1` values.

I calculate:

```text
expected sum = sum of all numbers from 0 to n
```

using the formula:

```python
n * (n + 1) // 2
```

Then I calculate the sum of the numbers actually present in the array.

Finally:

```text
missing number = expected sum - actual sum
```

The missing value is the difference because every other number in the complete range is present in the array.

---

## Algorithm

1. Find `n` using `len(numbers)`.
2. Calculate the expected sum from `0` to `n`.
3. Traverse the array and calculate the actual sum.
4. Subtract the actual sum from the expected sum.
5. Return the difference.

---

## Example

For:

```python
numbers = [3, 0, 1]
```

The length is:

```text
n = 3
```

The complete range is:

```text
0, 1, 2, 3
```

Expected sum:

```text
3 × 4 / 2 = 6
```

Actual sum:

```text
3 + 0 + 1 = 4
```

Therefore:

```text
6 - 4 = 2
```

So the missing number is:

```text
2
```

---

## Important Distinction

Three related ideas must not be confused:

```text
n + 1       → number of values in the complete range
0 → n       → the actual range of values
n(n + 1)/2  → the sum of those values
```

For `n = 2`:

```text
n + 1 = 3
range = 0, 1, 2
sum = 2 × 3 / 2 = 3
```

---

## Implementation

The implementation is available in `find_missing_number.py`.

The core approach is:

```python
n = len(numbers)
expected_sum = n * (n + 1) // 2

actual_sum = 0
for number in numbers:
    actual_sum += number

return expected_sum - actual_sum
```

A clearer variable name such as `actual_sum` or `total` is preferred over `sum`, because `sum` is also a Python built-in function.

---

## Edge Cases Tested

### Missing value in the middle

```python
[3, 0, 1]
```

Result:

```text
2
```

### Missing value at the end

```python
[0, 1]
```

Result:

```text
2
```

### Larger unsorted input

```python
[9, 6, 4, 2, 3, 5, 7, 0, 1]
```

Result:

```text
8
```

### Single-element array containing zero

```python
[0]
```

Result:

```text
1
```

### Single-element array containing one

```python
[1]
```

Result:

```text
0
```

### Empty array

```python
[]
```

Result:

```text
0
```

For an empty array, `n = 0`, so the complete range is just `0`. The expected sum and actual sum are both `0`, producing the missing number `0`.

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

The array is traversed once to calculate the actual sum. The expected sum calculation takes constant time.

### Space Complexity

```text
O(1)
```

Only a constant number of variables are used. No additional data structure grows with the input size.

---

## What I Learned

- I learned how to use a mathematical property to solve an array problem without an additional data structure.
- `n` is the length of the input array, while the complete range contains `n + 1` values because it includes both `0` and `n`.
- The sum formula for `0` through `n` is `n * (n + 1) // 2`.
- Subtracting the actual sum from the expected sum reveals the missing number.
- I learned to distinguish between the number of values, the range of values, and their sum.
- I reinforced that an unsorted input does not matter for this approach because only the total sum is needed.
- I learned that using `sum` as a variable shadows Python's built-in `sum()` function, so a name such as `actual_sum` is clearer.
- I reinforced boundary-case testing with empty and single-element arrays.

---

## Pattern

**Mathematical Invariant — Expected Total vs Actual Total**

General idea:

```text
expected complete total
          -
actual total
          =
missing contribution
```

This approach is useful when the input is expected to contain a complete mathematical range or collection except for one missing value, and the constraints allow the use of the corresponding mathematical invariant.

---

## Status

- [x] Problem understood
- [x] Range `0 → n` understood
- [x] Expected sum formula understood
- [x] Actual sum calculated
- [x] Missing value derived by subtraction
- [x] Empty input tested
- [x] Single-element inputs tested
- [x] Larger input tested
- [x] Unsorted input tested
- [x] Complexity analyzed
- [x] Solution verified
