class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict(list)
        for i,c in enumerate(s):
            dic[c].append(i)
        i, stack = 0, []
        for i, cur in enumerate(s):
            if cur in dic:
                start, end = dic[cur][0], dic[cur][-1]
                while stack and stack[-1][1] >= start:
                    start = min(stack[-1][0], start)
                    end = max(stack[-1][1], end)
                    stack.pop()
                stack.append((start, end))
                dic.pop(cur)
        res = []
        for i1, i2 in stack:
            res.append(i2 - i1 + 1)
        return res
