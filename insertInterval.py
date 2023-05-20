class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        x, y = newInterval
        for i, interval in enumerate(intervals):
            if y < interval[0]:
                res.append([x,y])
                return res + intervals[i:]
            elif x > interval[1]: #first it will start up as x is always smaller than interval if it doesn't find its place
                res.append(interval)
            else: #in the range
                x, y = min(x, interval[0]), max(y, interval[1])
        res.append([x,y])
        return res

                
        
