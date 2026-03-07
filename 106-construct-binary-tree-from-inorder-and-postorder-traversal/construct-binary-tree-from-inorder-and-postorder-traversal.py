# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapping = {val: i for i, val in enumerate(inorder)}
        root_idx = len(postorder) - 1
        def arr_to_tree(left, right):
            if left > right:
                return
            nonlocal root_idx
            val = postorder[root_idx]
            root_idx -= 1
            pivot_idx = mapping[val]
            root = TreeNode(val)
            root.right = arr_to_tree(pivot_idx + 1, right)
            root.left = arr_to_tree(left, pivot_idx - 1)
            return root
        return arr_to_tree(0, len(postorder) - 1)