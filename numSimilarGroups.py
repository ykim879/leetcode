class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        # island, how many island we have
        ## connected vertices: (1) if there is difference: count += 1 if count == 2 they are connected -> to check neighbor
        visited = set()
        def dfs(i):            
            # add it to visited
            visited.add(i)
            # check other neighbors
            cur = strs[i]
            for i2 in range(len(strs)): # for all indeices this: it it doens't it gives incorrect error since we can traverse before but it was island but actually it could be connected to now
                if i2 in visited:
                    continue
                nxt, count = strs[i2], 0
                if cur == nxt:
                    dfs(i2)
                    continue
                for t in range(len(strs[0])):
                    if cur[t] != nxt[t]:
                        count += 1
                        if count > 2:
                            break
                if count <= 2:
                    dfs(i2)
        res = 0
        for i in range(len(strs)):
            if i not in visited:
                res += 1 
                dfs(i)
        return res
