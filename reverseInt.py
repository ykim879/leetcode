class Solution:
    def reverseInt(self, x: int) -> int:
        MIN, MAX = -2 ** 31, 2 ** 31
        res, sign = 0, 1
        if x < 0:
            sign = -1
            x *= -1
        while x > 0:
            res *= 10
            res += x % 10 
            x //= 10
        return sign * res if MIN <= res < MAX else 0
