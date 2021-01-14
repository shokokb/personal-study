class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    print("=== Queue(Class) ===")
    queueObj = Queue()
    # print(queueObj.is_empty())
    queueObj.enqueue("Hello")
    queueObj.enqueue("World")
    queueObj.enqueue("Mr")
    queueObj.enqueue("Japan")
    dequeued = queueObj.dequeue()
    print(dequeued)
    dequeued = queueObj.dequeue()
    print(dequeued)
    dequeued = queueObj.dequeue()
    print(dequeued)
    dequeued = queueObj.dequeue()
    print(dequeued)
    print("\n")
    print("\n")
