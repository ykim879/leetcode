class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left - right: left < right: nums[left]
        # left > right: left < nums[mid] -> left = mid + 1
        # nums[mid] < left -> nums[mid] < right: check if mid is minimum if not right = mid - 1
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                return nums[l]
            m = (l+r + 1) // 2
            if nums[l] < nums[m]:
                l = m + 1
            elif nums[m] < nums[m-1]:
                return nums[m]
            else:
                r = m - 1
        return nums[l]
