# Python for DSA — Dictionaries

## What I learned

A Python dictionary stores relationships as:

```text
key → value
```

Example:

```python
scores = {
    "Akhil": 85,
    "Rahul": 91
}
```

Dictionaries are hash-table based, so key lookup, insertion, and deletion are typically `O(1)` on average.

## Dictionary vs set

A set mainly answers:

> Have I seen this value?

A dictionary answers:

> What information is associated with this key?

```text
set  → value / existence
 dict → key → value
```

## Basic operations

```python
scores["Akhil"] = 90       # insert/update
value = scores["Akhil"]   # lookup
```

Typical average complexity:

```text
lookup    → O(1)
insertion → O(1)
update    → O(1)
delete    → O(1)
```

Accessing a missing key with `scores[key]` raises `KeyError`. `scores.get(key, default)` can safely return a default instead.

## Frequency counting

A major DSA pattern is:

```text
item → frequency
```

For example:

```python
numbers = [1, 2, 2, 3, 3, 3]
frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1
```

The result is:

```text
1 → 1
2 → 2
3 → 3
```

If there are `n` input elements:

```text
Time  = O(n) average
Space = O(n)
```

The dictionary lookup is not another `O(n)` loop; it is typically `O(1)` average.

## Value → index mapping

When I repeatedly need the index associated with a value, I can build a dictionary:

```python
index_map = {}

for i, number in enumerate(numbers):
    index_map[number] = i
```

For:

```text
[10, 20, 30, 40, 50]
```

this represents:

```text
10 → 0
20 → 1
30 → 2
40 → 3
50 → 4
```

Then `index_map[40]` is typically `O(1)` average.

This pattern is important for problems such as Two Sum.

## Counter

For frequency counting, Python provides:

```python
from collections import Counter

frequency = Counter(numbers)
```

`Counter` behaves like a specialized dictionary for counts.

For:

```python
words = ["cat", "dog", "cat", "bird", "dog", "cat"]
frequency = Counter(words)
```

we get conceptually:

```text
cat  → 3
dog  → 2
bird → 1
```

A missing `Counter` key returns `0`:

```python
frequency["horse"]  # 0
```

Creating a `Counter` from `n` input items takes approximately `O(n)` time.

## defaultdict

`defaultdict` automatically creates a default value for a missing key.

```python
from collections import defaultdict

graph = defaultdict(list)

graph["A"].append("B")
graph["A"].append("C")
graph["B"].append("D")
```

The conceptual structure is:

```text
A → [B, C]
B → [D]
```

Accessing `graph["C"]` creates and returns a new empty list:

```python
graph["C"]  # []
```

This pattern is especially useful for adjacency lists when we study graphs.

## Dictionary keys must be hashable

Dictionary keys must be hashable. Immutable values such as integers, strings, and suitable tuples can be keys:

```python
grid = {
    (2, 4): "visited"
}
```

A mutable list cannot be a dictionary key.

## Iteration

Iterating through all dictionary entries takes `O(n)` because each entry is visited.

```python
for key, value in scores.items():
    print(key, value)
```

## DSA mental model

I should choose a dictionary when I need a fast mapping such as:

```text
number    → frequency
number    → index
character → count
word      → information
node      → neighbors
```

The distinction I learned is:

```text
SET       → "Have I seen this?"
DICT      → "What information belongs to this?"
COUNTER   → "How many times did I see this?"
DEFAULTDICT → "What collection belongs to this key?"
```

## DSA checkpoint

I can now explain dictionary hashing at a high level, average `O(1)` key lookup, frequency counting, value-to-index mapping, `Counter`, `defaultdict`, and the time-space tradeoff involved in using hash-based structures.
