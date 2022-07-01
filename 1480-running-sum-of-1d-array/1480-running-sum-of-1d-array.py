class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        currSum = 0
        output = []
        
        for index, value in enumerate(nums):
            output.append(currSum + value)
            currSum += value
        
        return output 