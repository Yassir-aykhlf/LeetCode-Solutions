# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        dq = deque([root])
        left_to_right = True
        while dq:
            level = []
            dq_len = len(dq)
            for i in range(dq_len):
                curr = dq.popleft()
                level.append(curr.val)
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            result.append(level if left_to_right else level[::-1])
            left_to_right = not left_to_right
        return result