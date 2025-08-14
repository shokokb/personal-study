# coding : UTF-8

from collections import deque

def main():
    queue = deque()
    queue.append("Blue")    # O(1)
    queue.append("Green")   # O(1)
    queue.append("Red")     # O(1)
    item = queue.popleft()  # O(1)
    print(item)
    item = queue.popleft()      # O(1)
    print(item)
    item = queue.popleft()      # O(1)
    print(item)

if __name__ == "__main__":
    main()