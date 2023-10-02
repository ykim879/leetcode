class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        i1 = i2 = 0
        while i1 < m:
            if nums1[i1] > nums2[0]:
                temp = nums1[i1]
                nums1[i1] = nums2[0]
                nums2[0] = temp
                # bubble sort the nums2
                i2 = 0
                while i2 < n - 1 and nums2[i2] > nums2[i2 + 1]:
                    temp = nums2[i2 + 1]
                    nums2[i2 + 1] = nums2[i2]
                    nums2[i2] = temp
                    i2 += 1
            i1 += 1
        i2 = 0
        while i2 < n:
            nums1[i1] = nums2[i2]
            i1 += 1
            i2 += 1
        
