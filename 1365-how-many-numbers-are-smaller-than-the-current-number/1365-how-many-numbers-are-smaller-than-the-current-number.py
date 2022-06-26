class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dct = {}
        for i, n in enumerate(sorted(nums)):
            if n not in dct:
                dct[n] = i
        return [dct[n] for n in nums]