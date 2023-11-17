from collections import Counter
class Solution:
    def __init__(self):
        self.visited = {}
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        key = (s1, s2)
        if key in self.visited:
            return self.visited[key]

        if len(s1) == 1 or Counter(s1) != Counter(s2):
            self.visited[key] = False
            return False
        
        res = False
        for i in range(1, len(s1)):
            left,right = s1[:i], s1[i:]
            if right + left == s2 or (self.isScramble(left, s2[:i]) and self.isScramble(right, s2[i:])) or (self.isScramble(left, s2[-1 * i : ]) and self.isScramble(right, s2[:-1*i])):
                res = True
                break
        self.visited[key] = res
        return res
