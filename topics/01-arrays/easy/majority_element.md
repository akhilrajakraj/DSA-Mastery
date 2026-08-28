# Majority Element

## Problem

Given an array of integers, find the element that appears **more than `n / 2` times**, where `n` is the length of the array.

For this version of the problem, a majority element is guaranteed to exist.

Examples:

```text
[3, 2, 3] → 3
[2, 2, 1, 1, 1, 2, 2] → 2
[5, 5, 5, 2, 2] → 5
```

---

## My Initial Thinking

The straightforward approach would be to pick each element and count how many times it appears in the array. If its count is greater than `n / 2`, it is the majority element.

However, repeatedly scanning the entire array for every candidate would take `O(n²)` time.

The better approach is to use a **dictionary** to keep track of frequencies while traversing the array once.

---

## Key Idea

Use a dictionary with:

```text
number → number of occurrences
```

For example, for:

```python
numbers = [2, 2, 1, 1, 1, 2, 2]
```

we build:

```text
2 → 4
1 → 3
```

Since:

```text
4 > 7 / 2
```

`2` is the majority element.

---

## Algorithm

1. Create an empty dictionary called `counts`.
2. Traverse every number in the array.
3. If the number already exists in `counts`, increase its count.
4. Otherwise, create the key with a count of `1`.
5. Traverse the dictionary's key-value pairs.
6. If a number's count is greater than `n / 2`, return that number.
7. The problem guarantees that such an element exists.

Counting logic:

```python
counts = {}

for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1
```

Majority check:

```python
for number, count in counts.items():
    if count > len(numbers) / 2:
        return number
```

---

## Understanding `n / 2`

The condition is:

```text
count > n / 2
```

For:

```python
numbers = [3, 2, 3]
```

we have:

```text
n = 3
n / 2 = 1.5
```

The count must therefore be greater than `1.5`. Since counts are whole numbers, at least `2` occurrences are required.

`3` occurs twice:

```text
2 > 1.5 → True
```

Therefore `3` is the majority element.

---

## Can Two Elements Both Be Majority Elements?

No.

A majority element must appear **more than half** of the array.

If two different values both appeared more than half, their combined occurrences would exceed the length of the array.

For example:

```text
[1, 1, 2, 2]
```

Each value occurs twice, but:

```text
2 > 4 / 2 → False
```

So neither is a majority element.

Our problem guarantees that a majority element exists, so this no-majority situation does not need to be handled by the final implementation.

---

## Dry Run

Input:

```text
numbers = [3, 2, 3]
```

Start:

```text
counts = {}
```

First number `3`:

```text
3 is not in counts
```

Create it:

```text
{3: 1}
```

Next number `2`:

```text
2 is not in counts
```

Create it:

```text
{3: 1, 2: 1}
```

Next number `3`:

```text
3 is already in counts
```

Increase its count:

```text
{3: 2, 2: 1}
```

Now:

```text
n = 3
n / 2 = 1.5
```

Check `3`:

```text
2 > 1.5 → True
```

Return:

```text
3
```

---

## Important Python Lesson: Dictionary Counting

A dictionary stores key-value associations.

For this problem:

```text
key   → number
value → frequency
```

A dictionary does not use `append()` like a list.

For a new number:

```python
counts[number] = 1
```

For an existing number:

```python
counts[number] += 1
```

This is a reusable **frequency-counting pattern** that will appear in many other DSA problems.

---

## Important Debugging Lesson

During implementation, I initially wrote:

```python
for number, counts in counts.items():
```

This reused the name `counts` for both the dictionary and the individual frequency. Although the code could work, it is confusing and makes the meaning of the variable change.

The clearer version is:

```python
for number, count in counts.items():
```

where:

```text
counts → complete dictionary
count  → frequency of the current number
```

I also initially had a fallback:

```python
return counts
```

but because the problem guarantees a majority element, the function should simply return the majority number when it is found.

---

## Test Cases

### Test 1

```python
[3, 2, 3]
```

Result:

```text
3
```

### Test 2

```python
[2, 2, 1, 1, 1, 2, 2]
```

Result:

```text
2
```

### Test 3

```python
[5, 5, 5, 2, 2]
```

Result:

```text
5
```

### Test 4

```python
[1]
```

Result:

```text
1
```

### Test 5

```python
[4, 4, 2, 4, 3, 4, 4]
```

Result:

```text
4
```

### Test 6

```python
[-1, -1, -1, 2, 3]
```

Result:

```text
-1
```

### Test 7

```python
[1, 2, 2, 2, 2]
```

Result:

```text
2
```

### Test 8

```python
[7, 7, 3, 3, 7, 2, 7, 7, 4]
```

Result:

```text
7
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

The array is traversed once to build the frequency dictionary. The dictionary is then traversed to find the majority element. In the worst case, this is another `O(n)` operation.

Therefore:

```text
O(n) + O(n) = O(n)
```

### Space Complexity

```text
O(n)
```

In the worst case, every element can be different, so the dictionary can contain `n` different keys.

---

## Comparison With Brute Force

### Brute Force

```text
Time  = O(n²)
Space = O(1)
```

Repeatedly count occurrences by scanning the array for every candidate.

### Dictionary Approach

```text
Time  = O(n)
Space = O(n)
```

Store frequencies while traversing the array.

The dictionary approach trades additional memory for significantly better time complexity.

---

## What I Learned

- I learned how to use a dictionary for frequency counting.
- I reinforced the key-value relationship: `number → count`.
- I learned that `dict[key] = value` is used to create or update dictionary entries, rather than `append()`.
- I learned the majority condition is strictly `count > n / 2`.
- I learned why two different elements cannot both be majority elements.
- I compared the brute-force `O(n²)` solution with the dictionary-based `O(n)` solution.
- I reinforced the difference between a dictionary and the values stored inside it.
- I learned to use clear variable names such as `counts` for the dictionary and `count` for an individual frequency.
- I reinforced testing with duplicates, negative values, a single element, and a majority appearing in different positions.

---

## Pattern

**Hash Table / Dictionary — Frequency Counting**

General pattern:

```text
input element
     ↓
exists in dictionary?
   ↙          ↘
 yes           no
  ↓             ↓
increase       create
count          count = 1
     ↓
frequency information
```

This pattern is fundamental for problems involving frequencies, duplicates, counting, grouping, and lookup.

---

## Status

- [x] Problem understood
- [x] Brute-force approach understood
- [x] Dictionary approach identified
- [x] Frequency counting implemented
- [x] Majority condition implemented
- [x] Dictionary iteration understood
- [x] Variable naming cleaned up
- [x] No-majority behavior understood
- [x] Normal majority tested
- [x] Duplicate values tested
- [x] Negative values tested
- [x] Single-element input tested
- [x] Complexity analyzed
- [x] Solution verified
