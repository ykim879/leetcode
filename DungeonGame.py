class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        R, C = len(dungeon) - 1, len(dungeon[0]) - 1
        MAX = 40000000 
        # from destination to current, we the minimum health we need at each place
        for r in range(R, -1, -1):
            for c in range(C, -1, -1):
                need = MAX
                if r == R and c == C:
                    need = 1
                elif r < R:
                    need = dungeon[r+1][c]
                if c < C:
                    need = min(need, dungeon[r][c + 1])
                need -= dungeon[r][c];  
                if need <= 0:
                    need = 1              
                dungeon[r][c] = need
        return dungeon[0][0];
