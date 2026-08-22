# Python for DSA — Sets

## What I learned

A Python `set` is an unordered collection of **unique** elements. It is mainly useful when I need uniqueness and fast membership checks.

```python
numbers = {10, 20, 30, 40}
```

Unlike a list, a set does not provide normal positional indexing:

```python
numbers[0]  # invalid for a set
```

## Why sets are useful in DSA

The most important operation is membership:

```python
if value in seen:
    ...
```

For a hash-based set, membership is typically:

```text
O(1) average
```

This is much faster asymptotically than membership in a list, which is typically `O(n)`.

## Hashing mental model

A set uses hashing to help locate values. Conceptually:

```text
value → hash(value) → storage location → lookup
```

This avoids scanning every element in the normal case.

Hash collisions can occur when different values map to the same location. A set handles collisions internally, which is why the technically correct statement is **O(1) average-case lookup**, not guaranteed O(1) in every theoretical situation.

## Duplicates are removed

```python
numbers = {1, 2, 2, 3, 3, 3}
```

becomes conceptually:

```text
{1, 2, 3}
```

Therefore:

```python
len(numbers)
```

returns `3`.

Converting a list to a set is useful for deduplication:

```python
unique = set(numbers)
```

This takes `O(n)` time in the typical case because the input elements must be processed.

## Important operations

| Operation | Typical average complexity |
|---|---:|
| `x in s` | `O(1)` |
| `s.add(x)` | `O(1)` |
| `s.remove(x)` | `O(1)` |
| `s.discard(x)` | `O(1)` |
| `len(s)` | `O(1)` |
| Iterate through set | `O(n)` |
| `set(iterable)` | `O(n)` average |

`remove(x)` raises `KeyError` when the element is absent, while `discard(x)` does nothing when it is absent.

## Duplicate detection pattern

A common DSA pattern is:

```python
def has_duplicate(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True
        seen.add(number)

    return False
```

Complexity:

```text
Time  = O(n) average
Space = O(n)
```

The loop is `O(n)`, but `number in seen` is `O(1)` average, so the loop does not become `O(n^2)`. The set may store up to `n` values, so extra space is `O(n)`.

## Time-space tradeoff

A duplicate-checking solution using nested loops can use:

```text
Time  = O(n²)
Space = O(1)
```

Using a set changes this to approximately:

```text
Time  = O(n)
Space = O(n)
```

I am using extra memory to reduce the running time. This is a fundamental **time-space tradeoff** in algorithm design.

## Sets and tuples for grid problems

A tuple containing hashable values can be a set element:

```python
visited = set()
visited.add((row, col))
```

For example:

```python
visited.add((2, 4))
print((2, 4) in visited)  # True
```

This gives a powerful future pattern for grid BFS/DFS and visited-state tracking:

```text
(row, col) → tuple → set → fast membership
```

## Set operations

Given:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

Common operations include:

```python
a & b   # intersection → {3, 4}
a | b   # union        → {1, 2, 3, 4, 5, 6}
a - b   # difference   → {1, 2}
```

## Hashable elements

Set elements must be hashable. Immutable values such as integers and suitable tuples can be stored in sets:

```python
visited.add((2, 4))
```

A mutable list cannot be a set element:

```python
visited.add([2, 4])  # invalid
```

## Choosing between list, tuple, and set

```text
Need ordered/indexed data?          → list
Need a fixed structured value?      → tuple
Need unique values + fast lookup?   → set
```

The key DSA question is not simply "Which structure is better?" It is:

> **Which operation needs to be fast for this problem?**

## Example: common values

```python
def find_common(a, b):
    seen = set(a)
    result = []

    for number in b:
        if number in seen:
            result.append(number)

    return result
```

If `a` and `b` each have `n` elements:

```text
set(a)                  → O(n)
loop through b          → O(n)
each set membership     → O(1) average
------------------------------------------
Total time              → O(n)
Extra space             → O(n)
```

## DSA checkpoint

I should now be able to explain:

- why sets remove duplicates;
- why sets do not provide normal indexing;
- why membership is O(1) average;
- the basic hashing mental model;
- what a hash collision means;
- why duplicate detection can improve from O(n²) to O(n) using a set;
- why that improvement costs O(n) extra space;
- why tuples are useful as set elements for coordinates;
- when a set is a better choice than a list or tuple.
