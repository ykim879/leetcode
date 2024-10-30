class Solution:
    def countOrders(self, n: int) -> int:
        # p[i] < d[i]
        ## p[i]: doesn't any constraint  when we are adding d[i] it is only possible d[i] is in the path
        # when ever we have element i, chose two integers (index) that is able us to place the element in the list of order
        ## i1, i2 : i1 < i2
        ## mathematical approach
        # n, n *2, n (n-2)//2 decrease n by 2 
        res, mod = 1, 10**9 + 7
        for fact in range(1, 2*n+1):
            res *= fact
        return (res // 2 **n ) % mod
