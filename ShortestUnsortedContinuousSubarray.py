class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        first, second = -1, -2
        for i, n in enumerate(nums):
            if n != sortedNums[i]:
                if first == -1:
                    first = second = i
                else:
                    second = i
        return second - first + 1
