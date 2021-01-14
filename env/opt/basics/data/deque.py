# coding: UTF-8

from collections import deque

if __name__ == "__main__":
    # stack(deque)
    print("stack - deque")
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    print("LIFO=", q.pop())

    # queue(deque)
    print("queue - deque")
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    print("FIFO=", q.popleft())