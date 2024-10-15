class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for c in s:
            if stack and ((stack[-1] == "A" and c == "B") or (stack[-1] == "C" and c == "D")):
                stack.pop()
                continue
            stack.append(c)
        return len(stack)  
