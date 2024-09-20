from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])  # Initialize the queue with the root node
        
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            level = []  # List to store the values of the current level
            
            for _ in range(level_size):
                node = queue.popleft()  # Pop the leftmost node from the queue
                level.append(node.val)  # Append its value to the level list
                
                # Add the left and right children of the current node to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Append the current level to the result
            result.append(level)
        
        return result
