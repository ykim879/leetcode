class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        return len(word1) == len(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values()) and set([*word1]) == set([*word2])
