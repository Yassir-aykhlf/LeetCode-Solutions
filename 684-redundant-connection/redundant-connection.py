class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        root = [i for i in range(n + 1)]
        def find(node):
            if root[node] == node:
                return node
            root[node] = find(root[node])
            return root[node]
        def union(end1, end2):
            root1 = find(end1)
            root2 = find(end2)
            if root1 != root2:
                root[root1] = root2
                return True
            return False
        for u, v in edges:
            if not union(u, v):
                return [u, v]