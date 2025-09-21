class MRUQueue:

    def __init__(self, n: int):
        self.elements = [n for n in range(1, n + 1)] 

    def fetch(self, k: int) -> int:
        n = self.elements.pop(k - 1)
        self.elements.append(n)
        return n


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)