class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degree = {i: 0 for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
        dq = deque([i for i in range(numCourses) if in_degree[i] == 0])
        processed = []
        while dq:
            prereq = dq.popleft()
            processed.append(prereq)
            for course in adj[prereq]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    dq.append(course)
        return processed if len(processed) == numCourses else []