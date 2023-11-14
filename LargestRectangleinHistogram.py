L = len(heights)
        stack = [(h, i) for i, h in enumerate(heights)]
        stack.sort(reverse= True)
        index = {}
        res = 0
        for h, i in stack:
            start = end = i
            if i > 0 and (i-1) in index:
                start = index[i-1][0]
            if i < L - 1 and (i+1) in index:
                end = index[i+1][1]
            index[start] = index[end] = (start, end)
            res = max(res, (end - start + 1) * h)
        return res
