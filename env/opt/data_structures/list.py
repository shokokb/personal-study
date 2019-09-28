# import numpy as np

# Stack
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

### List ###
print("=== List ===")
list = ["Yamada", "Takahashi", "Hashimoto"]
print(list)
print("\n")
# ["Yamada", "Takahashi", "Hashimoto"]


### Array ###
# 標準機能出ない為、見送り
# import matplotlib.pyplot as plt
# date = np.array(range(1,31))
# temp = np.array([
#     22,25,23,26,21,22,22,
#     17,20,19,22,26,21,19,
#     22,20,15,16,22,26,26,
#     28,19,21,23,25,22,26,
#     26,26])
 
# plt.plot(date, temp)
# plt.xlim([1,31])
# plt.ylim([0,40])
# plt.show()

# print("=== Stack ===")
# stack = ["Hello", "World", "Miss"]
# print("=== push(first-in) ===")
# stack.append("Japan")
# print(stack)
# print("=== pop(first-out) ===")
# poped = stack.pop()
# print(stack)
# print(poped)
# print("\n")

print("=== Stack(Class) ===")
text = "Hello"
stackObj = Stack()
print(stackObj.is_empty())
for c in text:
    stackObj.push(c)
reversed_text = ""
for i in range(len(stackObj.items)):
    reversed_text += stackObj.pop()
print(reversed_text)

print("=== Queue(Class) ===")
queueObj = Queue()
print(queueObj.is_empty())
queueObj.enqueue("Hello")
queueObj.enqueue("World")
queueObj.enqueue("Mr")
queueObj.enqueue("Japan")
poped = queueObj.dequeue()
print(poped)
poped = queueObj.dequeue()
print(poped)
poped = queueObj.dequeue()
print(poped)
poped = queueObj.dequeue()
print(poped)
print("\n")
print("\n")

# HashTable
test_results = {"Taro": 50, "Jiro": 30}
test_results["Taro"] += 15
test_results["Jiro"] = 20 
test_results["Taro"] += 5
test_results["Taro"] += 10
test_results["Saburo"] = 30
print(test_results["Taro"])
print(test_results["Jiro"])
print(test_results["Saburo"])
