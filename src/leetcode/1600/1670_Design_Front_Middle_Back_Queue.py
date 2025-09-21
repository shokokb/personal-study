class FrontMiddleBackQueue:

    def __init__(self):
        self.items = []
        
    def pushFront(self, val: int) -> None:
        self.items.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        self.items.insert(len(self.items) // 2, val)

    def pushBack(self, val: int) -> None:
        self.items.append(val)

    def popFront(self) -> int:
        if len(self.items) == 0:
            return -1
        return self.items.pop(0)

    def popMiddle(self) -> int:
        if len(self.items) == 0:
            return -1
        return self.items.pop((len(self.items) - 1)// 2)

    def popBack(self) -> int:
        if len(self.items) == 0:
            return -1
        return self.items.pop()
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()