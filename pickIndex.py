class Solution:
    import bisect
    import random

    def __init__(self, w: List[int]):
        self.weights = [i/sum(w) for i in accumulate(w)]

    def pickIndex(self) -> int:
        return bisect.bisect(self.weights, random.random())


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
