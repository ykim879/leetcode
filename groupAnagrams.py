class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for word in strs:
            # Sort the word to create the key
            key = tuple(sorted(word))
            anagrams[key].append(word)
        
        # Convert the values in the dictionary to a list of lists
        return list(anagrams.values())
