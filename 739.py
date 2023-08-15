class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                i2, _ = stack.pop()
                res[i2] = i - i2
            stack.append((i, temp))
        return res
