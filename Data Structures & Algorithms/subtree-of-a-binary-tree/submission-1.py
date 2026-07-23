class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2 or r1.val != r2.val:
                return False
            return is_same(r1.left, r2.left) and is_same(r1.right, r2.right)


        def dfs(node):
            if not node:
                return False   

            if is_same(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)

        if not subRoot:
            return True

        return dfs(root)