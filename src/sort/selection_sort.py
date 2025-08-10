# coding : UTF-8

# Selection Sort
# Uhstable sort - does not maintains the relative order of equal elements
# Time complexity: O(n^2) - inefficient for large datasets
# Spece complexity: O(1) - constant space
def selection_sort(l):
    n = len(l)

    for idx in range(n):
        # select min
        # find min in l[idx:]
        min_idx = idx
        for i in range(idx + 1, n):
            if l[i] < l[min_idx]:
                min_idx = i

        # Unstable
        # l[idx], l[min_idx] = l[min_idx], l[idx]

        # Stable 
        key = l[min_idx]

        while min_idx > idx:
            l[min_idx] = l[min_idx - 1]
            min_idx -= 1
        
        l[idx] = key
    return l

def main():
    l = [3, 1, 2, 5, 4]
    sorted_list = selection_sort(l)
    print(sorted_list)

if __name__ == "__main__":
    main()