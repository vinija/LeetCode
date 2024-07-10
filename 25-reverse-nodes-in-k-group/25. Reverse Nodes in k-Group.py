class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse a single group
        def reverse(head, k):
            new_head, ptr = None, head
            while k:
                next_node = ptr.next
                ptr.next = new_head
                new_head = ptr
                ptr = next_node
                k -= 1
            return new_head
        
        # Count the number of nodes in the list
        count = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            count += 1
        
        # Initialize pointers
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        # While there are enough nodes left to form a complete group
        while count >= k:
            # Remember the start of this segment
            kth = group_prev
            for i in range(k):
                kth = kth.next
            group_next = kth.next
            
            # Reverse this part
            new_head = reverse(group_prev.next, k)
            
            # Connect reversed part to the previously processed list
            tail = group_prev.next
            group_prev.next = new_head
            tail.next = group_next
            
            # Move to the next segment
            group_prev = tail
            count -= k
        
        return dummy.next
