from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []

        for index, value in count.items():
            if value > 1:
                res.append(index)
        
        return res
        