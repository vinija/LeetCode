class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        currJumpEnd = 0
        farthest = 0
        
        for index in range(len(nums)-1):
            farthest = max(farthest, index+nums[index])
            
            #if we've reached the end of currJump and need another jump
            if index == currJumpEnd:
                jump+=1
                currJumpEnd = farthest
        
        return jump