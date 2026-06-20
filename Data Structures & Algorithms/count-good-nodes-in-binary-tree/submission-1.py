class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        goodNodeCt = 0
        stk = [(root, root.val)]

        while stk:
            curr, maxNum = stk.pop()

            if curr.val >= maxNum:
                goodNodeCt += 1

            newMax = max(maxNum, curr.val)

            if curr.left:
                stk.append((curr.left, newMax))

            if curr.right:
                stk.append((curr.right, newMax))

        return goodNodeCt