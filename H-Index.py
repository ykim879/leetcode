class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # sort the citations and from the end if num(papers) >= citations[i]: return citations[i]
        citations.sort()
        for i in range(len(citations) - 1, -1, -1):
            if len(citations) - i >= citations[i]:
                return max(citations[i], len(citations) - i - 1)
        return len(citations)
