# time: O(n^2)
# space: O(n) to store visit list

class Solution:
    def findCircleNum(self, arr: List[List[int]]) -> int:
        ret = 0
        visited = set()
        def markSurr(x):
        
            for index, conn in enumerate(arr[x]):
                if conn and index not in visited:
                    visited.add(index)
                    markSurr(index)
        
        
        
        
        for i in range(len(arr)):
            if i not in visited:
                ret += 1
                visited.add(i)
                markSurr(i)
                
                
        return ret