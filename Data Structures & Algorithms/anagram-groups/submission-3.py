class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        # store the string in alphabetical order and then check if that key exist, add the index to the group 
        for s in strs:
            alphabetical = "".join(sorted(s))
            if alphabetical in anagrams:    
                anagrams[alphabetical].append(s)
            else: 
                anagrams[alphabetical] = [s]
        return list(anagrams.values())