class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1, v2 = v1.split("."), v2.split(".")
        L1, L2 = len(v1), len(v2)
        l = min(L1, L2)
        # check if either same with minimum arr
        for i in range(l):
            n1, n2 = int(v1[i]), int(v2[i])
            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1
        # if either has longer length and remaining is not 0 return the corresponding
        if L1 > L2:
            for i in range(l, L1):
                if int(v1[i]) > 0:
                    return 1
        elif L1 < L2:
            for i in range(l, L2):
                if int(v2[i]) > 0:
                    return -1
        return 0
