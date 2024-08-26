from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index: int, currTarget: int, path: List[int]):
            # Base case: If current target is 0, we've found a valid combination
            if currTarget == 0:
                result.append(path)
                return
            # If current target is less than 0, no valid combination can be found from here
            if currTarget < 0:
                return

            # Loop through candidates starting from the current index
            for i in range(index, len(candidates)):
                # Recurse with the same index (to allow using the same element) and decreased target
                dfs(i, currTarget - candidates[i], path + [candidates[i]])

        if not candidates or target <= 0:
            return []

        result = []
        dfs(0, target, [])
        return result
