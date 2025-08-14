# coding : UTF-8

def main():
    queue = []

    queue.append("Blue")    # Almost O(1)
    print(queue)

    queue.append("Green")   # Almost O(1)
    print(queue)

    queue.append("Red")     # Almost O(1)
    print(queue)

    item = queue.pop(0)     # O(n)
    print(item, queue)

    item = queue.pop(0)     # O(n)
    print(item, queue)

    item = queue.pop(0)     # O(n)
    print(item, queue)

if __name__ == "__main__":
    main()