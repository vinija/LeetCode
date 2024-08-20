class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Determine the length of the list and make it circular
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        # Now current is the last node
        current.next = head  # Make the list circular
        
        # Step 2: Find the new head and tail
        k = k % length
        steps_to_new_head = length - k
        
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        
        # Step 3: Break the circle
        new_tail.next = None
        
        return new_head
