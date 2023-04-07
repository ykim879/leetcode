import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # overlapped:
        #   data type: heqp
        #   representation: (height, right) that is overlapped currently - sorted by height (non-decreasing order)
        overlapped = []
        res = []
        def ifHeightHasChanged():
            if overlapped and res[-1][1] != -1 * overlapped[0][0]:
                    res.append([max_building[1], -1 * overlapped[0][0]])
            elif not overlapped:
                res.append([max_building[1], 0])
        
        for each in buildings:
            # before we check current new building, we want to pop maximum height if it is out of range
            while overlapped and overlapped[0][1] < each[0]:
                max_building = heapq.heappop(overlapped)
                # we need to pop all buildings that are overlapped by current maximum height to not duplicate result
                while overlapped and overlapped[0][1] <= max_building[1]:
                    heapq.heappop(overlapped)
                # check if the maximum height has changed
                ifHeightHasChanged()

            heapq.heappush(overlapped, (-1 * each[2], each[1]))
            # check lefti and add res if the height has changed
            if len(res) == 0:
                res.append([each[0], each[2]])
            elif -1 * overlapped[0][0] != res[-1][1]:
                max_ = -1 * overlapped[0][0]
                if res[-1][0] == each[0]:
                    if max_ > res[-1][1]:
                        res.pop(-1)
                    else:
                        continue
                res.append([each[0], max_])

        #after check pop all remaining buildings
        while overlapped:
            max_building = heapq.heappop(overlapped)
            while overlapped and overlapped[0][1] <= max_building[1]:
                heapq.heappop(overlapped)
            ifHeightHasChanged()
            
        return res
