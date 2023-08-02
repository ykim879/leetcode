class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        r, c = len(maze) - 1, len(maze[0]) - 1
        bfs = deque([(entrance[0], entrance[1], 0)])
        visited = set()
        while bfs:
            cr, cc, cost = bfs.popleft()
            if (cr, cc) in visited:
                continue
            visited.add((cr, cc))
            cost += 1
            for ir, ic in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                ir += cr
                ic += cc
                if ir < 0 or ir > r or ic < 0 or ic > c or (ir == entrance[0] and ic == entrance[1]):
                    continue
                if maze[ir][ic] == '.':
                    if ir == 0 or ir == r or ic == 0 or ic == c:
                        return cost
                    bfs.append((ir, ic, cost))
        return -1
