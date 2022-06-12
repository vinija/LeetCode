class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = {}
        
        def dfs(indexS1, indexS2):
            #we've reached the end of both the strings base case
            if indexS1 == len(s1) and indexS2 == len(s2):
                return True
            #we've already seen this index combination
            if (indexS1, indexS2) in dp:
                return dp[(indexS1, indexS2)]
            #meat of the logic, valid index, and make sure the current index of s1 == indexS1 + indexs2 of s3 and run dfs with incrementing it once more
            if indexS1 < len(s1) and s1[indexS1] == s3[indexS1 + indexS2] and dfs(indexS1 + 1, indexS2):
                return True
            if indexS2 < len(s2) and s2[indexS2] == s3[indexS1 + indexS2] and dfs(indexS1, indexS2 + 1):
                return True
            
            #if false, we need to record it
            dp[(indexS1, indexS2)] = False
            
            return False
        
        return dfs(0, 0)