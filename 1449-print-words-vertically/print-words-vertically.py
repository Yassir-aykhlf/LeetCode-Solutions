class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        m = len(words)
        n = 0
        for w in words:
            n = max(n, len(w))
        matrix = [[''] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                matrix[i][j] = words[i][j] if j < len(words[i]) else ''
        res = []
        for j in range(n):
            curr = []
            for i in range(m):
                curr.append(matrix[i][j] if matrix[i][j] != '' else ' ')
            res.append(''.join(curr).rstrip())
        return res