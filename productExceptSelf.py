class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # count the number of 0
        totalProd, count0 = 1, 0
        for n in nums:
            if n == 0:
                count0 += 1
            else:
                totalProd *= n
        if count0:
            return [ 0 if n != 0 else totalProd for n in nums] if count0 == 1 else [0 for _ in nums]
        return [totalProd//n for n in nums]
