from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root):
    if not root:
        return None

    queue = deque()
    queue.append(root)
    level = 0
    while len(queue) > 0:
        print(f"Level : {level}")
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
                
        level += 1


queue = deque()
