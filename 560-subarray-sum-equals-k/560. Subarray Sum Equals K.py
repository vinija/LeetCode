class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cumulative_sum = 0
        sum_freq = defaultdict(int)
        sum_freq[0] = 1

        for num in nums:
            cumulative_sum += num

            if (cumulative_sum - k) in sum_freq:
                count += sum_freq[cumulative_sum - k]
            
            sum_freq[cumulative_sum] += 1
        
        return count