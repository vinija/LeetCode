# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return head
        
        dummy = head.next
        prev = head
        
        while dummy != None:
            
            if dummy.val == prev.val:
                prev.next = dummy.next
                dummy = dummy.next
            else:
                dummy = dummy.next
                prev = prev.next
        
        return head
            
        