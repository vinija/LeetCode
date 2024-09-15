class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        jumps = 0
        farthest = 0
        current_end = 0

        for i in range(len(nums) -1):
            #update the farthest position we can reach
            farthest = max(farthest, i + nums[i])
            print(farthest)

            #If we reach the end of the current jump range
            if i == current_end:
                jumps += 1 #make a jump
                current_end = farthest #update the end to farthest

                #If the farthest point reaches or exceeds the last index, we can break
                if current_end >= len(nums) - 1:
                    break
        
        return jumps