class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array since it is doing binary search on nums1, it want to optimize search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        L1, L2 = len(nums1), len(nums2)
        total = L1 + L2
        half = total // 2
        # median is when there is smaller element (L1 + L2) // 2
        # Binary search on nums1
        l, r = 0, L1
        while l <= r:
            i = (l + r) // 2
            j = half - i

            # Edge cases for out-of-bounds
            nums1_left = nums1[i-1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < L1 else float('inf')
            nums2_left = nums2[j-1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < L2 else float('inf')

            # Check if valid partition
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Odd total length
                if total % 2:
                    return min(nums1_right, nums2_right)
                # Even total length
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2

            # Adjust binary search range
            elif nums1_left > nums2_right:
                r = i - 1
            else:
                l = i + 1
