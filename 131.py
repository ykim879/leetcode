class Solution:
    def partition(self, s: str) -> List[List[str]]:
        from copy import copy
        import heapq

        L = len(s)
        visited = set()
        memoized = defaultdict(list)
        memoized[(0,-1)].append([])
        q = [(0, j) for j in range(0, L)]

        def palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        while q:
            i, j = heappop(q)
            if (i,j) not in visited:
                if palindrome(i,j):
                    start = i+1
                    for end in range(start, L):
                        heappush(q, (start, end))
                    for prev in memoized[0, i-1]:
                        prev = copy(prev)
                        prev.append(s[i:j+1])
                        memoized[(0,j)].append(prev)
                visited.add((i,j))

        return memoized[(0,L-1)]

                    
                
                

