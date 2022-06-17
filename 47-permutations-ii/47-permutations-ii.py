class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        
        def backtrack(currPath, nums):
            
            if not nums and currPath[:] not in output:
                output.append(currPath[:])
                
            for index in range(len(nums)):
                currPath.append(nums[index])
                backtrack(currPath,nums[:index] + nums[index+1:])
                currPath.pop()
            
        
        backtrack([], nums)
        return output