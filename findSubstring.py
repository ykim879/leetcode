from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        len_word = len(words[0])
        total_length = len_word * len(words)
        words = Counter(words)  # Get the frequency of each word
        res = []
        for i in range(len_word):  # Start from each offset within word_length
            l = i
            window = Counter()
            for r in range(i, len(s) - len_word + 1, len_word):
                word = s[r:r + len_word]
                if word in words:
                ### if word is already as much as the whole world: we need to pop l until l is not as same as r 
                    while words[word] == window[word]:
                        window[s[l:l+len_word]] -= 1
                        l += len_word
                    ### append the right pointer and add in counter
                    window[word] += 1
                    ### see if len(sets) == len(window): add index
                    if total_length == r + len_word - l:
                        res.append(l)
                else:
                    l = r + len_word
                    window.clear()
        return res
