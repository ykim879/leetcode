class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        spells = [(s, i ) for i, s in enumerate(spells)]
        spells.sort(reverse= True)
        S, P = len(spells), len(potions) - 1
        res = [0 for _ in range(S)]
        s = 0
        for spell, i in spells:
            if spell * potions[s] >= success:
                res[i] = s
            else:
                e = P
                if spell * potions[e] < success:
                    res[i] = 0
                    break
                # binary search
                while s < e:
                    mid = (s+e) // 2
                    if spell * potions[mid] >= success:
                        if spell * potions[mid - 1] < success:
                            s = mid
                            break
                        e = mid - 1
                    else:
                        s = mid + 1
            res[i] = P - s + 1
        return res
