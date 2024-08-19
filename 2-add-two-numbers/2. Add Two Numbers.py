# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        done = False   
        l1_node = l1
        l2_node = l2
        result_l = ListNode()
        r_next = result_l     
        while not done:
            l1_val = l1_node.val if l1_node is not None else 0 
            l2_val = l2_node.val if l2_node is not None else 0
            val = l1_val + l2_val + carry    
            if val > 9:
                val = val % 10
                carry = 1
            else:
                carry = 0
            r_next.val = val
            # check if the loop continues
            l1_node = l1_node.next if l1_node is not None else None 
            l2_node = l2_node.next if l2_node is not None else None 
            done = not l1_node and not l2_node
            if not done:
                #add a new result node
                r_next.next = ListNode()
                r_next = r_next.next
        if carry == 1:
            r_next.next = ListNode() 
            r_next.next.val = 1
        return result_l 
