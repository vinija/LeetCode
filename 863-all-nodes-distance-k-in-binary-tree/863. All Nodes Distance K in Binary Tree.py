from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Helper function to map each node to its parent
        def map_parents(node, parent=None):
            if node:
                parent_map[node] = parent
                map_parents(node.left, node)
                map_parents(node.right, node)

        # Edge case: if root is None
        if not root:
            return []

        # Dictionary to store parent references
        parent_map = {}
        map_parents(root)

        # BFS starting from the target node
        queue = deque([(target, 0)])
        visited = {target}
        result = []

        while queue:
            node, distance = queue.popleft()
            
            # If the current node is at distance k, add it to the result
            if distance == k:
                result.append(node.val)
            
            # Explore the neighbors: left child, right child, and parent
            for neighbor in (node.left, node.right, parent_map[node]):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
        
        return result
