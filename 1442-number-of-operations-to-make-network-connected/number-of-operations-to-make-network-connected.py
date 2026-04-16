class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        isolated = n
        root = [i for i in range(n)]
        def find(connection):
            if root[connection] == connection:
                return connection
            root[connection] = find(root[connection])
            return root[connection]
        def union(end1, end2):
            nonlocal isolated
            root1 = find(end1)
            root2 = find(end2)
            if root1 != root2:
                isolated -= 1
                root[root1] = root2
        for u, v in connections:
            union(u, v)
        return isolated - 1