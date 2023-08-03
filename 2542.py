class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        import heapq
        L = len(nums1)
        l = sorted([(nums2[i], nums1[i]) for i in range(L)], reverse=True)
        print(l)
        res = 0
        cur = 0
        hq = []
        for n2, n1 in l:
            heapq.heappush(hq, n1)
            cur += n1
            if len(hq) >= k:
                if len(hq) > k:
                    cur -= heapq.heappop(hq)
                res = max(res, cur * n2)
        return res
