class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        res = []
        def backtrack(comb, count):
            if len(comb) == len(nums):
                res.append(list(comb))
            else:
                for key in count.keys():
                    if count[key] > 0:
                        comb.append(key)
                        count[key] -= 1
                        backtrack(comb, count)
                        comb.pop()
                        count[key] += 1
        backtrack([], Counter(nums))
        return res
