# Python for DSA — Tuples

## What I learned

A tuple is an ordered collection like a list, but it is **immutable**.

```python
point = (10, 20)
```

The key comparison is:

```text
list  → ordered, mutable
tuple → ordered, immutable
```

## Indexing

Tuple indexing is typically `O(1)`:

```python
point = (10, 20, 30)
value = point[1]
```

## Traversal and membership

Traversing a tuple is `O(n)` because every element may need to be visited.

Membership such as:

```python
30 in point
```

is generally `O(n)` in the worst case because the tuple may need to be scanned.

Immutability does not make linear searching constant-time.

## Tuple unpacking

A very useful DSA pattern is:

```python
point = (10, 20)
x, y = point
```

which gives:

```text
x = 10
y = 20
```

This appears frequently with coordinates, intervals, graph edges, and value/index pairs.

## Tuples for coordinates

For a grid position, I can represent a cell as:

```python
position = (row, col)
```

For example:

```python
position = (2, 4)
```

The tuple communicates that the two values form one fixed coordinate pair.

## Tuples with sets

A tuple whose elements are hashable can be stored in a set:

```python
visited = set()
visited.add((2, 4))

print((2, 4) in visited)  # True
```

This is an important future DSA pattern for grid traversal:

```python
visited = set()
visited.add((row, col))
```

The tuple represents the coordinate and the set tracks visited coordinates efficiently.

## List vs tuple

| Feature | List | Tuple |
|---|---|---|
| Ordered | Yes | Yes |
| Indexing | `O(1)` | `O(1)` |
| Mutable | Yes | No |
| `append()` | Yes | No |
| `pop()` | Yes | No |
| Typical use | Dynamic collection | Fixed structure |
| Set/dict compatibility | Not hashable | Hashable when contents are hashable |

## DSA mental model

I should choose a tuple when the values form a fixed structure that should not be mutated, such as `(row, col)`, `(start, end)`, or `(value, index)`.

The important reason to choose a tuple is its immutability and fixed structure, not simply the claim that tuples are faster than lists.
