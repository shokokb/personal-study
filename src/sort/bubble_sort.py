# coding : UTF-8

def bubble_sort(l):
    for idx in range(len(l)):
        # Elements before index idx (l[:idx]) are already sorted.
        for i in range(len(l) - 1, idx, -1):
            if l[i] < l[i - 1]: # compare l[i - 1] ans l[i] as neighbors
                l[i], l[i - 1] = l[i - 1], l[i] 
    return l

def main():
    l = [4, 3, 1, 5, 2]
    sorted_list = bubble_sort(l)
    print(sorted_list)

if __name__ == "__main__":
    main()