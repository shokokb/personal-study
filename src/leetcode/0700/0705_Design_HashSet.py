class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []
        

    def add(self, key: int) -> None:
        for k in self.set:
            if k == key:
                return
        self.set.append(key)
        
    def remove(self, key: int) -> None:
        for i, k in enumerate(self.set):
            if k == key:
                del self.set[i]
                return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.set
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)