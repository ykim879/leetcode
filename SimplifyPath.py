class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        directories = path.split("/")
        stack = []
        for directory in directories:
            if len(directory) == 0 or directory == ".":
                continue
            elif directory == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(directory)
        res = ""
        for s in stack:
            res += "/" + s
        if len(res) == 0:
            return "/"
        return res
