class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # place larger value fist from the back. 
        p, p1, p2 = len(nums1) - 1, m-1, n-1
        while p1 >= 0 and p2 >= 0:
            if nums2[p2] >= nums1[p1]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        if p2 >= 0:
            nums1[:p+1] = nums2[:p2+1]
