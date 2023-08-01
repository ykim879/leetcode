class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for f, t in connections:
            adj[f].append((t, True))
            adj[t].append((f, False))
        d = deque(adj[0])
        visited = set([0])
        res = 0
        while len(visited) < n:
            c, sign = d.popleft()
            if c in visited:
                continue
            visited.add(c)
            if sign:
                res += 1
            d.extend(adj[c])
        return res
