class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # 2 negative 1 positive pick (2 values from minimum * maximum)
        # 3 positive (3 maximum)
        ## edge case: all values are negative: we want to find all -> nums[-1] * nums[-2] * nums[-3]
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
