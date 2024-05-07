class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        lookup = {w:i for i,w in enumerate(words)} # swap key (index) and value (word)
        res = []
        
        for i, w in enumerate(words):
            for j in range(len(w)+1):
                pre, suf = w[:j], w[j:] # prefix and suffix
                
                # prefixes
                if pre == pre[::-1] and suf[::-1] != w and suf[::-1] in lookup:
                    res.append([lookup[suf[::-1]], i]) # palindrome prefix e.g. 'lls' and 's', 'sssll' and 'lls' in Example 1
                        
                # suffixes
                if j != len(w) and suf == suf[::-1] and pre[::-1] != w and pre[::-1] in lookup: # j==len(w) case is already checked above
                    res.append([i, lookup[pre[::-1]]]) # palindrome suffix e.g. 'sll' and 's'
        
        return res