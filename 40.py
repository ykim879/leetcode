class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        from copy import deepcopy,copy
        candidates.sort()
        combinations = defaultdict(list)
        combinations[0].append(list())
        duplicates = 0
        L = len(candidates) - 1

        for i, n in enumerate(candidates):
            if n > target:
                break
            duplicates += 1
            if i < L and n == candidates[i+1]:
                continue
            previousCombinations = deepcopy(combinations)
            for key, valuelist in previousCombinations.items():
                newKey = key
                for d in range(1, duplicates + 1):
                    if newKey > target:
                        break
                    newKey += n
                    for value in valuelist:
                        newValue = copy(value)
                        newValue.extend([n] * d)
                        combinations[newKey].append(newValue)
            duplicates = 0
        return combinations[target]
