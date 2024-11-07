class Solution:
    def removeDuplicates(self, s: str) -> str:
        # stack: last element and return of stack will result
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
