from typing import List, Dict, Tuple
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Computes the minimum time required for all nodes in the network
        to receive a signal sent from node k.

        Parameters:
        times: List of directed edges represented as [u, v, w]
        n: Total number of nodes labeled from 1 to n
        k: Starting node

        Returns:
        Minimum time for all nodes to receive the signal, or -1 if impossible
        """

        # ----------------------------
        # Input validation
        # ----------------------------
        if n <= 0:
            raise ValueError("Number of nodes must be positive.")
        if not (1 <= k <= n):
            raise ValueError("Starting node k must be between 1 and n.")
        if times is None:
            raise ValueError("Times list cannot be None.")

        # ----------------------------
        # Build adjacency list
        # ----------------------------
        graph: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(1, n + 1)}

        for edge in times:
            if len(edge) != 3:
                raise ValueError("Each edge must contain exactly three integers.")
            u, v, w = edge
            if w < 0:
                raise ValueError("Edge weights must be non-negative.")
            if not (1 <= u <= n and 1 <= v <= n):
                raise ValueError("Node labels must be between 1 and n.")
            graph[u].append((v, w))

        # ----------------------------
        # Dijkstra's algorithm
        # ----------------------------
        min_heap: List[Tuple[int, int]] = [(0, k)]
        shortest_time: Dict[int, int] = {}

        while min_heap:
            current_time, node = heapq.heappop(min_heap)

            # Skip if we already found a shorter path
            if node in shortest_time:
                continue

            shortest_time[node] = current_time

            # Explore neighbors
            for neighbor, travel_time in graph[node]:
                if neighbor not in shortest_time:
                    heapq.heappush(
                        min_heap,
                        (current_time + travel_time, neighbor)
                    )

        # ----------------------------
        # Final result
        # ----------------------------
        if len(shortest_time) != n:
            return -1

        return max(shortest_time.values())
