from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1# base case

        for num in nums:
            next_dp = defaultdict(int)
            for current_sum in dp:
                next_dp[current_sum + num] += dp[current_sum]
                next_dp[current_sum - num] += dp[current_sum]
            dp = next_dp
        
        return dp[target]

        