# coding: UTF-8

class UnionFindTree:
    def __init__(self, n:int):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x:int):
        if self.par[x] == x:
            return x
        else:
            return self.find(self.par[x])
    
    def unit(self, x:int, y:int):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 
        
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x:int, y:int):
        return self.find(x) == self.find(y)

if __name__ == "__main__":
    utree1 = UnionFindTree(10)
    print(utree1.same(1, 2))
    print(utree1.find(2))
    utree1.unit(1, 2)
    print(utree1.same(1, 2))
    print(utree1.find(2))



