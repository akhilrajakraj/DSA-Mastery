# Python for DSA — Variables, Objects, and References

## What I learned

I learned that Python variables are better understood as **names/references to objects**, rather than simple boxes containing values.

```python
x = 10
```

Here, `x` refers to an integer object containing `10`.

### Assignment and references

When I write:

```python
x = 10
y = x
```

both names refer to the same integer object. If I later do:

```python
x = 20
```

`y` remains `10` because I reassigned `x`; I did not mutate the integer object.

### Mutable vs immutable

I learned the distinction between mutation and reassignment.

Common immutable types include:

- `int`
- `float`
- `bool`
- `str`
- `tuple`

Lists are mutable.

For example:

```python
a = [1, 2, 3]
b = a

a.append(4)
```

Both `a` and `b` now observe:

```text
[1, 2, 3, 4]
```

because both names refer to the same list object.

But:

```python
a = [1, 2, 3]
b = a.copy()

a.append(4)
```

produces separate outer list objects, so `b` remains `[1, 2, 3]`.

### Function arguments and mutation

If a function receives a list and mutates it, the caller can observe the change:

```python
def add_item(numbers):
    numbers.append(100)

numbers = [1, 2, 3]
add_item(numbers)
```

After the call, `numbers` is `[1, 2, 3, 100]`.

### Shallow copy

`list.copy()` creates a shallow copy. For nested lists, the outer list is new but nested mutable objects may still be shared. I will study shallow vs deep copying in more detail when it becomes relevant to recursion, backtracking, and graph problems.

## DSA mental model

When I see:

```python
b = a
```

I should think:

> `b` is another name referring to the same object.

When I see:

```python
b = a.copy()
```

for a list, I should think:

> `b` is a new outer list containing the same elements.

The key distinction is:

```text
Reassignment → changes what a name refers to
Mutation     → changes the object itself
```

This matters in DSA because unintended mutation can change input arrays/lists and can cause subtle bugs in recursion, backtracking, graphs, and dynamic programming.
