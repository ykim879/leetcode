class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        k -= 1
        d = deque() # <= k
        for i in range(len(nums)):
            # place ele in the place:
            # pop the end if it is smaller, and put if the deque empty or end ele is bigger
            while d and nums[d[-1]] <= nums[i]:
                d.pop()
            d.append(i)
            #k - 1 <= i : check max: pop until i is out of range, insert deque[0] in res
            if k <= i:
                while d[0] < i - k:
                    d.popleft()
                res.append(nums[d[0]])
        return res
'''
Time: O(n)
- The deque contains indices of elements in the current sliding window.
- When a new element is processed, the solution removes elements from the back of the deque that are **smaller** than the current element. This ensures that the deque only contains potential maximums.
- Each element can only be added to the deque once, and it can only be removed from the deque once. Therefore, each element is processed at most **twice** (once when it's added, once when it's removed).
- Hence, for each element, the operations on the deque (addition and removal) take **constant time** — O(1) for each add or remove operation.
space: O(k)
'''
