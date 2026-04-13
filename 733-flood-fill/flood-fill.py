class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        if image[sr][sc] == color:
            return image
        s_color = image[sr][sc]
        def dfs(row, col):
            if row < 0 or row >= m or \
                col < 0 or col >= n or \
                image[row][col] != s_color:
                return
            image[row][col] = color
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        dfs(sr, sc)
        return image