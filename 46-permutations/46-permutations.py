class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def backtrack(perm, nums):
            
            if not nums:
                res.append(perm[:])
                
            for i in range(len(nums)):
                perm.append(nums[i])
                backtrack(perm, nums[:i] + nums[i+1:])
                perm.pop()
        
        backtrack([], nums)
        return res