# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        #Helper function returns deepest nodes
        def dfs(node):
            #Base case if node is None, return depth -1 and no subtree
            if not node:
                return -1, None
            
            #Recurse the left and right subtree
            left_depth, left_subtree = dfs(node.left)
            right_depth, right_subtree = dfs(node.right)

            if left_depth == right_depth:
                return left_depth + 1, node
            
            elif left_depth > right_depth:
                return left_depth + 1, left_subtree
            
            else:
                return right_depth + 1, right_subtree
        
        return dfs(root)[1]