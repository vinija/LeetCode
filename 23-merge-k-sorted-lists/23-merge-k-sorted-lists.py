# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
 def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        t = root = ListNode()
        for i in range(len(lists)):
            if lists[i]:
                #When you put the objects (i.e. tuples) into heap, it will compare the first attribute in the object (in this case is key) to compare. If a tie happens, heap wills use the next attribute (i.e. value_1) and so on.
                heap.append((lists[i].val, i, lists[i]))
        heapq.heapify(heap)
        
        while(heap):
            smallest = heapq.heappop(heap)
            nxt = smallest[2].next
            
            root.next = ListNode(smallest[0])
            if(nxt):
                heapq.heappush(heap, (nxt.val,smallest[1],nxt ))
            root = root.next
        return t.next