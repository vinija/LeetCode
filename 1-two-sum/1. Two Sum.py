from typing import Dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mapSum = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in mapSum:
                return [mapSum[complement], index]
            mapSum[value] = index
      