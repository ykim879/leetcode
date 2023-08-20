class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import Counter
        m, csum, res = Counter([0]), 0, 0
        for n in nums:
            csum += n
            res += m[csum-k]
            m[csum] += 1
        return res

            
