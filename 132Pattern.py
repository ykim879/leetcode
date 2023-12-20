class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minArr = [nums[0]]
        for i in range(1, len(nums)):
            minArr.append(min(minArr[-1], nums[i]))
        s = [] # monotonic stacck of decreasing order
        for i in range(len(nums) - 1, 0, -1):
            n = nums[i]
            while s and s[-1] < n:
                if minArr[i-1] < s[-1]:
                    return True
                s.pop()
            if s and s[-1] == n:
                continue
            s.append(n)
        return False
