class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        def union(u, v):
            u_parent = find(u)
            v_parent = find(v)
            if u_parent != v_parent:
                parent[v_parent] = u_parent
                return True
            return False
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []