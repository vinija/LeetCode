class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        #traverse the string
        #keep track of the status of delete or not delete current character
        #the status includes current index, number of delete, the previous character, and the runing length of previous character
        #return the minium length of compresed between delete or not delete
		#O(n^2*26*k) = O(n^2*k) time and space
        
        memo = {}
        return self.dfs(s, 0, k, None, 0, memo)
    
    def dfs(self, s, i, k, prev, l, memo):
        if i == len(s):
            return 0
        if (i, k, prev, l) in memo:
            return memo[(i, k, prev, l)]
        
        if k > 0:
            delete = self.dfs(s, i + 1, k - 1, prev, l, memo)
        else:
			#in this case, we cannot delete, set it as INF to choose skip in the end
            delete = float("inf")
        
        if s[i] == prev:
		    #need one more digit for the count
            carry = 1 if l == 1 or len(str(l + 1)) > len(str(l)) else 0
            skip = carry + self.dfs(s, i + 1, k, s[i], l + 1, memo)
        else:
            skip = 1 + self.dfs(s, i + 1, k, s[i], 1, memo)
        
        memo[(i, k, prev, l)] = min(delete, skip)
        
        return memo[(i, k, prev, l)]