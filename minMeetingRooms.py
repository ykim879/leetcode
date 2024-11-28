class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
       # premise: for each interval, check what is the max overlapping meetings in ant given time
        res = 0
        # sort the intervals in (starti) -> endi 
        intervals.sort(key = lambda x : x[0])
        ## stack = [] min heap
        dms = []
        ## overalapping = len(stack) + 1 of any given time 
        for start, end in intervals:
            while dms and dms[0] <= start:
                heapq.heappop(dms)
            heapq.heappush(dms, end)
            res = max(len(dms), res)
        return res
