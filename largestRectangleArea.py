class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        L = len(h)
        #for each i, if we know subarray where h[i] is minimum, histogram including h[i] would be subarray * min[h[i]]
        sa, sb, res = [L] * L, [-1] * L, 0
        # sa: monolithic with decreaing order if h[sa[-1]] < h[i]: append i
        # else: pop until h[sa[-1]] < h[i] # there is element smaller than hpi
        stack = []
        for i in range(L-1, -1, -1):
            while stack and h[stack[-1]] >= h[i]:
                stack.pop()
            if stack:
                sa[i] = stack[-1]
            stack.append(i)
        stack.clear()
        for i, n in enumerate(h):
            while stack and h[stack[-1]] >= h[i]:
                stack.pop()
            if stack:
                sb[i] = stack[-1]
            res = max(res, (sa[i] - sb[i] - 1) * n)
            stack.append(i)
        return res
