class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color:
            return image
        og = image[sr][sc]
        def dfs(r, c):
            if not (
                0 <= r < len(image) and
                0 <= c < len(image[0]) and 
                image[r][c] == og
            ):  return
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        dfs(sr, sc)
        return image