class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # split the number using "."
        # by using two pointer compare until non of them are "0"
        version1 = version1.split(".")
        version2 = version2.split(".")
        print(version1, version2)
        for i in range(min(len(version1), len(version2))):
            # eliminate leading 1
            ver1, ver2 = version1[i], version2[i]
            v1, v2 = 0, 0
            L1, L2 = len(ver1), len(ver2)

            while v1 < L1 and ver1[v1] == "0":
                v1 += 1
            while v2 < L2 and ver2[v2] == "0":
                v2 += 1
            
            if (L1 - v1) > (L2 - v2):
                return 1
            elif (L1 - v1) < (L2 - v2):
                return -1
            
            while v1 < L1 and v2 < L2:
                if ver1[v1] > ver2[v2]:
                    return 1
                elif ver1[v1] < ver2[v2]:
                    return -1
                v1 += 1
                v2 += 1
        
        for i in range(len(version1), len(version2)):
            ver = version2[i]
            for v in ver:
                if v != "0":
                    return -1
        for i in range(len(version2), len(version1)):
            ver = version1[i]
            for v in ver:
                if v != "0":
                    return 1      
        
        return 0
