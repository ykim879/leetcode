import random
class RandomizedSet(object):

    def __init__(self):
        self.set = set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            return False
        else:
            self.set.add(val)
            return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            self.set.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.sample(self.set, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
