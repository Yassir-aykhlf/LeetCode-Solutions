class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        def dfs(city: int):
            for nei in range(len(isConnected[city])):
                if isConnected[city][nei] and nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        for city in range(n):
            if city not in visited:
                provinces += 1
                visited.add(city)
                dfs(city)
        return provinces