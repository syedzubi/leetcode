def canReachLeafNode(root):
    if not root or root.val == 0:
        return False

    if not root.left and not root.right:  # is it a leaf node || does it not have any children?
        return True
    if canReachLeafNode(root.left):
        return True
    if canReachLeafNode(root.right):
        return True
    return False


def findPathLeaf(root, path):  # path can be an empty array
    if not root or root.val == 0:  # BASE CASE FOR RECURSSION
        return False

    path.append(root.val)
    if not root.left and not root.right:
        return True

    if findPathLeaf(root.left, path):
        return True

    if findPathLeaf(root.right, path):
        return True

    # what if a leaf node is a zero then ur path [4,1,3] needs to be popped out
    path.pop()
    # so that u can search for the other path which is [4,1,2] here 2 doesn't contain any children
    return False
