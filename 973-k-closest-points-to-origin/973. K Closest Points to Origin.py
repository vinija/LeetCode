import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        max_heap = []

        for x, y in points:
            #calculate the distance from origin
            dist = -(x*x + y*y) #neg b/c python in min heap by default
            
            #push to heap
            heapq.heappush(max_heap, (dist, [x,y]))

            #if heap exceeps k, remove the farthest point
            if len(max_heap) > k:
                heapq.heappop(max_heap)
            
        return [point for (dist,point) in max_heap]