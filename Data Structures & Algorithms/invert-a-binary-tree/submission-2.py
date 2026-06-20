# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stk = [root]
        while stk:
            curr = stk.pop()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                stk.append(curr.left)
            if curr.right:
                stk.append(curr.right)

        return root

