import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        # Create a min-heap
        heap = []
        
        # Push the head of each list into the heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        # Create a dummy node to serve as the starting point of the merged list
        dummy = ListNode(0)
        current = dummy
        
        # While the heap is not empty, keep popping the smallest element
        while heap:
            # Pop the smallest element from the heap
            val, idx, node = heapq.heappop(heap)
            # Add the smallest element to the current list
            current.next = node
            current = current.next
            
            # If there is a next node in the same list, push it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        # Return the merged list, which starts at dummy.next
        return dummy.next
