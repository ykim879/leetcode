class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        res = ""
        for k, v in sorted(Counter(list(s)).items(), reverse = True, key = lambda item: item[1]):
            res += k * v
        return res
