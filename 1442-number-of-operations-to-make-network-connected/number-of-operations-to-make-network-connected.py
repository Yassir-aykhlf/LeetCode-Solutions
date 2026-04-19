class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        root = [i for i in range(n)]
        isolated = n
        def find(i):
            if root[i] == i:
                return i
            root[i] = find(root[i])
            return root[i]
        def union(i, j):
            nonlocal isolated
            root1 = find(i)
            root2 = find(j)
            if root1 != root2:
                isolated -= 1
                root[root1] = root2
        for end1, end2 in connections:
            union(end1, end2)
        return isolated - 1