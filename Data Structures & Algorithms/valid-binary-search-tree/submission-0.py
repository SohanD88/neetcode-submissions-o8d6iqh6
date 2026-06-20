class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, leftBound, rightBound):
            if not root:
                return True

            if not (leftBound < root.val < rightBound):
                return False

            return dfs(root.left, leftBound, root.val) and dfs(root.right, root.val, rightBound)

        return dfs(root, float("-inf"), float("inf"))