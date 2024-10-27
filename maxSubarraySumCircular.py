class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currentsum, currentsum2, totalsum , res, minres = 0, 0, 0, -3 * 10**4 - 1, 3 * 10**4 + 1
        for n in nums:
            totalsum += n
            currentsum += n
            currentsum2 += n
            res = max(res, currentsum)
            minres = min(currentsum2, minres)
            if currentsum < 0:
                currentsum = 0
            if  currentsum2 > 0:
                currentsum2 = 0
        if totalsum - minres == 0:
            return res
        return max(res, totalsum - minres)
