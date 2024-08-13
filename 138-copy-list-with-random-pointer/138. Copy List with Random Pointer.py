"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Copy each node and insert next to original node
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        # Assign random pointers to the copied node
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        #Separate the copied list from original
        current = head
        copied_head = head.next
        copied_current = copied_head
        while current:
            current.next = current.next.next
            if copied_current.next:
                copied_current.next = copied_current.next.next
            current = current.next
            copied_current = copied_current.next
        
        return copied_head
        