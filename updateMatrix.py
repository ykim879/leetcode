from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R, C = len(mat), len(mat[0])
        q = deque()
        
        # Initialize the queue with all '0' cells and set '1' cells to infinity
        for r in range(R):
            for c in range(C):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = float('inf')
        
        # Directions for moving up, down, left, right
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # BFS
        while q:
            r, c = q.popleft()
            
            # Check all 4 possible directions
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                
                # If within bounds and can be updated with a shorter distance
                if 0 <= nr < R and 0 <= nc < C and mat[nr][nc] > mat[r][c] + 1:
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))
        
        return mat
