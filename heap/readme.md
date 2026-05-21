stack and queue based on arrival time
heap is based on priority. when priority same then considers arrival time.

# Heap

## What is a Heap?

A Heap is a special type of binary tree used to efficiently:
- get minimum/maximum element
- insert elements
- delete minimum/maximum

Uses:
- Priority Queue
- Dijkstra Algorithm
- Prim’s Algorithm
- Heap Sort
- Scheduling systems

---

# Types of Heap

## Min Heap

Rule:

\[
\text{Parent} \le \text{Children}
\]

Example:

```text
        1
      /   \
     3     2
    / \   /
   7   6 5
```

---

## Max Heap

Rule:

\[
\text{Parent} \ge \text{Children}
\]

Example:

```text
        9
      /   \
     7     8
    / \   /
   3   2 5
```

---

# Heap Property

Heap is NOT fully sorted.

Only parent-child ordering exists.

Min Heap:

```text
parent <= children
```

Max Heap:

```text
parent >= children
```

---

# Complete Binary Tree

Heap must always be a complete binary tree.

Meaning:
- all levels completely filled
- except last level
- last level filled left to right

Valid:

```text
        1
      /   \
     2     3
    / \
   4   5
```

Invalid:

```text
        1
      /   \
     2     3
      \
       5
```

---

# Array Representation

Tree:

```text
        1
      /   \
     3     2
    / \   /
   7   6 5
```

Array:

```text
[1, 3, 2, 7, 6, 5]
```

---

# Heap Formulas

Suppose current index = `i`

Left Child:

\[
2i + 1
\]

Right Child:

\[
2i + 2
\]

Parent:

\[
\left\lfloor \frac{i-1}{2} \right\rfloor
\]

Example:

```text
Index:  0 1 2 3 4 5
Array: [1,3,2,7,6,5]
```

---

# Insertion

## Step 1
Insert at last position.

## Step 2
Heapify Up (Bubble Up).

If child < parent:
- swap
- move upward
- continue until heap property restored

Complexity:

\[
O(\log n)
\]

---

# Deletion

Usually delete root.

## Step 1
Remove root.

## Step 2
Move last element to root.

## Step 3
Heapify Down.

Complexity:

\[
O(\log n)
\]

---

# Heapify

## Heapify Up
Used after insertion.

## Heapify Down
Used after deletion.

---

# Heap vs Sorted Array

| Operation | Heap | Sorted Array |
|---|---|---|
| Get min/max | O(1) | O(1) |
| Insert | O(log n) | O(n) |
| Delete min/max | O(log n) | O(n) |

---

# Heap vs BST

| Feature | Heap | BST |
|---|---|---|
| Root min/max | ✅ | ❌ |
| Fully sorted | ❌ | ✅ |
| Search arbitrary element | O(n) | O(log n) |
| Complete tree | ✅ | ❌ |

---

# Python Heap

```python
import heapq

heapq.heappush(heap, x)
heapq.heappop(heap)
heap[0]
```

---

# Max Heap in Python

```python
heapq.heappush(heap, -x)
```

---

# Dry Run — Min Heap Insertions

Insertions:

```text
[3, 2, 1, 5, 6, 4]
```

| Step | Tree | Array | Action |
|---|---|---|---|
| Insert 3 | ```text\n3\n``` | `[3]` | No swap |
| Insert 2 | ```text\n  3\n /\n2\n``` | `[3,2]` | `2 < 3` → swap |
| After Heapify | ```text\n  2\n /\n3\n``` | `[2,3]` | Heap restored |
| Insert 1 | ```text\n    2\n   / \\\n  3   1\n``` | `[2,3,1]` | `1 < 2` → swap |
| After Heapify | ```text\n    1\n   / \\\n  3   2\n``` | `[1,3,2]` | Heap restored |
| Insert 5 | ```text\n      1\n     / \\\n    3   2\n   /\n  5\n``` | `[1,3,2,5]` | No swap |
| Insert 6 | ```text\n      1\n     / \\\n    3   2\n   / \\\n  5   6\n``` | `[1,3,2,5,6]` | No swap |
| Insert 4 | ```text\n       1\n     /   \\\n    3     2\n   / \\   /\n  5   6 4\n``` | `[1,3,2,5,6,4]` | No swap |

---

# Final Min Heap

```text
       1
     /   \
    3     2
   / \   /
  5   6 4
```

Array:

```text
[1,3,2,5,6,4]
```

---

# Heapify Up Rule

```python
while child < parent:
    swap(child, parent)
    move upward
```
