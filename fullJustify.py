class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line, res, totalLength = [], [], 0
        def leftJustify():
            ele = ""
            for word in line:
                ele += (word + " ")
            return ele[:-1] if len(ele) > maxWidth else ele + (maxWidth - len(ele)) * " "
        for word in words:
            if totalLength + len(word) > maxWidth: #edge case: ""?
                ele = ""
                # justify(line)
                if len(line) == 1:
                    #left justify
                    ele = leftJustify()
                else:
                    ngaps = len(line) - 1
                    space, greedySpace = (maxWidth - totalLength + 1) // ngaps, (maxWidth - totalLength + 1) % ngaps
                    for i, cur in enumerate(line):
                        ele += cur
                        if i < len(line) - 1:
                            ele += " " * (space + 1)
                            if i < greedySpace:
                                ele += " "
                res.append(ele)
                line.clear()
                totalLength = 0
            line.append(word)
            totalLength += (len(word) + 1)
        if len(line) > 0:
            res.append(leftJustify())
        return res
