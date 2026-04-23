class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degree = {i: 0 for i in range(numCourses)}
        seq = []
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
        dq = deque([node for node in range(numCourses) if in_degree[node] == 0])
        while dq:
            course = dq.popleft()
            seq.append(course)
            for nei in adj[course]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    dq.append(nei)
        return seq if len(seq) == numCourses else []