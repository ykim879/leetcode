class Solution:
    def __init__(self):
        self.memo = {0:0, 1:1}
    def fib(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]
