class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        #If target is out of the possible range, return 0
        if total_sum < abs(target) or (total_sum + target) %2 != 0:
            return 0
        
        #calculate the required subset sum
        # (P+N) + (P-N) = total_sum + target
        # P = total_sum + target // 2
        subset_sum = (total_sum + target) // 2

        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j-num]
        
        return dp[subset_sum]


