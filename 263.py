class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        primes = [2,3,5]
        while n > 1:
            prime = -1
            for k in primes:
                if n % k == 0:
                    prime = k
                    break
            if prime > 0:
                n = n // prime
            else:
                return False
        return True
