class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = defaultdict(lambda:0)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        next_time = self.time[message]
        if next_time <= timestamp:
            self.time[message] = timestamp + 10
            return True
        else:
            return False
            

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)