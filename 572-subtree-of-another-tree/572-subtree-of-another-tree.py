# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        
        def isSame(root:Optional[TreeNode], subRoot: Optional[TreeNode])-> bool:
            
            if not root and not subRoot:
                return True
            
            if not root or not subRoot:
                return False
            
            if root.val != subRoot.val:
                return False
            
            return isSame(root.left, subRoot.left) and isSame(root.right,subRoot.right)
        
        if isSame(root,subRoot) :
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)