# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      h = []
      for l in lists:
        cur = l
        while cur:
          heappush(h, cur.val)
          cur = cur.next
      dummy = cur = ListNode()        
      while len(h) > 0:
        cur.next = ListNode(heappop(h))
        cur = cur.next
      return dummy.next