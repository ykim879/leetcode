class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for c in tokens:
            if c.isdigit() or (c != "-" and c[0] == "-"):
                stack.append(int(c))
            else:
                right = stack.pop()
                left = stack.pop()
                if c == "+":
                    stack.append(right + left)
                elif c == "-":
                    stack.append(left - right)
                elif c == "/":
                    stack.append(int(float(left)/right))
                elif c == "*":
                    stack.append(left * right)
            
        return stack.pop()
