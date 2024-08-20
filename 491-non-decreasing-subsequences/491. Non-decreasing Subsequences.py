from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int, path: List[int]):
            if len(path) > 1:
                result.add(tuple(path))
            
            used = set()
            for i in range(start, len(nums)):

                if (not path or nums[i] >= path[-1]) and nums[i] not in used:
                    used.add(nums[i])
                    backtrack(i + 1, path + [nums[i]])
        
        result = set()
        backtrack(0, [])
        return list(result)
        