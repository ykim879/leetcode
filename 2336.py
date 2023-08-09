from heapq import heappush, heappop
class SmallestInfiniteSet:

    def __init__(self):
        self.k = 1
        self.hq = []
        self.set = set()
    def popSmallest(self) -> int:
        if self.hq:
            res = heappop(self.hq)
            self.set.remove(res)
            return res
        self.k += 1
        return self.k - 1
    def addBack(self, num: int) -> None:
        if num < self.k and num not in self.set:
            heappush(self.hq, num)
            self.set.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
