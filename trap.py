class Solution:
    def trap(self, height: List[int]) -> int:
        # stores max of height[i + 1:]
        L = len(height)
        maxh = [0 for _ in range(L)]
        for i in range(L - 2, -1, -1):
            maxh[i] = max(height[i + 1], maxh[i + 1])
        l, res = 0, 0
        # loop
        while l < L - 1: # this can be chaned
            while height[l] == 0:
                l += 1
                if l == L:
                    break
            r = l + 1
            if r < L:
                leftwall = min(maxh[l], height[l])
                ## find r bigger or equal to l: set waterbetween
                while leftwall > height[r]: # always there is r
                    r += 1
                res += (r - l - 1) * leftwall
                ### loop until l == r: add up the height of between
                l += 1
                while l < r:
                    res -= height[l]
                    l += 1
        return res
