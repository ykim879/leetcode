class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)//3
        L = len(nums) - 1
        res = []
        nums.sort()
        occ = 0
        for i,n in enumerate(nums):
            occ += 1
            if i == L or n != nums[i+1]:
                if occ > N:
                    res.append(n)
                occ = 0
        return res
            
