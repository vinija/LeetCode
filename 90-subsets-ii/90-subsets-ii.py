class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        self.dfs(nums,[],output)
        return output
    
    def dfs(self,nums:List[int], curr: List[int], output : List[int]):
        
        if curr not in output:
            output.append(curr)
        
        for i in range(len(nums)):
            self.dfs(nums[i+1:],curr+[nums[i]],output)