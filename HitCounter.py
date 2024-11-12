class HitCounter:

    def __init__(self):
        self.timestamp = deque() # deque [timestamp, count]
        self.count = 0
    def update(self, time):
        while self.timestamp and self.timestamp[0][0] <= time - 300:
            _,count = self.timestamp.popleft()
            self.count -= count
    def hit(self, timestamp: int) -> None:
        self.update(timestamp)
        if self.timestamp and self.timestamp[-1][0] == timestamp:
            self.timestamp[-1][1] += 1
        else:
            self.timestamp.append([timestamp, 1])
        self.count += 1
    def getHits(self, timestamp: int) -> int:
        self.update(timestamp)
        return self.count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
