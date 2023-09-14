class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # xor for all nums in list
        s = reduce(xor, nums)
        # find the last 1
        nz = s & (s-1) ^ s 
        # nz represents 1 bit that only one number has between two numbers of result.
        # therefore, filter(lambda n: n & nz, nums) should return include that number but not another number 
        # xor all numbers will return only this number since others will appeeared twice
        num1 = reduce(xor, filter(lambda n: n & nz, nums))

        return (num1, s ^ num1)
