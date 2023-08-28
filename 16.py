class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        L = len(nums) - 1
        diff = 2 * 10 ** 4
        for i in range(L - 1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            newtarget = target - nums[i]
            start, end = i+1, L
            while start < end:
                total = nums[start] + nums[end]
                if total == newtarget:
                    return target
                if abs(diff) > abs(newtarget - total):
                    diff = newtarget - total
                if total < newtarget:    
                    start += 1
                else:
                    end -= 1
        return target - diff
