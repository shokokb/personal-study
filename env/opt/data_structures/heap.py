# coding: UTF-8

class Heap:
    @classmethod
    def __init__(self):
        self.l = []

    @classmethod
    def size(self):
        return len(self.l)

    @classmethod
    def push (self, val):
        self.l.append(val)
        i = self.size()
        while i > 1:
            pi = i // 2
            if self.l[pi-1] > self.l[i-1]:
                self.l[pi-1], self.l[i-1] = self.l[i-1], self.l[pi-1]
            i = pi
        
    @classmethod
    def pop(self):
        
        if self.size() == 0:
            return None

        first = self.l.pop(0)
        self.l.insert(0, self.l.pop())
        pi = 1
        li = 2 * pi
        ri = 2 * pi + 1
        i = ri if ri <= self.size() and self.l[ri-1] < self.l[li-1] else li
        while i <= self.size():
            if self.l[pi-1] > self.l[i-1]:
                self.l[pi-1], self.l[i-1] = self.l[i-1], self.l[pi-1]
                pi = i
                li = 2 * pi
                ri = 2 * pi + 1
                i = ri if ri <= self.size() and self.l[ri-1] < self.l[li-1] else li
            else: 
                break
        print(first, self.l)
        return first
	
    @classmethod
    def sort(self):
        ret = []
        while self.size() > 0:
            n = self.pop()
            ret.append(n)
        return ret

    @classmethod
    def display (self):
        print(self.l)


if __name__ == "__main__":
    h = Heap()

    h.push(1)
    h.push(3)
    h.push(6)
    h.push(4)
    h.push(8)
    h.push(7)
    h.push(5)
    h.push(2)
    
    h.display()

    n = h.pop()
    print("pop=", n)
    h.display()

