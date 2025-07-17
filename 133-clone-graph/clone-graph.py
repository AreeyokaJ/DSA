"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        cloned = {}

        def clone(node):
            if not node:
                return None 
            
            if node in cloned:
                return cloned[node]

            copy = Node(node.val) 
            cloned[node] = copy 

            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))

            return copy

        return clone(node)

        