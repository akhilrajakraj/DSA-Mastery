# Python for DSA — Lists

## What I learned

A Python `list` is an ordered, mutable collection and is one of the most important structures I will use throughout DSA.

```python
numbers = [10, 20, 30, 40]
```

Lists use zero-based indexing:

```text
index:  0   1   2   3
value: 10  20  30  40
```

## Important operations and complexity

| Operation | Typical complexity |
|---|---:|
| `arr[i]` | `O(1)` |
| `arr.append(x)` | `O(1)` amortized |
| `arr.pop()` | `O(1)` |
| `arr.pop(0)` | `O(n)` |
| `arr.insert(0, x)` | `O(n)` |
| `x in arr` | `O(n)` |
| Traverse the list | `O(n)` |

## Why indexing is O(1)

Index access such as:

```python
numbers[3]
```

can directly access the element at the requested position, rather than scanning from the beginning.

## Why operations at the front are O(n)

For:

```python
numbers.insert(0, 5)
```

existing elements may need to shift to make room:

```text
[10, 20, 30, 40]
        ↓ shift
[5, 10, 20, 30, 40]
```

Similarly, `pop(0)` can require the remaining elements to shift left. With `n` elements, this can require `O(n)` work.

## Why append is O(1) amortized

Python lists are dynamic arrays. Most appends can place the new element into available capacity, so an individual append is usually constant time.

Occasionally, the underlying storage becomes full. Python then needs to allocate larger storage and move existing elements. That individual resize can cost `O(n)`, but over a long sequence of appends the average cost per append is `O(1)` amortized.

## Searching

For:

```python
x in numbers
```

Python may scan elements sequentially. Best case can be `O(1)`, but the usual worst-case complexity is `O(n)`.

## DSA mental model

I should not assume that every nested loop is `O(n^2)`. I need to look at what each loop actually does and use the operation complexities of the underlying Python data structures.

For lists, a useful mental model is:

```text
Fast:
arr[i]          → O(1)
arr.append(x)   → O(1) amortized
arr.pop()       → O(1)

Potentially expensive:
arr.insert(0,x)  → O(n)
arr.pop(0)      → O(n)
x in arr        → O(n)
```

This is especially important when choosing a data structure. If I repeatedly need efficient operations at the front, I should consider `collections.deque` rather than repeatedly using `list.pop(0)`.
