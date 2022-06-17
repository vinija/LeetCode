class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nn = sorted(nums)
        
        def backtrack(temp, start):
            res.append(list(temp))
            for i in range(start, N):
                if i > start and nn[i] == nn[i-1]: continue
                temp.append(nn[i])
                backtrack(temp, i + 1)
                temp.pop()
                
        res = []
        backtrack([], 0)
        return res
        