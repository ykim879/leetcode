class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # rooms can be adjency matrix
        # start the stack from all gates
        R, C = len(rooms), len(rooms[0])
        q = deque()
        for r in range(R):
            for c in range(C):
                if rooms[r][c] == 0:
                    for i, j in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                        q.append((r+i, c+j, 1))
        while q:
            r, c, d = q.popleft()
            if r < 0 or r >= R or c < 0 or c >= C or rooms[r][c] < 2147483647:
                continue
            rooms[r][c] = d
            for i, j in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                q.append((r+i, c+j, d+1))
