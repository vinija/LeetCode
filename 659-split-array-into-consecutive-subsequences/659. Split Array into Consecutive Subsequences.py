from collections import defaultdict

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # Frequency of each number
        freq = defaultdict(int)
        # Dictionary to track how many subsequences end at a specific number
        end = defaultdict(int)
        
        # Count frequency of each number in nums
        for num in nums:
            freq[num] += 1
        
        # Iterate over each number in the nums array
        for num in nums:
            if freq[num] == 0:
                continue
            
            # If there's a subsequence ending with num - 1, extend it with num
            if end[num - 1] > 0:
                end[num - 1] -= 1
                end[num] += 1
                freq[num] -= 1
            # Else, try to form a new subsequence num, num+1, num+2
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num] -= 1
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                end[num + 2] += 1
            else:
                return False
        
        return True
