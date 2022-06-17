# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root,root)
    
    def isMirror(self, first, second):
        if not first and not second: return True
        if not first or not second: return False
        
        return first.val == second.val and self.isMirror(first.right,second.left) and self.isMirror(first.left,second.right)
        