# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            levelSize = len(queue)
            levelMax = float('-inf') #max value for this level

            for _ in range(levelSize):
                node = queue.popleft()
                levelMax = max(node.val, levelMax)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(levelMax)

        return result
        