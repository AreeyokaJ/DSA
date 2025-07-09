# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
         
        #recursive dfs inorder - store it into an array, and then return k -1  
        ordered_nums = [] 

        def inorder(root):
            if not root:
                return 

            inorder(root.left)

            #visit 
            ordered_nums.append(root.val)

            inorder(root.right) 

            return 

        inorder(root)
        return ordered_nums[k-1]


        #recursive dfs inorder - keep count and return correct 





        #ITERATIVE DFS SOLUTION 
        #stack = []

        # curr = root

        # while stack or curr:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left 

        #     curr = stack.pop()

        #     k -= 1 
        #     if k == 0:
        #         return curr.val

        #     curr = curr.right 
