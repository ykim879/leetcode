class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort by enddate - dp[i] has dependency of end date no t start date
        L = len(startTime)
        ranges = [(startTime[i], endTime[i], profit[i]) for i in range(L)]
        ranges.sort(key = lambda x: x[1])
        # dp[i] considering i element dp[i] = max(dp[ends before this start date] + profit[i], dp[i-1])
        dp = [0 for _ in range(L)]
        # finding right dp[ends before this start date]: have to find right most where the enddate is before the startdate 
        def find_right_end(idx, limit):
            ### binary search if dp[mid]'s enddate >= startdate:  end date = mid - 1
            ### elif mid's enddate < startdate: if mids' enddate + 1 doesn't exist or enddate + 1 >= startdate : return this mid else: return startdate = mid + 1
            start, end = 0, idx - 1
            while start <= end:
                mid = (start + end) // 2
                if ranges[mid][1] > limit:
                    end = mid - 1
                elif mid + 1 == idx or ranges[mid + 1][1] > limit:
                    return dp[mid]
                else:
                    start = mid + 1
            return 0
        for i, ran in enumerate(ranges):
            max_before = find_right_end(i, ran[0])
            dp[i] = max(max_before + ran[2], dp[i-1])
        return dp[-1]
