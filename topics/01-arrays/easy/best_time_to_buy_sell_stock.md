# Best Time to Buy and Sell Stock

## Problem

Given an array where each element represents a stock price on a particular day, choose one day to buy and a later day to sell to maximize profit.

If no profitable transaction is possible, return `0`.

Examples:

```text
[7, 1, 5, 3, 6, 4] → 5
[7, 6, 4, 3, 1] → 0
[2, 4, 1] → 2
```

---

## My Approach

I use a single traversal and keep track of two pieces of information:

```text
minimum_price → cheapest price seen so far
max_profit    → best profit found so far
```

For each current price, I calculate the profit that could be made by selling at that price:

```text
profit = current price - minimum price
```

If this profit is greater than the best profit found so far, I update `max_profit`.

If the current price is cheaper than `minimum_price`, I update `minimum_price`.

The important idea is to keep the best information seen so far rather than repeatedly searching the array.

---

## Algorithm

1. Handle an empty array by returning `0`.
2. Initialize `minimum_price` using the first price.
3. Initialize `max_profit` to `0`.
4. Traverse the prices from left to right.
5. Calculate the possible profit using the current price.
6. If the current profit is greater than `max_profit`, update `max_profit`.
7. If the current price is lower than `minimum_price`, update `minimum_price`.
8. Return `max_profit`.

Core idea:

```python
minimum_price = prices[0]
max_profit = 0

for current in prices:
    profit = current - minimum_price

    if profit > max_profit:
        max_profit = profit

    if current < minimum_price:
        minimum_price = current

return max_profit
```

---

## Why Do We Traverse From Left to Right?

The problem requires the buying day to come **before** the selling day.

Therefore, when processing a current day, `minimum_price` represents a price that has already been encountered.

For:

```text
[7, 1, 5, 3, 6, 4]
```

we eventually choose:


```text
buy  → 1
sell → 6
profit = 5
```

We never need to look backwards because the cheapest price seen so far is maintained while moving forward.

This prevents an invalid transaction such as buying after the selling day.

---

## Dry Run

Input:

```text
prices = [7, 1, 5, 3, 6, 4]
```

Initial state:

```text
minimum_price = 7
max_profit = 0
```

### Current = 7

```text
profit = 7 - 7 = 0
```

`max_profit` remains `0`.

### Current = 1

`1` is cheaper than `7`, so:

```text
minimum_price = 1
```

### Current = 5

```text
profit = 5 - 1 = 4
```

Since `4 > 0`:

```text
max_profit = 4
```

### Current = 3

```text
profit = 3 - 1 = 2
```

Since `2 < 4`, the best profit remains:

```text
max_profit = 4
```

### Current = 6

```text
profit = 6 - 1 = 5
```

Since `5 > 4`:

```text
max_profit = 5
```

### Current = 4

```text
profit = 4 - 1 = 3
```

Since `3 < 5`, the best profit remains `5`.

Final result:

```text
5
```

---

## Important Lesson: Keep the Best Value So Far

An early implementation used:

```python
max_profit = current - minimum_price
```

This was incorrect because it replaced the previous best profit with every newly calculated profit.

For example:

```text
profit = 4 → max_profit = 4
profit = 2 → max_profit = 2   ❌
profit = 5 → max_profit = 5
profit = 3 → max_profit = 3   ❌
```

The correct approach is:

```python
profit = current - minimum_price

if profit > max_profit:
    max_profit = profit
```

This means `max_profit` always represents the **best profit found so far**.

This is a reusable DSA pattern:

> Keep track of the best value encountered while traversing the input.

---

## Important Lesson: Price vs Profit

The variable storing the cheapest stock price should be named:

```python
minimum_price
```

not:

```python
minimum_profit
```

because it stores a **price**, while `max_profit` stores the difference between a selling price and a buying price.

Clear variable names make the algorithm easier to understand and debug.

---

## Edge Case: Empty Array

An empty array has no day on which to buy or sell:

```python
[]
```

Therefore the maximum possible profit is:

```text
0
```

The check must happen before accessing `prices[0]`:

```python
if not prices:
    return 0
```

Otherwise:

```python
prices[0]
```

would raise:

```text
IndexError: list index out of range
```

This was encountered during testing and fixed by adding the empty-input check.

---

## Test Cases

### Test 1 — Best profit in the middle

```python
[7, 1, 5, 3, 6, 4]
```

Result:

```text
5
```

### Test 2 — Continuously decreasing

```python
[7, 6, 4, 3, 1]
```

Result:

```text
0
```

### Test 3 — Profit before a later decrease

```python
[2, 4, 1]
```

Result:

```text
2
```

### Test 4 — Continuously increasing

```python
[1, 2, 3, 4, 5]
```

Result:

```text
4
```

### Test 5 — Single day

```python
[5]
```

Result:

```text
0
```

### Test 6 — All prices equal

```python
[3, 3, 3, 3]
```

Result:

```text
0
```

### Test 7 — Best profit near the end

```python
[10, 1, 2, 8, 4, 9]
```

Result:

```text
8
```

### Test 8 — Empty array

```python
[]
```

Result:

```text
0
```

### Test 9 — Two days with profit

```python
[1, 5]
```

Result:

```text
4
```

### Test 10 — Two days without profit

```python
[5, 1]
```

Result:

```text
0
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

The prices are traversed once. Each iteration performs a constant number of operations.

### Space Complexity

```text
O(1)
```

Only a constant number of variables are used:

```text
minimum_price
max_profit
current
profit
```

No additional data structure grows with the input size.

---

## Pattern

**Single-Pass State Tracking — Best Value So Far**

General idea:

```text
current element
      ↓
update useful state
      ↓
calculate current result
      ↓
compare with best result so far
      ↓
keep the best
```

For this problem:

```text
state 1 → minimum price seen so far
state 2 → maximum profit seen so far
```

This pattern is useful whenever the answer can be built by maintaining a small amount of information about everything encountered so far.

---

## What I Learned

- I learned how to solve the stock profit problem in one traversal.
- I learned to maintain the cheapest price seen so far.
- I learned to maintain the best profit found so far instead of overwriting it.
- I reinforced the importance of processing the array from left to right when order matters.
- I learned that the buying day must occur before the selling day.
- I learned the difference between a price and a profit and improved variable naming accordingly.
- I encountered and fixed an `IndexError` caused by accessing index `0` of an empty list.
- I reinforced handling edge cases such as empty arrays, single-element arrays, equal values, and decreasing prices.
- I reinforced the single-pass `O(n)` / constant-space pattern.

---

## Status

- [x] Problem understood
- [x] Minimum price concept understood
- [x] Maximum profit concept understood
- [x] Left-to-right traversal understood
- [x] Best-value-so-far pattern understood
- [x] Empty input handled
- [x] Decreasing prices tested
- [x] Increasing prices tested
- [x] Equal prices tested
- [x] Single-day input tested
- [x] Two-day inputs tested
- [x] Complexity analyzed
- [x] Solution verified
