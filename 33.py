class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
        if nums[start] > nums[end]:
            if target < nums[end]:
                while start < end and nums[start] > nums[end]:
                    mid = (start + end) // 2
                    if nums[mid] == target:
                        return mid
                    if nums[mid] < target or nums[start] < nums[mid]:
                        start = mid + 1
                    else:
                        end = mid - 1
                        if nums[end] == target:
                            return end
            elif target > nums[start]:
                while start < end and nums[start] > nums[end]:
                    mid = (start + end) // 2
                    if nums[mid] == target:
                        return mid
                    if nums[mid] > target or nums[start] > nums[mid]:
                        end = mid - 1
                    else:
                        start = mid + 1
                        if nums[start] == target:
                            return start
            else:
                return -1
        # binary search
        while start <= end:
            mid = (start + end) //2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
