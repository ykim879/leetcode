class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        L = len(nums)
        # recursive kthSum() while base is k == 2
        def twoSum(start, tar):
            end = L - 1
            res = []
            while start < end:
                cur = nums[start] + nums[end]
                if cur == tar:
                    res.append([nums[start] , nums[end]])
                    while start < end and nums[start] == nums[start + 1]: 
                        start += 1
                if cur > tar:
                    end -= 1
                else:
                    start += 1
            return res
        def kthSum(k, start, tar):
            if k == 2:
                return twoSum(start, tar)
            res = []
            for i in range(start, L):
                cur = nums[i]
                if i > start and cur == nums[i-1]:
                    continue
                for arr in kthSum(k - 1, i + 1, tar - cur):
                    newEle = arr + [cur]
                    res.append(newEle)
            return res
        return kthSum(4, 0, target)
            
