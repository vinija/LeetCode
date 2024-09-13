# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: Perform inorder traversal to get the nodes in sorted order
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

        # Step 2: Build a balanced BST from a sorted list of values
        def build_balanced_bst(sorted_vals):
            if not sorted_vals:
                return None
            mid = len(sorted_vals) // 2
            root = TreeNode(sorted_vals[mid])
            root.left = build_balanced_bst(sorted_vals[:mid])
            root.right = build_balanced_bst(sorted_vals[mid + 1:])
            return root

        # Get the sorted list of values from the BST
        sorted_vals = inorder_traversal(root)

        # Rebuild the balanced BST from the sorted list
        return build_balanced_bst(sorted_vals)
