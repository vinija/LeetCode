class Solution:
    def arraySign(self, nums: List[int]) -> int:
        currMult = 1
        for value in nums:
            currMult *=value
        
        if currMult == 0:
            return 0
        elif currMult > 0:
            return 1
        return -1