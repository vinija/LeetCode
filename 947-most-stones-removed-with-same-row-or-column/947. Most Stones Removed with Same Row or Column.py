from typing import List, Set, Tuple
from collections import defaultdict

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(x: int, y: int):
            visited.add((x,y))
            for nx, ny in row_map[x] + col_map[y]:
                if (nx, ny) not in visited:
                    dfs(nx, ny)
        
        # Maps to store stones by row and column
        row_map = defaultdict(list)
        col_map = defaultdict(list)

        # Populate the maps
        for x, y in stones:
            row_map[x].append((x,y))
            col_map[y].append((x,y))
        
        visited = set()
        num_connected_components = 0

        # Perform DFS for each unvisited stone
        for x, y in stones:
            if (x,y) not in visited:
                dfs(x,y)
                num_connected_components += 1
        
        return len(stones) - num_connected_components