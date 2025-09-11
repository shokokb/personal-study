# coding: UTF-8

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for _ in range(self.MAX)] 

    def set(self, key:int, value: str):
        idx = self.hashFunction(key)
        if value not in self.arr[idx]:
            self.arr[idx].append(value)
    
    def get(self, key:int):
        idx = self.hashFunction(key)
        print("===")
        for v in self.arr[idx]:
            print(v)
        print("===")

    def hashFunction(self, key:int) -> int:
        return key % self.MAX


if __name__ == "__main__":
    h = HashTable()
    h.set(1003, 'apple')
    h.set(1003, 'banana')
    h.set(1003, 'grape')
    h.get(1003)
    h.get(1004)
