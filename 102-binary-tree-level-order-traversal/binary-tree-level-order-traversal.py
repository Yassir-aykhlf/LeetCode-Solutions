# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        dq = deque([(root)])
        while dq:
            level_size = len(dq)
            curr_level = []
            for i in range(level_size):
                node = dq.popleft()
                curr_level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            result.append(curr_level)
        return result