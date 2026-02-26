# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode(0) 
        curr = dummy 

        min_heap = []

        for i, node in enumerate(lists):
            if node == None:
                continue
            heapq.heappush(min_heap, (node.val, i))

        while len(min_heap) > 0: 
            val, index = heapq.heappop(min_heap)

    
            curr.next = ListNode(val)
            curr = curr.next
            if(lists[index].next):
                lists[index] = lists[index].next 
                heapq.heappush(min_heap, (lists[index].val, index))

        return dummy.next