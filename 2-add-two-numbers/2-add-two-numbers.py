# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:


        carry = 0 

        z = None
        x = l1
        y = l2

        while x or y: 

            if x and y:
                sumxy = x.val + y.val + carry
            if x is None:
                sumxy = y.val + carry
            if y is None:
                sumxy = x.val + carry
                
            zval = sumxy%10
            carry = int(sumxy/10)

            tnode = ListNode(zval)
            if z is None:
                z = tnode
                nextnode = z
            else:

                nextnode.next = tnode
                nextnode = nextnode.next
            if x:
                x = x.next
            if y:    
                y = y.next
        if carry > 0:
            tnode = ListNode(carry)
            nextnode.next = tnode
        return z

        