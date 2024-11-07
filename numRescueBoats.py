class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        # Premise: we want to know how many boats to carry all people where at most this both can handle limit
        l, r = 0, len(people) - 1
        res = 0
        while l < r:
            if people[r] + people[l] <= limit:
                r -= 1
                l += 1
            else:
                r -= 1
            res += 1
        return res + 1 if l == r else res
