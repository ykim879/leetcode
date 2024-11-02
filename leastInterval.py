class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # problem: take the task in any order as much as possible
        # bigger counter goes first tahtn the others -> heapq
        # maintain the n list (in order) and set (to keep which elements are in this interval)
        # (1) order the maxheap with (count, character)
        tasks = Counter(tasks)
        h = [(-1*count, key) for key, count in tasks.items()] # available task
        heapq.heapify(h)
        q = deque() # cool down (time to be release, count, el)
        time = 0
        while h or q:
            time += 1
            if h:
                ## (1.1) pop the element from heapq (we know this is not in the list)
                c, el = heapq.heappop(h)
                c += 1
                if c < 0:
                    ## (1.2) put it in res, put this in list for appendi
                    q.append((time + n, c, el))
            if q and q[0][0] == time:
                _, c, el = q.popleft()
                heapq.heappush(h, (c, el))
        return time
