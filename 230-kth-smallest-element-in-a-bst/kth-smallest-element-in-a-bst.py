# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        #dfs inorder - store it to an array {recursive} return k - 1 in array
        #dfs inorder - keep a global count variable return 
        #dfs inorder , iterative 

        # stack = []
        # current = root

        # while stack or current:
        #     while current:
        #         stack.append(current)
        #         current = current.left
                

        #     current = stack.pop()
        #     k -= 1
        #     if k == 0:
        #         return current.val
            
        #     current = current.right


        # count = k
        # ans = 0 

        # def dfs(root):
        #     nonlocal count
        #     nonlocal ans

        #     if not root:
        #         return
            
        #     dfs(root.left)
        #     count -= 1 
        #     if count == 0:
        #         ans = root.val
        #         return

        #     dfs(root.right)
        
        # dfs(root)
        # return ans

        ans = []
        def dfs(root):
            if not root:
                return

            
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)

        
        dfs(root)
        return ans[k - 1]

