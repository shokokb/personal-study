class Node:
    def __init__(self, data):
        self.data = data

class Array:
    def __init__(self):
        self.size = 0
        self.array = []

    # Random Access(O(1))
    def data(idx):
        return self.array[idx].data

    def append(self, data):
        self.insert(self.size, data)

    # insertion(O(n))
    def insert(self, idx, data):
        if self.size == 0:
            self.array.append(Node(data)) 
        else:
            self.array.append(None)
            # 後ろに一つずつずらす
            i = self.size
            for i in reversed(range(idx, self.size)):
                self.array[i + 1] = self.array[i]
            self.array[idx] = Node(data)
        self.size += 1

    def remove(self, idx):
        for i in reversed(range(idx, self.size - 1)):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def print_all(self):
        for i in range(self.size):
            print(str(self.array[i].data) + " ", end = "")
        print()

if __name__ == "__main__":
    ary = Array()
    print("size=" + str(ary.size))
    ary.append(100)
    ary.append(300)
    ary.append(200)
    ary.print_all()
    print("size=" + str(ary.size))
    ary.insert(1, 400)
    ary.print_all()
    ary.insert(0, 500)
    ary.print_all()
    ary.remove(3)
    ary.print_all()