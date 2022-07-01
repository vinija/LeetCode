class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output=[]
        
        self.dfs(s,output,[])
        
        return output
    
    def dfs(self,s,output,currentpath):
        if not s:
            output.append(currentpath)
            return
        
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], output, currentpath+[s[:i]])
            
    def isPal(self,s):
        if(s == s[::-1]):
            return True
        return False