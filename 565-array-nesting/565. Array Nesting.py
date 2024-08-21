class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        max_len = 0
        
        for i in range(len(nums)):
            if not visited[i]:
                start = i
                count = 0
                while not visited[start]:
                    visited[start] = True
                    start = nums[start]
                    count += 1
                max_len = max(max_len, count)
        
        return max_len
