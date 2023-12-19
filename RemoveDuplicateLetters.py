class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        freq = Counter(list(s))
        st = [] # Monotonic stack to maintain increasing order of chars
        seen = set() # seen tracks if the value is included in stack
        for i, c in enumerate(s):
            if c in seen:
                freq[c] -= 1
                continue
            while st and st[-1] > c and freq[st[-1]] > 0 : # pop to track lex order
                seen.remove(st[-1])
                st.pop()
            st.append(c)
            seen.add(c)
            freq[c] -= 1
        return "".join(st)
