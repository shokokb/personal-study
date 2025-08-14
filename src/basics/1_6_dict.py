# coding : UTF-8

# In a list, finding an item needs checking each one, so it takes O(n) time.
# In a dictionary, finding by key is very fast, almost O(1), 
# because it uses a hash table.
# But finding by value is still O(n).

def linear_search_arr(arr, name):
    for i in range(len(arr)):
        if arr[i][0] == name:
            return arr[i][0], arr[i][1]
    return None, None

def linear_search_hashtable(ht, name):
    for k in ht:
        if ht[k] == name:
            return k, ht[k]
    return None, None

def main():
    # in case of array
    arr = [
        ("Joe", "M"),
        ("Sue", "F"),
        ("Dan", "M"),
        ("Nell", "F"),
        ("Ally", "F"),
        ("Bob", "M")
    ]
    name, gender = linear_search_arr(arr, "Sue")
    print(name, gender) # O(n) linear search

    # in case of hashtable
    ht = {
        "Joe" : "M",
        "Sue" : "F",
        "Dan" : "M",
        "Nell": "F",
        "Ally": "F",
        "Bob" : "M"
    }
    print(ht["Sue"]) # Almost O(1), O(n) when a lot of collisions occur

if __name__ == "__main__":
    main()