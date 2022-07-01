class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
#         currSum = 0
#         output = []
        
#         for index, value in enumerate(nums):
#             output.append(currSum + value)
#             currSum += value
        
#         return output 

        dp = [0] * (len(nums)+1)
        
        
        for index in range(1,len(nums)+1):
            dp[index] = dp[index-1]+nums[index-1]
        
        
        return dp[1:]