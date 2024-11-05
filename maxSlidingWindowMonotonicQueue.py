class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # max (heapq) last in always going to last longer -> monotonic queue (value, index)
        q = deque() 
        res = []
        for end, num in enumerate(nums):
            while q and q[-1][0] <= num:
                q.pop()
            q.append((num, end))
            if end >= k - 1:
                start = end - k + 1
                while q[0][1] < start:
                    q.popleft()
                res.append(q[0][0])
        return res
