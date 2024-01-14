class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res, visited, oindexed, group = [-1 for _ in rains], {}, defaultdict(list), 0
        def updateVisited(group, v):
            if oindexed[group]:
                group += 1
            visited[v] = group
            return group
        for i, v in enumerate(rains):
            if v == 0:
                res[i] = 1
                oindexed[group].append(i)
            elif v in visited:
                dried = False
                for g in range(visited[v], group + 1):
                    if oindexed[g]:
                        res[oindexed[g].pop()] = v
                        dried = True
                        group = updateVisited(group, v)
                        break
                if not dried:
                    return []
            else:
                group = updateVisited(group, v)
        return res
