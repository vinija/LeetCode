class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        result = []

        def backtrack(start, comb, remaining):
            #if comb valid, add to result
            if len(comb) == k and remaining == 0:
                result.append(list(comb))
                return
            
            if len(comb) > k or remaining < 0:
                return
            
            for i in range(start, 10):
                comb.append(i)
                backtrack(i+1, comb, remaining - i)
                comb.pop()
        backtrack(1, [], n)
        return result
        