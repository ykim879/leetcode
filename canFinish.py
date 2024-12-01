class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prev -> next 
        adj = defaultdict(list) # key = node, value = list of neighbors
        for nxt, prev in prerequisites:
            adj[prev].append(nxt)
        # find cycle: current node is in parents
        parents, visited = set(), set()
        def dfs(cur):
            if cur in parents:
                return False
            parents.add(cur)
            for nxt in adj[cur]:
                if nxt not in visited:
                    if not dfs(nxt):
                        return False
            visited.add(cur)
            return True
        for i in range(numCourses):
            if i not in visited and not dfs(i):
                return False
        return True
