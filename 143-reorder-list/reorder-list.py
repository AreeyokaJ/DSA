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
        #find the middle 

        slow = head 
        fast = head.next 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 


        #break the list into two parts 
        first = head 
        second = slow.next 
        slow.next = None 

        #reverse the second part 

        prev = None 

        while second: 
            temp = second.next 
            second.next = prev 
            prev = second 
            second = temp 
        
        second = prev

        #interwine the two lists 

        while second:
            temp1, temp2 = first.next, second.next 

            first.next = second 
            second.next = temp1 

            first = temp1 
            second = temp2

