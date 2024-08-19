# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        num_set = set(nums)

        dummy = ListNode(0)
        dummy.next = head

        current = dummy

        while current.next:
            if current.next.val in num_set:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
        
        