class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def search(self, root, val):
        if not root:
            return None

        if root.val == val:
            return root  # return True or return whatever u want
        elif val < root.val:
            return self.search(root.left, val)
        else:
            return self.search(root.right, val)
        return None  # or return False or just say nahin mila boss
