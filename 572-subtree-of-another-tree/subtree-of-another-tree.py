# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True 
        if not root:
            return False 

        if not self.isSameTree(root, subRoot):
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return True 

    

    def isSameTree(self, a, b):
        if not a and not b: 
            return True 
        
        if not a or not b:
            return False 
        
        if a.val == b.val:
            return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)

        return False 
        
