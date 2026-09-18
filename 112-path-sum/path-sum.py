# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = False
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def dfs(node, acc):
            if not node:
                return 0
            if node.val + acc == targetSum and not node.left and not node.right:
                self.res = True
            dfs(node.left, acc + node.val)
            dfs(node.right, acc + node.val)
        dfs(root, 0)
        return self.res