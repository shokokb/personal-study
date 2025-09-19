# Python Interview Prep TODO List

---

## 1. Must-Have Skills (should be able to write reflexively)

### Basic Control Structures
- [ o ] Conditionals (`if`, `elif`, `else`)
- [ o ] Loops (`for` + `range` / direct iteration)
- [ o ] Loops (`while`)
- [ o ] Usage of `break` / `continue`

### Basic Data Structure Operations
- [ o ] `list`: creation, `append`, `pop`, slicing
- [ o ] `dict`: creation, access, update, iteration
- [ o ] `set`: creation, addition, set operations (`&`, `|`, `-`)
- [ o ] `tuple` (including unpacking)

### Built-in Functions
- [ o ] `len()`, `min()`, `max()`, `sum()`, `sorted()`
- [ ] `enumerate()`, `zip()`, `map()`, `filter()`
- [ o ] `any()`, `all()`

### Comprehensions
- [ o ] List comprehension (e.g., `[x*2 for x in arr if x > 0]`)
- [ ] Dict comprehension (e.g., `{k: v for k, v in data if condition}`)

### Function Definition
- [ ] Arguments (default values, variable length `*args`, `**kwargs`)
- [ o ] `return`

### Algorithm Tricks
- [ ] `sorted(..., key=..., reverse=True)`
- [ ] `heapq` (priority queue)
- [ ] Binary search (`bisect`)

---

## 2. Nice-to-Have Skills (bonus points)

### Python 3.10+ Features
- [ o ] `match-case` (pattern matching)
- [ ] Structural pattern matching (partial matches, unpacking)

### Enumerations
- [ ] Using `Enum` class for constant management

### Decorators
- [ o ] `@staticmethod`, `@classmethod`
- [ ] Custom decorators

### Generators
- [ ] Lazy evaluation with `yield`

### `functools` / `itertools`
- [ ] `lru_cache`
- [ ] `permutations`, `combinations`, `groupby`

### Type Hints
- [ ] `list[int]`, `dict[str, int]`
- [ ] `Optional`, `Union` (from `typing`)

### Context Managers
- [ ] `with` statement (file handling, resource management)

---

## 3. Algorithms (LeetCode Core)

### Data Structure Basics
- [ o ] Stack (LIFO) – `append`, `pop`, valid parentheses
- [ o ] Queue (FIFO) – `collections.deque`
- [ ] Priority Queue – `heapq`
- [ ] Hash Map / Hash Set usage

### Search & Traversal
- [ o ] Depth-First Search (DFS) – recursion & stack
- [ o ] Breadth-First Search (BFS) – queue
- [ ] Binary Search (iterative & recursive)
- [ ] Sliding Window technique

### Dynamic Programming (DP)
- [ o ] 1D DP (e.g., **House Robber**, Fibonacci)
- [ o ] 2D DP (e.g., **Longest Common Subsequence**, Edit Distance)
- [ ] Knapsack pattern
- [ ] State compression (space optimization)

### Graphs
- [ ] Adjacency list representation
- [ ] Topological Sort
- [ ] Union-Find (Disjoint Set Union, DSU)

### Other Core Patterns
- [ o ] Two Pointers (e.g., sorted array, linked list)
- [ ] Prefix Sum
- [ ] Backtracking (e.g., subsets, permutations)
- [ ] Greedy algorithms (e.g., interval scheduling, stock problems)

---

## Summary
- **Must-have skills**: Python basics (syntax, data structures, built-ins).  
- **Nice-to-have skills**: Pythonic features (`match-case`, `Enum`, `decorators`).  
- **Algorithms**: Master stack/queue, DFS/BFS, DP, and greedy — they appear frequently in interviews.
