class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        combo = {")" : "(", "}" : "{", "]" : "["}
        for c in s:
            match c:
                case "(" | "{" |"[":
                    stack.append(c)
                case ")" | "}" | "]":
                    if not stack or stack[-1] != combo[c]:
                        return False
                    stack.pop()
        return len(stack) == 0
