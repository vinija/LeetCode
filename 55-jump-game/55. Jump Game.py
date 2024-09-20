class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0 #Track the furthest jump thus far

        for i in range(len(nums)):
            #If the current index is beyond farthest reachable index, return false
            if i > farthest:
                return False
            
            #Update the farthest reachable index
            farthest = max(farthest, i + nums[i])

            if farthest >= len(nums) -1:
                return True

        
        return False