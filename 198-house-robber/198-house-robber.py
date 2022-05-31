class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        if len(nums) < 3:
            return max(nums)
        
        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        
        return dp[-1]

        