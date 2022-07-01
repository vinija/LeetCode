"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def get_depth(self, p):
		# helper function to find the depth of the pointer in the tree
        depth = 0
        while p:
            p = p.parent
            depth += 1
        return depth
    
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
		# find the depth of each pointer
        p_depth = self.get_depth(p)
        q_depth = self.get_depth(q)
		
		# Move the lower pointer up so that they are each at the same level. 
		# For the smaller depth (p_depth < q_depth or q_depth < p_depth), 
		# the loop will be skipped and the pointer will stay at the same depth.
        for _ in range(p_depth - q_depth):
            p = p.parent
        for _ in range(q_depth - p_depth):
            q = q.parent
        
		# Now that they are at the same depth, move them up the tree in parallel until they meet
        while p != q:
            p=p.parent
            q=q.parent
        return p