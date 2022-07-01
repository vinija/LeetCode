class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPal = ""
    
        for index, word in enumerate(s):
            maxPal = max(maxPal, self.expandFromCenter(s,index,index), self.expandFromCenter(s,index,index+1),key=len)
        return maxPal
    
    def expandFromCenter(self,s,left,right) -> str:
        
        while(right< len(s) and left>=0 and s[left]==s[right]):
            left -=1
            right +=1
        
        return s[left+1:right]