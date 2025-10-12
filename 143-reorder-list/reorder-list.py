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
        
        #create two seperate lists 
        first = head 
        second = slow.next
        slow.next = None


        #reverse the 2nd list
        prev = None 

        while second:
            temp = second.next 
            second.next = prev 
            prev = second 
            second = temp 

        second = prev

        #interleave the two lists 
        
        while second:
            temp1, temp2 = first.next, second.next 

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2 
        
