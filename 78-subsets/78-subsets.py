class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, currentPath, answer):
            #if currentPath not in answer:
            answer.append(currentPath)
                
            for i in range(len(nums)):
                dfs(nums[i+1:], currentPath + [nums[i]], answer)        
        
        answer = []
        dfs(nums, [], answer)
        return answer