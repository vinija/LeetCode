"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ''
        
        def helper(x: 'Node') -> List:
            if x:
                return [[i.val,helper(i)] for i in x.children]
        
        return [root.val, helper(root)]
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        def helper(vals):
            if not vals:
                return
            
            k = vals[0]
            for i in vals[1:]:
                node = Node(k)
                node.children = [helper(x) for x in i]
                return node
            
        return helper(data)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))