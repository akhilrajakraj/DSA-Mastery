# Big-O Basics

## Purpose

Big-O describes how an algorithm's resource usage grows as the input size `n` grows. In this stage, we focus primarily on asymptotic growth rather than exact runtime.

## Core Complexities

### O(1) — Constant

The amount of work stays essentially constant as `n` grows.

Example:

```python
value = numbers[0]
```

Time: `O(1)`

### O(log n) — Logarithmic

The problem size is repeatedly reduced by a constant factor, commonly by half or by doubling a search/index value.

Example:

```python
i = 1
while i < n:
    i *= 2
```

The values grow as `1, 2, 4, 8, ...`, so the loop takes `O(log n)` iterations.

### O(n) — Linear

The algorithm may process each input element once.

```python
for number in numbers:
    print(number)
```

Time: `O(n)`

### O(n log n)

Often appears when `n` work is performed across `log n` levels.

Example pattern:

```text
O(n) * O(log n) = O(n log n)
```

### O(n²) — Quadratic

Work grows approximately as `n * n`.

```python
for x in numbers:
    for y in numbers:
        print(x, y)
```

Time: `O(n²)`

### O(2ⁿ) — Exponential

Common when each element creates two independent choices, such as generating all subsets.

```text
2 choices per element × n elements → 2ⁿ possibilities
```

### O(n!) — Factorial

Common when generating all permutations of `n` elements.

## Rules for Analyzing Code

### Sequential operations → Add

```text
O(n) + O(n) = O(2n) = O(n)
```

### Nested operations → Multiply

```text
O(n) * O(n) = O(n²)
```

### Keep the dominant term

```text
O(n²) + O(n) → O(n²)
```

### Ignore constant factors

```text
O(2n) → O(n)
O(10n) → O(n)
```

### Constant loops remain constant

```python
for i in range(10):
    pass
```

This is `O(1)`, regardless of input size.

### Doubling/halving often means logarithmic

```python
i *= 2
```

or

```python
i //= 2
```

usually indicates `O(log n)` when the loop continues until it reaches a boundary based on `n`.

## Sequential vs Nested Example

Sequential:

```python
for i in range(n):
    pass

for j in range(n):
    pass
```

`O(n) + O(n) = O(n)`.

Nested:

```python
for i in range(n):
    for j in range(n):
        pass
```

`O(n) * O(n) = O(n²)`.

## Logarithmic Nested Loops

Consider:

```python
i = 1
while i < n:
    j = 1
    while j < n:
        j *= 2
    i *= 2
```

`i` and `j` are separate variables. The assignment `j = 1` resets `j` at every outer iteration. The inner loop does not change `i`.

The outer loop takes `O(log n)` iterations because `i` doubles. For every outer iteration, `j` is reset and takes `O(log n)` iterations because it also doubles.

Therefore:

```text
O(log n) * O(log n) = O((log n)²)
```

## Time vs Space

Time and space are separate measurements.

```python
total = 0
for number in numbers:
    total += number
```

Time: `O(n)`

Extra space: `O(1)`

By contrast:

```python
result = []
for number in numbers:
    result.append(number * 2)
```

Time: `O(n)`

Extra space: `O(n)` because the result grows with the input.

## Best, Average, and Worst Case

For a linear search:

```python
for number in numbers:
    if number == target:
        return True
return False
```

- Best case: `O(1)` — target is first.
- Worst case: `O(n)` — target is last or absent.
- Average case is generally `O(n)` under the usual assumptions.

## Important Mental Models

- `O(1)` → fixed amount of work.
- `O(log n)` → repeatedly reduce the problem by a constant factor.
- `O(n)` → may inspect the whole input.
- `O(n log n)` → linear work across logarithmic levels.
- `O(n²)` → pair each item with many/all other items.
- `O(2ⁿ)` → two choices per element.
- `O(n!)` → permutations/arrangements.

## Mastery Checkpoint

Before moving on, you should be able to:

- distinguish sequential and nested operations;
- identify constant loops;
- recognize doubling/halving loops as logarithmic;
- calculate common combinations such as `O(n log n)` and `O((log n)²)`;
- simplify constants and non-dominant terms;
- distinguish time complexity from extra space complexity;
- explain best and worst case for simple algorithms.
