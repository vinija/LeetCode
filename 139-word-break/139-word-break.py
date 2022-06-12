class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict)
        
        dp = [False] * (len(s)+1)
        
        dp[0] = True
        #dp will only be true at the index it has found the word at
        for index in range(1,len(s)+1):
           
            for subIndex in range(index):
                if dp[subIndex] and s[subIndex:index] in wordSet:
                    dp[index] = True
                    break
        print(dp)
        return dp[len(s)]