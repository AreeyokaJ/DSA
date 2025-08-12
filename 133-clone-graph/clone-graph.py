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
        
        copy = {}

        def clone(node):
            if not node:
                return None 

            if node in copy:
                return copy[node]

            double = Node(node.val)
            copy[node] = double 

            for nei in node.neighbors:
                double.neighbors.append(clone(nei))

            return double

        return clone(node)