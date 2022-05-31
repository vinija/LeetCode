class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:  # sum has to be even to be split in subsets
            return False
        
        s = sum(nums)
        dp = [True]+[False]*s
        
        # Now, loop through each element
        for num in nums:
            for curr in range(s, num-1, -1):  # avoid going out-of-bounds
                """
                Case 1: The current sum (curr) has been seen before.
                        Then, if we don't select the current element, the sum will not change.
						So, this total sum will still exist, and its dp value remains True.
				
				Case 2: The current sum (curr) has not been seen before,
				        but it can be obtained by selecting the current element.
						This means that dp[curr-num] = True, and thus dp[curr] now becomes True.
				
				Case 3: The current sum (curr) has not been seen before,
				        and it cannot be obtained by selecting the current element.
						So, this total sum will still not exist, and its dp value remains False.
                """
                dp[curr] = dp[curr] or dp[curr-num]
        # Finally, we want to obtain the target sum
        return dp[s//2]  # or dp[s>>1]

