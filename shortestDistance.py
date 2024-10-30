from collections import deque

class Solution:
    def shortestDistance(self, grid):
        # Next four directions.
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        rows, cols = len(grid), len(grid[0])
        
        # Total matrix to store total distance sum for each empty cell.
        total = [[0] * cols for _ in range(rows)]
        
        emptyLandValue = 0
        minDist = float('inf')
        
        for row in range(rows):
            for col in range(cols):
                
                # Start a BFS from each house.
                if grid[row][col] == 1:
                    minDist = float('inf')
                    
                    # Use a queue to perform BFS, starting from the cell at (row, col).
                    q = deque([(row, col)])
                    
                    steps = 0
                    
                    while q:
                        steps += 1
                        
                        for _ in range(len(q)):
                            curr_row, curr_col = q.popleft()
                            
                            for dr, dc in dirs:
                                nextRow, nextCol = curr_row + dr, curr_col + dc
                                
                                # For each cell with the value equal to empty land value,
                                # add distance and decrement the cell value by 1.
                                if 0 <= nextRow < rows and 0 <= nextCol < cols and grid[nextRow][nextCol] == emptyLandValue:
                                    grid[nextRow][nextCol] -= 1
                                    total[nextRow][nextCol] += steps
                                    q.append((nextRow, nextCol))
                                    minDist = min(minDist, total[nextRow][nextCol])
                    
                    # Decrement empty land value to be searched in next iteration.
                    emptyLandValue -= 1
        
        return -1 if minDist == float('inf') else minDist
