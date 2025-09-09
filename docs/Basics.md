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

# List vs Tuple vs Set vs Dictionary
| Collection   | Order | Duplicates | Index Access | Search   | Add       | Remove    | Notes |
|--------------|-------|-----------|--------------|----------|-----------|-----------|-------|
| Tuple        | Yes   | Yes       | O(1)         | O(n)     | ✕         | ✕         | Immutable, read-only |
| List         | Yes   | Yes       | O(1)         | O(n)     | O(1)*     | O(n)      | Mutable, ordered, slow to remove from start |
| Set          | No    | No        | ✕            | O(1) avg | O(1) avg  | O(1) avg  | Mutable, unordered, no duplicates, fast search/add/remove |
| Dictionary   | No    | No        | ✕ (keys yes) | O(1) avg | O(1) avg  | O(1) avg  | Keys are fast to access (hash table), values can be anything |

*List append is “Amortized O(1)”

| Collection   | Example Code | Explanation | Time Complexity |
|--------------|--------------|-------------|----------------|
| Tuple        | `fruits = ("Apple", "Grape", "Orange")`<br>`print(fruits[0])` | Ordered, can have duplicates, **cannot add/remove** items | Access by index: O(1), Search: O(n) |
| List         | `fruits = ["Apple", "Grape", "Orange"]`<br>`fruits.append("Kiwi")`<br>`fruits.pop(1)` | Ordered, can have duplicates, **can add/remove**, fast at end, slow at start/middle | Access by index: O(1), Append: Amortized O(1), Insert/Pop at start/middle: O(n), Search: O(n) |
| Set          | `fruits = {"Apple", "Grape", "Orange"}`<br>`fruits.add("Kiwi")`<br>`fruits.remove("Grape")` | Unordered, no duplicates, fast search/add/remove, **cannot use index** | Add/Remove/Search: O(1) average, O(n) worst case |
| Dictionary   | `ht = {"Joe":"M", "Sue":"F"}`<br>`ht["Sue"]`<br>`ht["Dan"] = "M"` | Key-value pairs, keys are unique, fast lookup by key, unordered, can add/remove items | Access by key/Add/Remove: O(1) average, O(n) worst case, Search by value: O(n) |

## 💡 Quick Tips:

- Tuple → Fixed list, safe from changes.
- List → Ordered, can change, duplicates allowed.
- Set → Unique items only, fast check if item exists.
- Dictionary → Map keys to values, fast key lookup, search by value is slow.

# Python Data Structures 

| Data Structure | Image | Usage / Features | Time Complexity |
|----------------|-------|-----------------|----------------|
| **List** | 📚 Boxes lined up on a shelf | Keep items in order, access by index | `l[i]` O(1), `append` O(1), `pop(0)` O(n) |
| **Tuple** | 📦 Box with a lid (cannot open) | Immutable, for fixed data | Read O(1) |
| **Set** | 🃏 A pile of cards with no duplicates | Quickly check if an item exists | `x in s` O(1) |
| **Dict** | 📇 Notebook with names and phone numbers | Fast lookup by key | `ht[key]` O(1) |
| **Stack** | 🍽 Plates stacked on top of each other | LIFO (Last In, First Out) | `push/pop` O(1) |
| **Queue** | 🛒 Line at the checkout | FIFO (First In, First Out) | `append/popleft` O(1) (use deque) |

## 💡 Example Images
- **List** → Boxes lined up on a shelf  
- **Tuple** → Box with a lid (cannot open)  
- **Set** → Pile of cards with no duplicates  
- **Dict** → Pulling out a name and phone number card  
- **Stack** → Plates stacked on top of each other  
- **Queue** → People in line at a checkout  

