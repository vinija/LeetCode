class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictionary = {}
        
        for word in strs:
            sortedWord = "".join(sorted(word))
            
            if sortedWord in dictionary:
                dictionary[sortedWord].append(word)
            else:
                dictionary[sortedWord] = [word]
        
        return dictionary.values()
        

        