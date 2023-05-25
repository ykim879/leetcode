from collections import deque
from copy import copy
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # keep track of unique answer
        # keep track if queen can be placed
        # for each square, check queen is placed and queen is not placed with bfs. 
        # visited: 0,1 of each square - current chess state and current square
        #           for current chess state: set value of available spots 
        # bfs: 1. place queen at the square and occupies all non-placable squares if it is able to place more if n is empty bfs if not skip
        #      2. do not place queen at the square in the moment
        
        # for each row place in different position, prev will always be different so no duplicate will be there
        # for each row, place available col, available, positivediag, negative diag with current step. replace avaiability list whenever it ends with current row
        cols = set(i for i in range(n))
        negativeDiag = set(i for i in range(2*n)) # abs(r -c) # positiveDiag
        positiveDiag = set(i for i in range(-1 * n + 1, n)) # r + c
        currentRow = [([], cols, positiveDiag, negativeDiag)]
        for r in range(n):
            nextRow = []
            while currentRow:
                track, availableCols, availablePositiveDiag, availableNegativeDiag = currentRow.pop()
                if not availableCols or not availablePositiveDiag or not availableNegativeDiag:
                    continue
                for c in availableCols:
                    if r + c not in availableNegativeDiag or r - c not in availablePositiveDiag:
                        continue
                    s = ""
                    for c1 in range(n):
                        if c1 == c:
                            s += "Q"
                        else:
                            s += "."
                    newTrack, newCols, newPositiveDiag, newNegativeDiag = copy(track), copy(availableCols), copy(availablePositiveDiag), copy(availableNegativeDiag)
                    newTrack.append(s)
                    newCols.remove(c)
                    newPositiveDiag.remove(r-c)
                    newNegativeDiag.remove(r+c)
                    nextRow.append((newTrack, newCols, newPositiveDiag, newNegativeDiag))
            currentRow.extend(nextRow)
        res = [row[0] for row in currentRow]
        return res
