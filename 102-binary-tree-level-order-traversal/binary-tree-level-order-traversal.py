# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [] 

        
        queue = deque()
        queue.append(root)
        ans = []

        while len(queue) > 0:

            group = []

            for i in range(len(queue)):
                node = queue.popleft()
                group.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(group)
        
        return ans
