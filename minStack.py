import heapq
class MinStack(object):

    def __init__(self):
        self.id = 0
        self.h = []
        self.stack = []
        self.deleted = set()
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append((self.id, val))
        heapq.heappush(self.h, (val, self.id))
        self.id += 1

    def pop(self):
        """
        :rtype: None
        """
        id, _ = self.stack.pop()
        self.deleted.add(id)
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

    def getMin(self):
        """
        :rtype: int
        """
        # set () with deleted node, if get min is in deleted node, pop it and after pop it as well
        val, id = self.h[0]
        while id in self.deleted:
            heapq.heappop(self.h)
            val, id = self.h[0]
        # want to track next min
        return val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
