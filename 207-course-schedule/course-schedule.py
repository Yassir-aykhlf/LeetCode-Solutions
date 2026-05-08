class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * n
        for v, u in edges:
            adj[u].append(v)
            indegree[v] += 1
        dq = deque([i for i in range(n) if indegree[i] == 0])
        processed_count = 0
        while dq:
            u = dq.popleft()
            processed_count += 1
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    dq.append(v)
        return processed_count == n