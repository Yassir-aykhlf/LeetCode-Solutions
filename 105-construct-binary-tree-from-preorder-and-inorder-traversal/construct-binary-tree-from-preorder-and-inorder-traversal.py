# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapping = {val: i for i, val in enumerate(inorder)}
        preorder_index = 0
        def arr_to_tree(left, right):
            if left > right:
                return 
            nonlocal preorder_index
            val = preorder[preorder_index]
            preorder_index += 1
            root_index = inorder[mapping[val]]
            root = TreeNode(val)
            root.left = arr_to_tree(left, mapping[val] - 1)
            root.right = arr_to_tree(mapping[val] + 1, right)
            return root
        return arr_to_tree(0, len(preorder) - 1)