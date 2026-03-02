# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = root.val
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res, node.val + left + right)
            self.res = max(self.res, node.val + left)
            self.res = max(self.res, node.val + right)
            self.res = max(self.res, node.val)
            best_val = max((node.val, node.val + left, node.val + right))
            return best_val
        dfs(root)
        return self.res