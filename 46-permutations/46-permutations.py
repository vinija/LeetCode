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
    #in the first level of the tree, you have N options and for each of the option, you have N-1 option, and for each of these N-1 options, you have another N-2 options, so putting them together you would end up N*(N-1)*(N-2).... = N!