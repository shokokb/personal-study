class Heap:
    def __init__(self):
        self.q = []

    def push(self, node):
        self.q.append(node)

        i = len(self.q) - 1
        p = (i - 1) // 2


        while p >= 0 and self.q[p] > self.q[i]:
            self.q[p], self.q[i] = self.q[i], self.q[p]
            i = p
            p = (i - 1) // 2

        # print("push", self.q)


    def pop(self):
        if not self.q:
            return None
        
        p = 0

        res = self.q.pop(p)

        if self.q:
            node = self.q.pop()
            self.q.insert(p, node)
            while True:
                l = 2 * p + 1
                r = 2 * p + 2
                smallest = p

                if l < len(self.q) and self.q[p] > self.q[l]:
                    smallest = l
                if r < len(self.q) and self.q[p] > self.q[r]:
                    smallest = r
                if smallest == p:
                    break

                self.q[p], self.q[smallest] = self.q[smallest], self.q[p]
                p = smallest 
            
    
        # print("pop", self.q)
        return res

    def is_empty(self):
        return len(self.q) == 0

def main():
    h = Heap()
    h.push(5)
    h.push(3)
    h.push(7)
    h.push(4)
    h.push(6)
    h.push(1)

    while not h.is_empty():
        node = h.pop()
        print(node)
    
if __name__ == "__main__":
    main()