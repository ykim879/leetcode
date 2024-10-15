class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        l = len(equations)
        adj = defaultdict(list)
        #(1) build adj
        for i, eq in enumerate(equations):
            a, b = eq
            w = values[i]
            adj[a].append((b, w))
            adj[b].append((a, 1/w))
        
        #(2) for each queries we want to populate res
        ##(2.1) bfs for queries
        def bfs(a, b):
            if a not in adj or b not in adj:
                return -1
            q, visited = deque([(a, 1)]), set()
            while q:
                c, w = q.popleft()
                if c in visited:
                    continue
                visited.add(c)
                if c == b:
                    return w
                for n, w2 in adj[c]:
                    q.append((n, w * w2))
            return -1
        return [bfs(a,b) for a, b in queries]
    
