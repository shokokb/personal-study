# Comparison of Array, List, and Python List

## Table

| Feature | Array | List | Python List |
|---------|-------|------|-------------|
| Element Storage | Elements are next to each other in memory | Elements are in nodes | Elements are next to each other in memory, but list can grow |
| Size | Fixed | Can change | Can change |
| Index Access | Fast, O(1) | Slow, O(n) because of linear search | Fast, O(1) |
| Add or Remove Elements | Slow, O(n) | Fast, O(1) | Slow in the middle, O(n) |
| Search for Value | O(n) because of linear search | O(n) | O(n) |
| Memory Use | High | Low | Medium |

## Notes

- **Array**  
  Elements are stored next to each other. Access by index is fast. Changing the size needs copying all elements.

- **List**  
  Elements are in nodes. Adding or removing elements is fast. Access by index is slow because we have to go through nodes.

- **Python List**  
  It is like a dynamic array. Access by index is fast. Adding at the end is usually fast. Inserting or removing in the middle is slow. It can grow when needed.
