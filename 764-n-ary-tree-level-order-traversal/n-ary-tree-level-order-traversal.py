"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        dq = deque([(root)])
        result = []
        while dq:
            level_size = len(dq)
            curr_level = []
            for i in range(level_size):
                node = dq.popleft()
                curr_level.append(node.val)
                for child in node.children:
                    dq.append(child)
            result.append(curr_level)
        return result