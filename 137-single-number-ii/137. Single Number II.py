from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)

        for index, value in count.items():
            if value == 1:
                return index
        return -1
        