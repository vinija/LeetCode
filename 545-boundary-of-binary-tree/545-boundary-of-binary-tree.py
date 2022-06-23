class Solution(object):
    def boundaryOfBinaryTree(self, root):
        def dfs_leftmost(node): # preorder
            if not node or (not node.left and not node.right):
                return
            boundary.append(node.val)
            
            if node.left:
                dfs_leftmost(node.left)
            else:
                dfs_leftmost(node.right)
                
        def dfs_rightmost(node): # postorder
            if not node or not node.left and not node.right:
                return
            if node.right:
                dfs_rightmost(node.right)
            else:
                dfs_rightmost(node.left)
            boundary.append(node.val)

        def dfs_leaves(node): # inorder
            if not node:
                return
            dfs_leaves(node.left)
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
            dfs_leaves(node.right)
            
        if not root:
            return []
        
        boundary = [root.val] # place root here first
        
        dfs_leftmost(root.left)
        dfs_leaves(root)
        dfs_rightmost(root.right)
        
        return boundary