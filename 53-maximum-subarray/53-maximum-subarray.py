class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -math.inf
        currSum = -math.inf
        
        for num in nums:
            currSum = max(num, currSum+num)
            maxSum = max(currSum,maxSum)
        
        return maxSum