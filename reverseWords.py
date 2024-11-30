class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words.reverse()
        res = ""
        for word in words:
            if word:
                res += (word + " ")
        return res[:-1] if res else ""
