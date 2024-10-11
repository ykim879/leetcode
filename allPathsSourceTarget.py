class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        end = len(graph) - 1
        res = []
        def dfs(cur, path):
            # base case
            if cur == end:
                res.append(list(path))
                return
            for neighbor in graph[cur]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()
        dfs(0, list([0]))
        return res
