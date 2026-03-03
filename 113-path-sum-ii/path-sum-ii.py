# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(node, remaining, currentPath):
            if not node:
                return 
            currentPath.append(node.val)
            if not node.left and not node.right and node.val == remaining:
                result.append(currentPath[:])
            else:
                dfs(node.left, remaining - node.val, currentPath)
                dfs(node.right, remaining - node.val, currentPath)
            currentPath.pop()
        dfs(root, targetSum, [])
        return result