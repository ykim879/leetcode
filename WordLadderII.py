class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        from collections import deque
        if endWord not in wordList:
            return []
        ## initialization
        # visited: key of word and value of depth
        visited = {beginWord: 0}
        # adj: key of word and value of the next possible word 
        adj = defaultdict(list)
        # q: queue
        q = deque([beginWord])

        # bfs to populate adj
        while q:
            word = q.popleft()
            depth = visited[word]
            if word == endWord:
                break
            # populate adj list
            diff = 0
            for i, w in enumerate(endWord):
                if word[i] != w:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                adj[word].append(endWord)
                if endWord not in visited:
                    visited[endWord] = depth + 1
                    q.append(endWord)
                continue
            for nextWord in wordList:
                if word == nextWord or word == endWord or (nextWord in visited and visited[nextWord] <= depth):
                    continue
                diff = 0
                for i, w in enumerate(nextWord):
                    if word[i] != w:
                        diff += 1
                        if diff > 1:
                            break
                if diff == 1:
                    adj[word].append(nextWord)
                    if nextWord not in visited:
                        visited[nextWord] = depth + 1
                        q.append(nextWord)
        
        # populate res by doing dfs
        res = []
        currentPath = []
        def dfs(cur):
            currentPath.append(cur)
            for nextWord in adj[cur]:
                if nextWord == endWord:
                    res.append(currentPath + [endWord])
                    break
                dfs(nextWord)
            currentPath.pop()
        dfs(beginWord)
        return res
