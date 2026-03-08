"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        hashmap = {} 

        temp = head
        dummy = Node(0) 
        newList = dummy 


        while temp: 
            newNode = Node(temp.val) 
            newList.next = newNode

            hashmap[temp] = newNode 

            newList = newList.next 
            temp = temp.next
        
        temp = head 

        while temp:
            rand = None 

            if temp.random: 
                rand = hashmap[temp.random]

            currentNode = hashmap[temp] 
            currentNode.random = rand

            temp = temp.next

        return dummy.next