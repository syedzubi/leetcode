# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def bfs(self, root):
        queue = deque()
        output = []
        if root:
            queue.append(root)

        while len(queue) > 0:
            for i in range(len(queue)): 
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            output.append(cur.val)
        return output

    def rightSideView(self,root):
        return self.bfs(root)
        