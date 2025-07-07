# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        res = 0 

        def height(root):
            if not root:
                return 0 
            
            left = height(root.left) 
            right = height(root.right) 

            nonlocal res 
            res = max(left + right, res)


            return 1 + max(left, right)


        
        return height(root)