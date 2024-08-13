class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}  # edge cases: to handle sum equal to multiple of k from start
        cumulative_sum = 0

        for i, num in enumerate(nums):
            cumulative_sum += num

            if k != 0:
                cumulative_sum %= k

            if cumulative_sum in remainder_map:
                if i - remainder_map[cumulative_sum] > 1:
                    return True
            # The correction: only add to the map if the remainder is not already in the map
            if cumulative_sum not in remainder_map:
                remainder_map[cumulative_sum] = i

        return False
