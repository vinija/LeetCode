from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        a, res = [], -1
        for r in matrix:
            for e in r:
                heappush(a, e)

        for _ in range(k):
            res = heappop(a)    
        return res