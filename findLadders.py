class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        queue = deque([beginWord])
        find = False
        parents = defaultdict(list)
        L = len(beginWord)
        while queue and not find:
            nextLayer = set()
            while queue:
                current = queue.popleft()
                for i in range(L):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = current[:i] + c + current[i+1:]
                        if newWord in wordList:
                            nextLayer.add(newWord)
                            parents[newWord].append(current)
                            if newWord == endWord:
                                find = True
                                break
            if not find:
                queue.extend(nextLayer)
                wordList -= nextLayer
        def backtrack(word):
            if word == beginWord:
                return [[beginWord]]
            return [path + [word] for parent in parents[word] for path in backtrack(parent)]
        return backtrack(endWord)
            
