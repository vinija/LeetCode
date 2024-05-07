from typing import List
from heapq import heappush, heappop
import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create graph as adjacency list
        graph = collections.defaultdict(list)
        for start, end, cost in flights:
            graph[start].append((end, cost))

        # Min-heap priority queue
        # (cost, current city, stops used)
        pq = [(0, src, 0)]
        
        # This will keep track of the minimum cost to get to each node with a certain number of stops
        # cost_so_far[node][stops] = cost
        cost_so_far = [[float('inf')] * (k + 2) for _ in range(n)]
        cost_so_far[src][0] = 0

        while pq:
            current_cost, current_city, stops = heappop(pq)

            # If the current city is the destination and within stop limit, return the cost
            if current_city == dst:
                return current_cost

            # If stops are within limit, explore the neighbors
            if stops <= k:
                for neighbor, weight in graph[current_city]:
                    new_cost = current_cost + weight
                    if new_cost < cost_so_far[neighbor][stops + 1]:
                        cost_so_far[neighbor][stops + 1] = new_cost
                        heappush(pq, (new_cost, neighbor, stops + 1))
        
        # Return the minimum cost among all valid stop counts at destination node
        min_cost = min(cost_so_far[dst][:k+2])
        return min_cost if min_cost != float('inf') else -1

