# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path, paths):
            if node:
                path += str(node.val)
                if not node.left and not node.right:  # If leaf node, add path to results
                    paths.append(path)
                else:
                    path += "->"  # Add the arrow to indicate the path continuation
                    dfs(node.left, path, paths)
                    dfs(node.right, path, paths)

        paths = []
        dfs(root, "", paths)
        return paths
