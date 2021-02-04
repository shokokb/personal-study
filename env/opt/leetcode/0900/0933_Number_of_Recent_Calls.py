class RecentCounter:

    def __init__(self):
        self.slide_window = deque()

    def ping(self, t: int) -> int:
        self.slide_window.append(t)
        while self.slide_window[0] < t - 3000:
            self.slide_window.popleft()
        return len(self.slide_window)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)