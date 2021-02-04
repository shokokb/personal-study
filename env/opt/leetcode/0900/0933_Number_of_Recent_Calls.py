class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        # self.requests.sort()
        term = [t - 3000, t]
        return len(list(filter(lambda x: term[0] <= x <= term[1], self.requests)))


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)