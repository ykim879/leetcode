from collections import deque
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #make priority as operation - match
        h = deque([(word1, word2, 0)])
        visited = set()
        min_ = len(word1) + len(word2) + 1 
        def skipSequence(w1, w2, o):
            if len(w1) == 0 or len(w2) == 0:
                return w1, w2, o
            i = 0
            while i < len(w1) and i < len(w2):
                if w1[i] == w2[i]:
                    i += 1
                else:
                    break
            return w1[i:], w2[i:], o
        while h:
            w1, w2, o = h.popleft()
            if (w1,w2) in visited:
                continue
            visited.add((w1,w2))
            if w1 == w2:
                #check all remaining if others have same p chose minimum
                if o < min_:
                    min_ = o
            elif len(w2) == 0:
                if o + len(w1) < min_:
                    min_ = o + len(w1)
            elif len(w1) == 0:
                if o + len(w2) < min_:
                    min_ = o + len(w2)
            elif w1[0] == w2[0]:
                h.append(skipSequence(w1[1:], w2[1:], o))
            else:
                o += 1
                if o >= min_:
                    continue
                #replace
                if len(w1) == 1 and len(w2) == 1:
                    if min_ > o:
                        min_ = o
                else:
                    h.append((skipSequence(w1[1:], w2[1:], o)))
                #insert
                h.append((skipSequence(w1, w2[1:], o)))
                #delete
                h.append((skipSequence(w1[1:], w2, o)))
        return min_
