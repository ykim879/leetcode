class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [] # folders 
        cur = ""
        for c in path + "/":
            if c != "/":
                cur += c
            elif cur:
                match cur:
                    case ".":
                        pass
                    case "..":
                        if stack:
                            stack.pop()
                    case _:
                        stack.append(cur)
                cur = ""                
        return "/" + "/".join(stack)
