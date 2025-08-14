# coding : UTF-8
import time

def linear_search_arr(arr, name):
    for i in range(len(arr)):
        if arr[i][0] == name:
            return arr[i][0], arr[i][1]
    return None, None

def linear_search_hashtable_by_name(ht, name):
    # O(n) because we iterate all keys instead of direct access
    for k in ht:
        if k == name:
            return k, ht[k]
    return None, None

def main():
    # Small example
    arr = [
        ("Joe", "M"), ("Sue", "F"), ("Dan", "M"),
        ("Nell", "F"), ("Ally", "F"), ("Bob", "M")
    ]
    ht = dict(arr)

    print("Array search:", linear_search_arr(arr, "Sue"))
    print("Hashtable direct access:", ht["Sue"])
    print("Hashtable search by name:", linear_search_hashtable_by_name(ht, "Sue"))

    # Benchmark with large data
    N = 1_000_000
    big_list = [(f"name{i}", i) for i in range(N)]
    big_dict = dict(big_list)
    target_key = f"name{N//2}"

    # List search O(n)
    start = time.time()
    linear_search_arr(big_list, target_key)
    end = time.time()
    print(f"List linear search: {end - start:.6f} seconds")

    # Dict direct access O(1)
    start = time.time()
    _ = big_dict[target_key]
    end = time.time()
    print(f"Dict direct access: {end - start:.6f} seconds")

    # Dict linear search O(n)
    start = time.time()
    linear_search_hashtable_by_name(big_dict, target_key)
    end = time.time()
    print(f"Dict linear search by name: {end - start:.6f} seconds")

if __name__ == "__main__":
    main()
