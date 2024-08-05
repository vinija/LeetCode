# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Helper function to perform in-order traversal and collect nodes' values
        def inorder_traversal(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        # Helper function to build a balanced BST from sorted values
        def build_balanced_bst(values: List[int]) -> Optional[TreeNode]:
            if not values:
                return None
            mid = len(values) // 2
            root = TreeNode(values[mid])
            root.left = build_balanced_bst(values[:mid])
            root.right = build_balanced_bst(values[mid+1:])
            return root
        
        # Step 1: Get sorted list of values from the unbalanced BST
        sorted_values = inorder_traversal(root)
        
        # Step 2: Build and return the balanced BST from the sorted values
        return build_balanced_bst(sorted_values)

# Time Complexity: O(n) for in-order traversal + O(n) for building balanced BST = O(n)
# Space Complexity: O(n) for storing sorted values + O(log n) for recursion stack (balanced tree) = O(n)
        