# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, min_cap, max_cap) -> bool:
            if not node:
                return True
            if not (min_cap < node.val < max_cap):
                return False
            is_left_valid = is_valid(node.left, min_cap, node.val)
            is_right_valid = is_valid(node.right, node.val, max_cap)
            return is_left_valid and is_right_valid
        return is_valid(root, float('-inf'), float('inf'))