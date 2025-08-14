# Python List vs Deque Cheat Sheet

- If you want FIFO or LIFO, deque is the best.
- If you need index access or sorting, use a list.
- If you remove items from the front a lot, always use deque, not a list.

| Operation                | Python List             | Time Complexity | Deque                  | Time Complexity |
|--------------------------|-----------------------|----------------|-----------------------|----------------|
| Access by index          | l[i]                  | O(1)           | N/A                   | N/A            |
| Assign value             | l[i] = x              | O(1)           | N/A                   | N/A            |
| Add to end               | l.append(x)           | Amortized O(1) | dq.append(x)          | O(1)           |
| Add to start             | l.insert(0, x)        | O(n)           | dq.appendleft(x)      | O(1)           |
| Remove from end          | l.pop()               | O(1)           | dq.pop()              | O(1)           |
| Remove from start        | l.pop(0)              | O(n)           | dq.popleft()          | O(1)           |
| Remove by value          | l.remove(x)           | O(n)           | N/A                   | N/A            |
| Check if exists          | x in l                | O(n)           | x in dq               | O(n)           |
| Find first index         | l.index(x)            | O(n)           | N/A                   | N/A            |
| Copy                     | l.copy()              | O(n)           | N/A                   | N/A            |
| Sort                     | l.sort() / sorted(l)  | O(n log n)     | N/A                   | N/A            |
| Reverse                  | l.reverse()           | O(n)           | N/A                   | N/A            |
| Count occurrences        | l.count(x)            | O(n)           | N/A                   | N/A            |
| Clear all elements       | l.clear()             | O(n)           | dq.clear()            | O(n)           |


