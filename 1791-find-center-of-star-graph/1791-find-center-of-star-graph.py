class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        common = -1
        
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        
        return edges[0][1]