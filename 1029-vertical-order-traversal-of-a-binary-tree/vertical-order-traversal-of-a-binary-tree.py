# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # [col] = [(row, val)] 
        col_row_val = defaultdict(list)
        node_row_col = deque([(root, 0, 0)])

        while node_row_col:
            node, row, col = node_row_col.popleft()
            if node:
                col_row_val[col].append((row, node.val))
                node_row_col.append((node.left, row + 1, col - 1))
                node_row_col.append((node.right, row + 1, col + 1))
        
        result = []        
        for col in sorted(col_row_val.keys()):
            sorted_column = sorted(col_row_val[col])
            result.append([val for row, val in sorted_column])
        
        return result