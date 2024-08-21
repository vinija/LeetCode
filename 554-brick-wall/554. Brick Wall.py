class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = {}
        
        for row in wall:
            edge_position = 0
            for i in range(len(row) - 1):
                edge_position += row[i]
                edges[edge_position] = edges.get(edge_position, 0) + 1
        
        max_edges = max(edges.values(), default=0)
        
        return len(wall) - max_edges
