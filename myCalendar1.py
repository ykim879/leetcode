from sortedcontainers import SortedDict
class MyCalendar(object):

    def __init__(self):
        self.c = SortedDict()

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if start in self.c:
            return False
        # for each start, we want to see the start is smaller doesn't intersact with current start and end
        smaller = self.c.bisect_left(start) - 1
        if smaller >= 0 and self.c.values()[smaller] > start:
            return False
        # for start, check if the end is not intersact witt the start of right
        smaller += 1
        if smaller < len(self.c) and self.c.keys()[smaller] < end:
            return False
        self.c[start] = end
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
