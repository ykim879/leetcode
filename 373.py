class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        from heapq import heappop, heappush
        h = [(nums1[0] + nums2[0], 0, 0)]
        L1, L2 = len(nums1), len(nums2)
        visited = set((0,0))
        res = []
        while h and k > 0:
            _, i1, i2 = heappop(h)
            res.append([nums1[i1], nums2[i2]])
            if i1 < L1 - 1 and (i1+1, i2) not in visited:
                heappush(h, (nums1[i1+1] + nums2[i2], i1+1, i2))
                visited.add((i1 + 1, i2))
            if i2 < L2 - 1 and (i1, i2 + 1) not in visited:
                heappush(h, (nums1[i1] + nums2[i2 + 1], i1, i2 + 1))
                visited.add((i1, i2 + 1))
            k -= 1
        return res
