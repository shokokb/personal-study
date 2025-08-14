# coding : UTF-8

def main():
    l = [0, 1, 2, 3]
    print("Initial list:", l)
    
    # 1. Index access
    print("Index access l[1]:", l[1], "O(1)")

    # 2. Assign
    l[1] = "*"
    print("After assign l[1] = '*':", l, "O(1)")

    # 3. Push / Append at end
    l.append(4)  
    print("After append 4:", l, "Amortized O(1)")

    # 4. Pop from end
    n = l.pop()  
    print("Pop from end:", n, "->", l, "O(1)")

    # 5. Pop from middle
    n = l.pop(1)  
    print("Pop from middle index 1:", n, "->", l, "O(n)")

    # 6. Insert in middle
    l.insert(1, 1)  
    print("After insert 1 at index 1:", l, "O(n)")

    # 7. Remove by value
    # l.append(1) # first node of x = 1
    # print(l)
    v = 1
    l.remove(v)
    print(f"After remove first node of {1}:", l, "O(n)")
    l.insert(1, 1)
    # Remove all items of target value
    # target = 1
    # l = [x for x in l if x != target]

    # 8. Index
    try:
        n = 2
        i = l.index(2)
        print(f"First index of {n}:", i, "O(n)")
    except ValueError:
        print("ValueError")
    # Find all indices of target value
    # target = 1
    # indices = [i for i, x in enumerate(l) if x == target]

    # 9. In
    x = 3
    print("Check if 3 in list:", x in l, "O(n)")

    # 10. Expand List
    l += [4, 5, 6]
    print("After expanding list:", l, "O(k)")

    # 11. Copy
    new_list = l.copy()
    print("After copying list:", new_list, "O(n)")
    print("Old List is not the same with New List :", l is new_list)

    # 12. Sort List
    unsorted_list = [1, 4, 2, 5, 3]
    l = unsorted_list.copy()
    l.sort()
    print("After sorting list:", l, "O(n log n)")
    print("After sorting list:", sorted(unsorted_list))

    # 13. Reverse List
    l.reverse()
    print("After reversing list:", l, "O(n)")

    # 14. count
    print("After counting list:", l.count(3), "O(n)")

    # 15. clear
    l.clear()
    print("After clearing list:", l, "O(n)")

    # 16. Slice
    l = [0, 1, 2, 3, 4, 5]
    print(l[1:3])
    print(l[2:])
    print(l[:])
    print(l[:-3])

    # 17. Peek
    print(l[-1])

    # 18. Is Empty
    def is_emply(l):
        return len(l) == 0
    print(l, "is empty:", is_emply(l))

    # 19. Size
    print("Size:", len(l))

    # 20. Dequeue
    item = l.pop(0)
    print("Dequeue", item, l)
         
if __name__ == "__main__":
    main()
