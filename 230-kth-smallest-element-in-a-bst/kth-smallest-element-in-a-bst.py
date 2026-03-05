# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.counter = 0
        self.res = -1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.counter += 1
            if self.counter == k:
                self.res = node.val
            inorder(node.right)
            return
        inorder(root)
        return self.res