class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        parents = set()
        adj = defaultdict(list)
        for nxt, pre in prerequisites:
            adj[nxt].append(pre)
        visited = set()
        path = []
        def dfs(cur): #O(numCourses + len(prerequisites)) = O(n+m) u->v v comes first then u
            # base case: (1) when when cur is visited: return True (2) when cur is in parents: return False
            if cur in visited:
                return True
            if cur in parents:
                return False
            # add in parents
            parents.add(cur)
            # visit all dfs(prerequisites) and see if it is all true. if any is false, return false
            for pre in adj[cur]:
                if not dfs(pre):
                    return False
            # remove cur from parents
            parents.remove(cur)
            # add cur to path
            path.append(cur)
            # add cur to visited
            visited.add(cur)
            return True
        for cur in range(numCourses):
            if not dfs(cur):
                return []
        return path
