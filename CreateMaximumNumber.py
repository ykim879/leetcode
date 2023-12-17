class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        memoized = {}
        # to make maxNumber of len k, we only can drop number len(nums) - k times. 
        # we can also drop and append at the last index to keep reltative index
        # with this limitation, if we keep dropping with capacity will ultimately fine 
        # memoized if len(stack) > k for
        def maxNumber(num, k, t):
            key = (t, k)
            if key in memoized:
                return memoized[key]
            drop = len(num) - k
            res = []
            for n in num:
                while drop and res and res[-1] < n:
                    res.pop()
                    drop -= 1
                res.append(n)
            for m in range(k, len(res) + 1):
                memoized[(t, m)] = res[:m]
            return res[:k]
        for i in range(min(len(nums1), k)+1):
            maxNumber(nums1, i, 1)
        for i in range(min(len(nums2), k)+1):
            maxNumber(nums2, i, 2)
        def merge(n):
            n_ = k - n
            arr1 = memoized[(1, n)]
            arr2 = memoized[(2, n_)]
            res = []
            i1, i2 = 0, 0
            for i in range(k):
                if i1 == n:
                    res.extend(arr2[i2:])
                    break
                elif i2 == n_:
                    res.extend(arr1[i1:])
                    break
                elif arr1[i1:] > arr2[i2:]: # compare the rest of array to predict future 
                    res.append(arr1[i1])
                    i1 += 1
                else:
                    res.append(arr2[i2])
                    i2 += 1
            return res
        return max(merge(n) for n in range(max(k - len(nums2), 0), min(len(nums1), k) + 1))
