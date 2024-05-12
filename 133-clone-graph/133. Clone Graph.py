"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        def dfs(oldNode):
            if oldNode in old_to_new:
                return old_to_new[oldNode]
        
            copy = Node(oldNode.val)
            old_to_new[oldNode] = copy

            for neighbor in oldNode.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy

        return dfs(node)