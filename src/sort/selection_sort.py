# coding : UTF-8

def selection_sort(l, stable = True):
    """
    Selection Sort implementation.
    Unstable sort - does not maintains the relative order of equal elements
    Time complexity: O(n^2) - inefficient for large datasets
    Space complexity: O(1) - constant space
    
    Args:
        l (list): List to be sorted.
        stable (bool): If True, use stable sorting method; else unstable.
        
    Returns:
        list: Sorted list.
    """
    n = len(l)

    for idx in range(n):
        # select min
        # find min in l[idx:]
        min_idx = idx
        for i in range(idx + 1, n):
            if l[i] < l[min_idx]:
                min_idx = i

        if stable:
            key = l[min_idx]

            while min_idx > idx:
                l[min_idx] = l[min_idx - 1]
                min_idx -= 1
        
            l[idx] = key
        else:
            # Unstable
            l[idx], l[min_idx] = l[min_idx], l[idx]

    return l

def main():
    l = [3, 1, 2, 5, 4]
    sorted_list = selection_sort(l, stable = True)
    print(sorted_list)

if __name__ == "__main__":
    main()