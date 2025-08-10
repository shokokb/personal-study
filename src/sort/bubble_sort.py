# coding : UTF-8

# Bubble Sort
# Stable sort - maintains the relative order of equal elements
# Time complexity: O(n^2) - inefficient for large datasets
# Spece complexity: O(1) - constant space
def bubble_sort(l):
    n = len(l)
    for idx in range(n):
        # Elements before index idx (l[:idx]) are already sorted.
        for i in range(n - 1, idx, -1):
            if l[i] < l[i - 1]: # compare l[i - 1] ans l[i] as neighbors
                l[i], l[i - 1] = l[i - 1], l[i] 
    return l

def main():
    l = [4, 3, 1, 5, 2]
    sorted_list = bubble_sort(l)
    print(sorted_list)

if __name__ == "__main__":
    main()