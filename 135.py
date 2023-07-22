class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        min_, L, cur, res = 1, len(ratings), 1, 1
        if L == 1:
            return 1

        def recurSum(n):
            res = 0
            for i in range(1, n + 1):
                res += i
            return res
        
        if ratings[0] > ratings[1]:
            res = 0
            
        for i in range(1, L):
            if ratings[i] > ratings[i-1]: #increasing
                cur += 1
                if i < L - 1 and ratings[i] > ratings[i+1]: # if it is peak
                    min_ = cur
                    cur = 1
                else:
                    res += cur
            elif ratings[i-1] > ratings[i]: #decreasing
                cur += 1
                if i == L - 1 or ratings[i] <= ratings[i+1]: # it is valley
                    if min_ > cur:
                        res += (min_ + recurSum(cur - 1))
                    else:
                        res += recurSum(cur)
                    cur = min_ = 1
            else:
                if i < L - 1 and ratings[i] > ratings[i+1]:
                    min_ = cur = 1
                else:
                    cur = 1
                    res += cur
        return res 
