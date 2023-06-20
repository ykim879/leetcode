class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        stack = []
        remainingLength = maxWidth
        res = []
        for word in words:
            l = len(word)
            if not stack:
                remainingLength -= l
                stack.append(word)
            elif remainingLength >= l + 1:
                remainingLength -= (l + 1)
                stack.append(word)
            else:
                if len(stack) <= 1:
                    s = stack[0]
                    for _ in range(remainingLength):
                        s += " "
                    res.append(s)
                else:
                    s = stack[0]
                    k = len(stack) - 1
                    a = remainingLength // k
                    r = remainingLength % k
                    for i in range(1, len(stack)):
                        s += " "
                        for _ in range(a):
                            s += " "
                        if i <= r:
                            s += " "
                        s += stack[i]
                    res.append(s)
                stack = [word]
                remainingLength = (maxWidth - l)
        #take care of last
        s = stack[0]
        for i in range(1, len(stack)):
            s += (" " + stack[i])
        for _ in range(remainingLength):
            s += " "
        res.append(s)
        return res
