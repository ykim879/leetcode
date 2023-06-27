from collections import deque
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        R, C = len(board), len(board[0])
        dest = R * C
        # bfs 
        visited = set()
        # store every 6 moves from start with priority queue where 
        q = deque([(0,1)])
        # calculate board from number
        def position(cur):
            cur -= 1
            curx =  cur // C
            cury = cur % C
            if curx % 2:
                cury = (C - 1) - cury
            curx = R - curx - 1
            return curx, cury
        while q:
            move, cur = q.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            move += 1
            for i in range(6, 0, -1):
                nex = cur + i
                if nex >= dest:
                    return move
                curx, cury = position(nex)
                if board[curx][cury] > -1:
                    nex = board[curx][cury]
                    if nex == dest:
                        return move 
                    if nex in visited:
                        continue
                q.append((move, nex))
        return -1
