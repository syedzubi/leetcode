class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, root, val):
        if not root:
            return TreeNode(val)

        if val < root.val:
            # we are assigning root.left whose result will eventually be returned
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def minValueNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def remove(self, root, val):
        # BASE CASE
        if not root:
            return None

        # Traversing through the tree
        if val < root.val:
            root.left = self.remove(root.left, val)
        elif val > root.val:
            root.right = self.remove(root.right, val)
        else:
            # we reached the node which needs to be removed
            # case 1 - what if there are no child nodes or if there is only 1 child node
            if not root.left:  # No children on the left
                return root.right
            elif not root.right:  # No children on the right
                return root.left
            else:
                # case 2 - we need to remove a node which has 2 children

                # we need to find the minimum value on the right side or the max value on the left side which can take up
                # the responsibility of ROOT BHAI
                minNode = self.minValueNode(root.right)
                root.val = minNode.val
                root.right = self.remove(root.right, minNode.val)
        return root
