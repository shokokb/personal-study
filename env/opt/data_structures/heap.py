# coding: UTF-8

class Heap:
    @classmethod
    def __init__(self):
        self.l = []

    @classmethod
    def size(self):
        return len(self.l)

    @classmethod
    def insert (self, val):
        self.l.append(val)
        i = self.size()
        while i > 1:
            pi = i // 2
            if self.l[pi-1] > self.l[i-1]:
                self.l[pi-1], self.l[i-1] = self.l[i-1], self.l[pi-1]
            i = pi
        
    @classmethod
    def remove(self):
        
        if self.size() == 0:
            return

        if self.size() == 1:
            first = self.l.pop(0)
            return first

        first = self.l.pop(0)
        last = self.l.pop()
        self.l.insert(0, last)
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
            n = self.remove()
            ret.append(n)
        return ret

    @classmethod
    def display (self):
        print(self.l)


if __name__ == "__main__":
    h = Heap()

    h.insert(1)
    h.insert(3)
    h.insert(6)
    h.insert(4)
    h.insert(8)
    h.insert(7)
    h.insert(5)
    h.insert(2)
    
    h.display()

    n = h.remove()
    print("remove=", n)
    h.display()

