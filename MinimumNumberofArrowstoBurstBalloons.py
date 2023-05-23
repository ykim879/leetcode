#By tracking end we can find inclusive 
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #sort points 
        points.sort()
        end = None
        res = 0
        #if newStart starts after end, than it is not overlapping: restart the pointer
        for p in points:
            if end == None or p[0] > end:
                end = p[1]
                res += 1
            else:
                end = min(p[1], end)
        return res
