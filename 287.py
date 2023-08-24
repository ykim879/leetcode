class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while fast == 0 or nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[fast]
        return nums[slow]
        
        
