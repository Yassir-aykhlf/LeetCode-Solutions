# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        dq = deque([root])
        depth = 1
        while dq:
            dq_len = len(dq)
            for i in range(dq_len):
                curr = dq.popleft()
                if not curr.left and not curr.right:
                    return depth
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            depth += 1
        return depth