# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def is_leaf(node):
            return node is not None and node.left is None and node.right is None

        total_sum = 0

        # If the left child exists and is a leaf, add its value to total_sum
        if root.left and is_leaf(root.left):
            total_sum += root.left.val

        # Recursively sum the left leaves in both the left and right subtrees
        total_sum += self.sumOfLeftLeaves(root.left)
        total_sum += self.sumOfLeftLeaves(root.right)

        return total_sum
