# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        #find middle 
        slow = head 
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #split list into two halves 
        second = slow.next
        slow.next = None 

        first = head

        #reverse second list 
        prev = None 

        while second:
            temp = second.next
            second.next = prev 
            prev = second
            second = temp 

        second = prev 

        #interweave the two lists

        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1 
            first = temp1
            second = temp2
        
        