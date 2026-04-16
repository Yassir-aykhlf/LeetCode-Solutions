class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        root = [i for i in range(n)]
        count = n

        def find(node):
            if node == root[node]:
                return node
            root[node] = find(root[node])
            return root[node]

        def union(node1, node2):
            nonlocal count
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                root[root1] = root2
                count -= 1

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    union(i, j)

        return count