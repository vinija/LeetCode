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
        if root is None:
            return ''
        q = deque([root])
        res = []
        q.append('#')
        while q:
            sz = len(q)
            for _ in range(sz):
                node = q.popleft()
                if node == '#':
                    res.append('#')
                    continue
                # print(node)
                res.append(str(node.val))
                for c in node.children:
                    q.append(c)
                q.append('#')
            # res.append('#')
        return ','.join(res)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        # print(data)
        if len(data) == 0:
            return None
        elements = data.split(',')
        # print(elements)
        while elements[-1] == '#':
            elements.pop()
        # print(elements)
        root = Node(int(elements[0]), [])
        q = deque([root])
        for i in elements[1:]:
            # print(i)
            if i == '#':
                cur = q.popleft()
            else:
                node = Node(int(i), [])
                q.append(node)
                cur.children.append(node)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))