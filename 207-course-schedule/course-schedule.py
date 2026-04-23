class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        in_degree = {course: 0 for course in range(numCourses)}
        count = 0
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
        dq = deque([node for node in in_degree if in_degree[node] == 0])
        while dq:
            node = dq.popleft()
            count += 1
            for nei in adj[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    dq.append(nei)
        return count == numCourses