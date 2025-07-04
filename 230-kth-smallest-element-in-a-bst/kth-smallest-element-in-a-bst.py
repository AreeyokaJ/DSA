# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = k 
        kth = root.val 


        def inorder(root):
            if not root:
                return 

            inorder(root.left) 
            nonlocal count 
            nonlocal kth 
            count -= 1 
            if count == 0:
                kth = root.val 
                return 
            inorder(root.right)

        inorder(root)
        return kth
                
        
