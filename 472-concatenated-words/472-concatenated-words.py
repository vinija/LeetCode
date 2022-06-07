# ORIGINAL POST WITH EXPLANATION: https://leetcode.com/problems/concatenated-words/discuss/871866/Easyway-Explanation-every-step
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d = set(words)
        
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in d and suffix in d:
                    return True
					
                if prefix in d and dfs(suffix):
                    return True
                
            
            return False
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        
        return res