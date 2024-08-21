class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt = 0
        
        def sumTree(node):
            if not node:
                return 0
            left_sum = sumTree(node.left)
            right_sum = sumTree(node.right)
            self.total_tilt += abs(left_sum - right_sum)
            return node.val + left_sum + right_sum
        
        sumTree(root)
        return self.total_tilt
