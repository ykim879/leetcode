class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # if there is only 2 character is difference 
        stack = [] # maximum length should be 2
        for idx in range(len(s)):
            if s[idx] != goal[idx]:
                if len(stack) == 2:
                    return False
                stack.append(idx)
        # and two string reverse are same
        if len(stack) == 0 and len(set(s)) < len(s):
            return True
        if len(stack) <= 1 or s[stack[0]] != goal[stack[1]] or s[stack[1]] != goal[stack[0]] :
            return False
        return True
        
