class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. 
        Set the size of the deque to be k.
        """
        self.l = [None for i in range(k)]
        self.k = k
        
    def size(self) -> int:
        size = len(list(filter(lambda n: n is not None, self.l)))
        return size
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. 
        Return true if the operation is successful.
        """
        size = self.size()
        if size >= self.k:
            return False
        left = self.l[0:self.k-1]
        self.l = [value]
        self.l.extend(left)
        # print("insertFront", self.l)
        return True       

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. 
        Return true if the operation is successful.
        """
        size = self.size()
        if size >= self.k:
            return False
        self.l[size] = value
        # print("insertLast", self.l)
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. 
        Return true if the operation is successful.
        """
        size = self.size()
        if size == 0:
            return False
        self.l = self.l[1:]
        self.l.append(None)
        # for i in range(1, self.k):
        #     self.l[i-1] = self.l[i]
        # self.l[self.k - 1] = None
        # print("deleteFront", self.l)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. 
        Return true if the operation is successful.
        """
        size = self.size()
        if size == 0:
            return False
        self.l[size - 1] = None
        # print("deleteLast", self.l)
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        size = self.size()
        if size == 0:
            return -1
        return self.l[0]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        size = self.size()
        if size == 0:
            return -1
        return self.l[size - 1]
        
    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size() == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size() == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()