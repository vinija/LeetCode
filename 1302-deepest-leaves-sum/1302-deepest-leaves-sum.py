# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        
        def traverseDepths(depth, currList, node):
            if depth == currList[0]:
                currList[1] += node.val
            elif depth > currList[0]:
                currList[0] = depth
                currList[1] = node.val               
            
            if node.left:
                traverseDepths(depth + 1, currList, node.left)
            if node.right:
                traverseDepths(depth + 1, currList, node.right)
        
        res = [0, 0]
        traverseDepths(0, res, root)
        
        return res[1]
        