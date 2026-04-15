class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        total = n

        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]

        def union(i, j):
            nonlocal total
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                total -= 1
    
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        return total