# Stack(FIFO)
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        last = len(self.items)-1
        return self.items[last]
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    print("=== Stack(Class) ===")
    text = "Hello"
    stackObj = Stack()
    # print(stackObj.is_empty())
    for c in text:
        stackObj.push(c)
    reversed_text = ""
    for i in range(stackObj.size()):
        reversed_text += stackObj.pop()
    print(reversed_text)
