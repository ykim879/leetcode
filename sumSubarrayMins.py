class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # 3* 10**4 is too big for O(n^2) in space and time
        L = len(arr)
        lst, bst = [-1] * L, [L] * L
        stack = [] # monolithic increasing, index of arr 
        ## s1 first index before i that smaller than i: any index bigger than i before i is no longer useful. increasing stack
        for i, n in enumerate(arr):
            while stack and n < arr[stack[-1]]:
                stack.pop()
            if stack:
                lst[i] = stack[-1]
            stack.append(i)
        stack.clear()
        ## s2: first index after i that smaller than i: from back to start: any index bigger than i before i is no longer useful. increasing stack
        for i in range(L-1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            if stack:
                bst[i] = stack[-1]
            stack.append(i)
        res = 0
        for i, n in enumerate(arr):
            res += (bst[i] - i) * (i - lst[i]) * n
        return res % (10 ** 9 + 7)
