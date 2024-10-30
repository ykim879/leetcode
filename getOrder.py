class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # at any given available cpu time: the cpu will take shortest processing time in queue. otherwise, if it is empty, idle.
        tasks = [(task[0], task[1], idx) for idx, task in enumerate(tasks)]
        tasks.sort(key= lambda x: x[0]) # to save time of ordering by processing time
        # priority queue: process the queue (process time, index)
        hq, res = [], []
        i, L, endTime = 0, len(tasks), 0
        while len(res) < L:
            if hq:
                processTime, idx = heapq.heappop(hq)
                res.append(idx)
                endTime += processTime
                # each time when we process task: queue up the elements that enqued before the end time. 
                while i < L and tasks[i][0] <= endTime :
                    heapq.heappush(hq, (tasks[i][1], tasks[i][2]))
                    i += 1
            else:
                # queue up all the elements which has time same enequeue time after i and update
                endTime = tasks[i][0]
                while i < L and tasks[i][0] == endTime :
                    heapq.heappush(hq, (tasks[i][1], tasks[i][2]))
                    i += 1
        return res
