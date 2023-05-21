class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l <= r:
            vl, vr = numbers[l], numbers[r]
            if vl + vr == target:
                if l == r:
                    if numbers[l-1] + vl == target:
                        return [l, l+1]
                    else:
                        return [l+1, l+2]
                return [l+1, r+1]
            mid = (l + r) // 2
            # the fast forward to compare with mid
            if vl + numbers[mid] > target:
                r = mid - 1
            elif vr + numbers[mid] < target:
                l = mid + 1
            # either case we will just compare the value of themselves
            elif vl + vr < target:
                l += 1
            else:
                r -= 1
