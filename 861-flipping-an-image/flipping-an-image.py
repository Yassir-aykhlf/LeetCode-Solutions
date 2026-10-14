class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        res = []
        for row in image:
            res.append(row[::-1])
        for i in range(len(res)):
            for j in range(len(res[0])):
                if res[i][j] == 1:
                    res[i][j] = 0
                else:
                    res[i][j] = 1
        return res