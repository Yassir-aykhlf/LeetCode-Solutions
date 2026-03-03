# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, acc):
            if not node:
                return 0
            acc += node.val
            dfs(node.left, acc)
            dfs(node.right, acc)
            if acc == targetSum and not node.left and not node.right:
                self.res = True
        dfs(root, 0)
        return self.res