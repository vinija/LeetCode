class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_len = 0
        zero_count = 0

        for right in range(len(nums)):
            #if we encounter a 0, increment count for zero
            if nums[right] == 0:
                zero_count += 1
            
            #while num of 0's > k, move left pointer over
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -=1
                left += 1
            
            max_len = max(max_len, right - left + 1)

        return max_len
        