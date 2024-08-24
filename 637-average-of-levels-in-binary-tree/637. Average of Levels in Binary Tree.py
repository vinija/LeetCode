from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        # Queue for BFS
        queue = deque([root])
        averages = []
        
        # BFS traversal
        while queue:
            level_sum = 0
            level_count = len(queue)
            
            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Calculate the average for this level
            level_average = level_sum / level_count
            averages.append(level_average)
        
        return averages
