from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []

        for key, value in count.items():
            if value == 1:
                res.append(key)

        return res


        