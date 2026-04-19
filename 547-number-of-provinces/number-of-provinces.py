class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        total = n
        root = [i for i in range(n)]
        def find(node):
            if root[node] == node:
                return node
            root[node] = find(root[node])
            return root[node]
        def union(node1, node2):
            nonlocal total
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                root[root1] = root2
                total -= 1
                return
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1 and (i, j) not in visited:
                    union(i, j)
        return total