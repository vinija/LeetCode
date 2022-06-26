class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dct = {}
        for i, n in enumerate(sorted(nums)):
            if n not in dct:
                dct[n] = i
        print(dct)
        #{1: 0, 2: 1, 3: 3, 8: 4}
        return [dct[n] for n in nums]