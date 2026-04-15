class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        computers = n
        root_idx = [i for i in range(n)]

        def find(node_idx):
            if root_idx[node_idx] == node_idx:
                return node_idx
            root_idx[node_idx] = find(root_idx[node_idx])
            return root_idx[node_idx]

        def union(idx1, idx2):
            root1 = find(idx1)
            root2 = find(idx2)
            if root1 == root2:
                return False
            root_idx[root1] = root2
            return True

        for u, v in connections:
            if union(u, v):
                computers -= 1
        return computers -1