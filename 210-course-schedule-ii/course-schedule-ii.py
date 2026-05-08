class Solution:
    def findOrder(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * n
        for v, u in edges:
            adj[u].append(v)
            indegree[v] += 1
        dq = deque([i for i in range(n) if indegree[i] == 0])
        order = []
        while dq:
            u = dq.popleft()
            order.append(u)
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    dq.append(v)
        return order if len(order) == n else []