class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        self.dfs(candidates,target,[],output,0)
        
        return output
    
    def dfs(self,candidates:List[int], target: int, currentPath:List[int], output:List[int],start:int):
        
        if target == 0:
            output.append(currentPath)
            return
        if target <0:
            return
        
        for index in range(start,len(candidates)):
            self.dfs(candidates,target-candidates[index], currentPath +[candidates[index]], output,index)