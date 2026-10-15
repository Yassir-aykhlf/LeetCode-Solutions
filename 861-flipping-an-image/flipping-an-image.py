class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        def rev(arr):
            for i in range(len(arr)):
                if arr[i]:
                    arr[i] = 0
                else:
                    arr[i] = 1
            return arr
        return [rev(row[::-1]) for row in image]