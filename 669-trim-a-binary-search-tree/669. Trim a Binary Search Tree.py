from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # Base case: if the node is None, return None
        if not root:
            return None
        
        # If the current node's value is less than low, we trim the left subtree
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        # If the current node's value is greater than high, we trim the right subtree
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        # Otherwise, the node is within range, so we trim its left and right subtrees
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        # Return the root as it's within the valid range
        return root
