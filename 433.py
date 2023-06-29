import heapq
class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        # shortest path: bfs
        # with priorityque: (differ, dist, node)
        # toVisit
        def getDiff(cur, nex):
            diff = 0
            for i in range(len(cur)):
                if cur[i] != nex[i]:
                    diff += 1
            return diff
        if startGene == endGene:
            return 0
        
        toVisit = set(bank)
        toVisit.add(startGene)
        if endGene not in toVisit:
            return -1
        diff = getDiff(startGene, endGene)
        pq = [(diff, 0, startGene)]

        while pq:
            diff, path, cur = heapq.heappop(pq)
            if cur in toVisit:
                toVisit.remove(cur)
                path += 1
                if getDiff(cur, endGene) <= 1:
                    return path
                for nex in toVisit:
                    diff = getDiff(cur, nex)
                    #is bank and others unique
                    if diff == 1:
                        heapq.heappush(pq, (diff, path, nex))
        return -1
