# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node, low = -math.inf, high = math.inf)->bool:
            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            
            return (isValid(node.right,node.val,high) and isValid(node.left, low, node.val))
        
        return isValid(root)