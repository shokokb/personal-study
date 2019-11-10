class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head : Node = None

    # Random Access(O(1))
    # def data(idx):
    #     temp = 
    #     return self.array[idx].data

    def size(self):
        temp = self.head
        size = 0
        while temp is not None:
            temp = temp.next
            size += 1
        return size
            
    def append(self, data):
        self.insert(self.size(), data)

    # insertion(O(1))
    def insert(self, idx, data):
        node = Node(data)
        if idx == 0:
            node.next = self.head
            self.head = node
        elif (0 < idx and idx <= self.size()):
            i = 0
            prev = self.head
            while prev is not None:
                if (i + 1 == idx):
                    node.next = prev.next
                    prev.next = node
                    break;
                prev = prev.next
                i += 1            

    def remove(self, idx):
        if idx == 0:
            self.head = head.next
        elif (0 < idx and idx <= self.size()):
            i = 0
            prev = self.head
            while prev is not None:
                if (i + 1 == idx):
                    prev.next = prev.next.next
                    break;
                prev = prev.next
                i += 1            

    def print_all(self):
        print("== print all ==")
        temp = self.head
        while temp is not None:
            print(str(temp.data) + " ")
            temp = temp.next

if __name__ == "__main__":
    l = List()
    print("size=" + str(l.size()))
    l.append(100)
    l.append(300)
    l.append(200)
    l.print_all()
    print("size=" + str(l.size()))
    l.insert(1, 400)
    l.print_all()
    l.insert(0, 500)
    l.print_all()
    l.remove(3)
    l.print_all()
    