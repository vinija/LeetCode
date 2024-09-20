from typing import List, Dict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {} 

        for s in strs:

            sorted_str = tuple(sorted(s))

            if sorted_str not in anagramDict:
                anagramDict[sorted_str] = [] #init a list if key doesn't exist
            
            anagramDict[sorted_str].append(s)
        
        #Return the grouped anagrams(values of the dictionary)
        return list(anagramDict.values())
            
