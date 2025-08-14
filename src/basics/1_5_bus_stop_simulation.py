from collections import deque

def bus_stop_simulation():
    queue = deque()

    # 人が並ぶ
    queue.append("Alice")
    queue.append("Bob")
    queue.append("Charlie")
    print("Queue at bus stop:", list(queue))

    # バス到着、順番に乗せる
    while queue:
        person = queue.popleft()
        print(person, "got on the bus. Remaining queue:", list(queue))

if __name__ == "__main__":
    bus_stop_simulation()
