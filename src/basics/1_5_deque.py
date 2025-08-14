from collections import deque

def main():
    q = deque([0, 1, 2, 3])
    q.append(5)         # O(1)
    item = q.popleft()  # O(1)
    print(item)
    item = q.pop()      # O(1)
    print(item)

if __name__ == "__main__":
    main()