class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        result = []

        def dfs(index: int, path: List[int]):
            result.append(path.copy())

            for i in range(index, len(nums)):
                path.append(nums[i])

                dfs(i+1, path)

                path.pop()

        dfs(0,[])
        return result
        