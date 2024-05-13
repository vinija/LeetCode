class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        
        n = len(passingFees)

        graph = collections.defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v,t))
            graph[v].append((u,t))

        heap = [(passingFees[0], 0, 0)]
        minCostAtTime = collections.defaultdict(lambda: float('inf'))
        minCostAtTime[(0,0)] = passingFees[0]

        while heap:
            currentCost, currentTime, u = heappop(heap)

            if u == n - 1:
                return currentCost
            
            for v, time in graph[u]:
                newTime = currentTime + time
                if newTime <= maxTime:
                    newCost = currentCost + passingFees[v]

                    if newCost < minCostAtTime[(v, newTime)]:
                        minCostAtTime[(v, newTime)] = newCost
                        heappush(heap, (newCost, newTime, v))

        return -1