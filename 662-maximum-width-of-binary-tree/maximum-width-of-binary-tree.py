# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_width = 0
        dq = deque([(root, 0)])
        while dq:
            current_width = dq[-1][1] - dq[0][1] + 1
            max_width = max(max_width, current_width)
            dq_len = len(dq)
            for _ in range(dq_len):
                node, index = dq.popleft()
                if node.left:
                    dq.append((node.left, 2 * index))
                if node.right:
                    dq.append((node.right, 2 * index + 1))
        return max_width
        