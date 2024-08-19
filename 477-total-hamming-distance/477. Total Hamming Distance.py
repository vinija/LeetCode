class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total_distance = 0
        n = len(nums)

        for bit in range(32):
            count_ones = 0

            for num in nums:
                if (num >> bit) & 1:
                    count_ones += 1
            
            count_zeroes = n - count_ones
            total_distance += count_ones * count_zeroes
        
        return total_distance
        