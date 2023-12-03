class Solution:
    def minCut(self, s: str) -> int:
        palindromes = {}
        def palindrome(sub):
            L = len(sub)
            res = True
            for i in range(L//2):
                if sub[i] != sub[L - i - 1]:
                    res = False
                    break
            palindromes[sub] = res
            return res
        cuts = {}
        def cutf(sub):
            if sub in cuts:
                return cuts[sub][1]
            L = len(sub)
            reslist = []
            res = False
            for i in range(1, L):
                left = palindromes.get(sub[:i], palindrome(sub[:i]))
                right = palindromes.get(sub[i:], palindrome(sub[i:]))
                reslist.append([sub[:i], sub[i:]])
                if left and right:
                    res = True
                    reslist = [[sub[:i], sub[i:]]]
                    break
            cuts[sub] = (reslist, res)
            return res

        if palindrome(s):
            return 0
        
        beforeLayer = [[s]]
        for c in range(len(s)-1):
            nextLayer = []
            for sublist in beforeLayer:
                for i, sub in enumerate(sublist):
                    if sub not in palindromes:
                        palindrome(sub)
                    if palindromes[sub]:
                        continue
                    valid = cutf(sub)
                    others = list()
                    others.extend(sublist[:i])
                    others.extend(sublist[i+1:])
                    if valid:
                        for other in others:
                            if not palindromes[other]:
                                valid = False
                                break
                    if valid:
                        return c + 1
                    for cut in cuts[sub][0]:
                        nextLayer.append(others + cut)
            beforeLayer = nextLayer
        return len(s) - 1
