class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(first = 1, curr = []):
            if len(curr) == k:
                #The [:] makes a shallow copy of the array, hence allowing you to modify your copy without damaging the original.
                result.append(curr[:])
            
            for index in range(first, n+1):
                curr.append(index)
                backtrack(index+1,curr)
                curr.pop()

        
        result = []
        backtrack()
        return result
        