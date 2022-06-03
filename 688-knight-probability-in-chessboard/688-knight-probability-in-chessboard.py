class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        memo={}
        def helper(x,y,total):
            if (x,y,total) in memo: return memo[(x,y,total)]
            if not (0<=x<n and 0<=y<n): return 0
            if total==0: return 1
            res=0
            for addX,addY in [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]:
                res+=helper(x+addX,y+addY,total-1)
            memo[(x,y,total)]=res
            return res
        
        return helper(row,column,k)/8**k