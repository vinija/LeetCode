"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def traverse(node):
            if not node:
                return
            
            for child in node.children:
                traverse(child)
            
            result.append(node.val)
        traverse(root)

        return result