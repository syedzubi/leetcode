class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root, answer):
        if root:
            answer.append(root.val)
            self.preorderTraversal(root.left, answer)
            self.preorderTraversal(root.right, answer)

    def postorderTraversal(self, root, answer):
        if root:
            self.postorderTraversal(root.left, answer)
            self.postorderTraversal(root.right, answer)
            answer.append(root.val)

    def inorderTraversal(self, root, answer):
        if root:
            self.inorderTraversal(root.left, answer)
            answer.append(root.val)
            self.inorderTraversal(root.right, answer)
