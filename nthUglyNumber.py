class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        lcd1, lcd2, lcd3, lcd4 = lcm(a,b), lcm(a,c), lcm(b,c), lcm(a,b,c)

        def checkPlace(c, n1, n2, lcd1, lcd2, lcd3, lcd4):
            return c//n1 + c// n2 - c//lcd1 - c//lcd2 - c//lcd3 + c//lcd4

        for k, n1, n2 in [(a,b,c), (b,a,c) , (c, a, b)]:
            start, end = 1, n
            while start <= end:
                m = (start + end) // 2
                c = k * m
                i = m + checkPlace(c, n1, n2, lcd1, lcd2, lcd3, lcd4)
                print(k,c,m,i)
                if i == n:
                    return c
                if i < n:
                    start = m + 1
                else:
                    end = m - 1
        return -1
