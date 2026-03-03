# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = {0: 1}
        def dfs(node, acc):
            if not node:
                return 0
            acc += node.val
            prev_acc = acc - targetSum

            path_count = prefix.get(prev_acc, 0)
            prefix[acc] = prefix.get(acc, 0) + 1

            path_count += dfs(node.left, acc)
            path_count += dfs(node.right, acc)
            
            prefix[acc] -= 1
            return path_count
        return dfs(root, 0)