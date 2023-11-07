class Solution:
    def hasPathSum(self, root, targetSum):
        def dfs(root, currentSum):
            if not root:
                return False

            currentSum += root.val

            if not root.left and not root.right:
                return currentSum == targetSum

            return (dfs(root.left, currentSum) or
                    dfs(root.right, currentSum))
        return dfs(root, 0)
