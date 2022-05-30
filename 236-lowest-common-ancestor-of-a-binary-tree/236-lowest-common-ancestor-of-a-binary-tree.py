# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        
        leftRes = self.lowestCommonAncestor(root.left,p,q)
        rightRes = self.lowestCommonAncestor(root.right,p,q)
        
        if (leftRes and rightRes) or (root in [p,q]):
            return root
        else:
            return leftRes or rightRes
        