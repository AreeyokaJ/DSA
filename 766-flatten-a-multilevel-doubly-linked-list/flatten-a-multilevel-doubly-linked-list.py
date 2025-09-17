"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None 

        dummy = Node(0)

        temp = dummy 

        stack = [head]


        while stack:
            curr = stack.pop() 

            if curr.next:
                stack.append(curr.next)
            
            if curr.child:
                stack.append(curr.child)

            temp.next = curr 
            curr.prev = temp 

            curr.child = None 

            temp = curr


        dummy.next.prev = None 
        return dummy.next 
    
        

        
