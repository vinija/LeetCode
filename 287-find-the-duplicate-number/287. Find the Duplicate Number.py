from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        for num, count in counter.items():
            if count > 1:
                return num

        return 0

        